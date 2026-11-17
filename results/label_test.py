"""Nhãn chấm tay TEST (A0 baseline, A4 đã chốt). Soạn bởi trợ lý AI sau khi đối chiếu ảnh trang gốc và
kiểm nội dung từng chunk được trích trong pgvector; SV đã rà lại và xác nhận (2026-11-17).
pass (ADVANCED.md): đúng + đủ + đúng đơn vị/phép tính + citation xác định đúng trang/vùng cho MỌI ý."""
import json
from pathlib import Path

R = Path(__file__).parent / "agent" / "test"
OK = "Đúng và đủ; citation chứa đúng số liệu/ý trên trang gốc (đã kiểm trong DB và ảnh trang)"
ANS = {
    "A0": {"t01": (0, "Sai: trả lời phân bố chi tiêu (tr. 48) và tự quy đổi tỷ giá; đáp án 336 USD ở bảng tr. 40", {0: False, 1: False}),
           "t07": (1, "11 quyền đúng; quyền số 11 sai ('khiếu nại, tố cáo, khởi kiện' là số 9; số 11 là 'tự bảo vệ')", {}),
           "t17": (1, "20,5 tỷ đúng; '16,4 tỷ' sai (16,4 là B2C 2022; e-Conomy 2023 là 16 tỷ, tr. 37) → chênh lệch 4,1 sai", {1: False}),
           "t18": (1, "Trung Quốc 50,2% đúng; '3.982 tỷ' là dự báo 2027, đúng là 2.682 tỷ (2022)", {1: False}),
           "t23": (0, "Sai văn bản: nêu Chỉ thị 18/CT-TTg; đúng là Quyết định 645/QĐ-TTg (tr. 3)", {0: False})},
    "A4": {"t17": (1, "Đáp số đúng (20,5 − 16 = 4,5) nhưng chỉ trích tr. 40; số 16 tỷ e-Conomy (tr. 37) không có citation → thiếu evidence", {}),
           "t18": (1, "Trung Quốc 50,2% đúng; '3.982 tỷ' là dự báo 2027 (đúng 2.682 tỷ năm 2022), citation p32:V1 không chứa số này", {}),
           "t20": (1, "34,6% / 24,1% / 10,5 điểm đều đúng nhưng chỉ trích tr. 77; 24,1% ở tr. 82 không có citation → thiếu evidence", {}),
           "t24": (0, "Từ chối nhầm: tr. 13 có đủ 2 nội dung đánh giá định kỳ", {})},
}
NEEDS_ALL_EVIDENCE = {("A4", "t17"), ("A4", "t20")}  # câu trả lời đúng nhưng citation thiếu một trang bắt buộc
UN_REASON = {"t25": "Không có B2C Việt Nam 2024 (chỉ có 2018–2023; 2024* chỉ cho toàn cầu/TQ/Mỹ)",
             "t26": "Không có Nhật Bản trong biểu đồ 1.3 (tr. 29)", "t27": "Không có thị phần GMV; 81% là tỷ lệ người dùng ưa chuộng (tr. 46)",
             "t28": "Không nêu mức phạt trong phần Nghị định 13/2023", "t29": "Không có Úc trong biểu đồ 2.3.2 (tr. 63)",
             "t30": "Không có tỷ lệ hoàn trả đơn hàng"}

for cfg in ("A0", "A4"):
    traces = json.loads((R / cfg / "traces.json").read_text(encoding="utf-8"))
    out = []
    for t in traces:
        qid, cits = t["query_id"], t["citations"]
        if qid in UN_REASON:
            ok = t["status"] == "abstain"
            out.append({"query_id": qid, "abstention_correct": ok, "citation_support": [False] * len(cits), "pass": ok,
                        "reason": UN_REASON[qid] + (" → từ chối đúng" if ok else f" → KHÔNG từ chối, khẳng định vô căn cứ: {t['answer'][:100]}")})
            continue
        if t["status"] == "abstain":
            g, why, bad = ANS[cfg].get(qid, (0, "Từ chối nhầm câu có đáp án", {}))
            g = 0
        else:
            g, why, bad = ANS[cfg].get(qid, (2, OK, {}))
        sup = [bad.get(i, True) for i in range(len(cits))]
        passed = g == 2 and all(sup) and bool(cits) and (cfg, qid) not in NEEDS_ALL_EVIDENCE
        out.append({"query_id": qid, "answer_grade": g, "citation_support": sup, "pass": passed, "reason": why})
    (R / cfg / "reviews.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(cfg, "pass", sum(r["pass"] for r in out), "/", len(out))
