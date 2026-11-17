"""Nhãn chấm tay TEST3 (A0 baseline, A6 = A4 + gpt-4.1, chọn trước khi chạy test3 — xem selection.json).
Soạn bởi trợ lý AI sau khi đối chiếu ảnh trang gốc và kiểm nội dung từng chunk được trích trong pgvector.
pass (ADVANCED.md): đúng + đủ + đúng đơn vị/phép tính + citation xác định đúng trang/vùng cho MỌI ý.
Câu thiếu bằng chứng: đạt khi từ chối HOẶC nêu rõ tài liệu không có thông tin, không thêm khẳng định vô căn cứ."""
import json
from pathlib import Path

R = Path(__file__).parent / "agent" / "test3"
OK = "Đúng và đủ; citation chứa đúng số liệu/ý trên trang gốc (đã kiểm trong DB và ảnh trang)"
ANS = {
    "A0": {"v06": (0, "Sai dòng bảng: 11/01/2022 – 01/03/2022 là luật sửa đổi nhiều luật; Luật Doanh nghiệp là 17/06/2020, hết hiệu lực một phần (tr. 88)", {0: False}),
           "v07": (0, "Sai ô: 'Quyền phản đối xử lý dữ liệu' là ô số 8; ô số 4 là 'Quyền rút lại sự đồng ý' (tr. 21)", {0: False}),
           "v08": (0, "Sai ô: 'Xây dựng, công bố công khai quy chế' là ô số 3; ô số 2 là 'Chỉ định, công bố công khai đầu mối liên hệ…' (tr. 11)", {}),
           "v13": (0, "Sai: 'Dưới 3 tiếng' 23% không phải cao nhất; cao nhất là 'Từ 3–5 tiếng' 37% (tr. 42)", {0: False, 1: False}),
           "v18": (1, "eMarketer 89,67 tỷ đúng; nói e-Conomy 'không có số liệu' — sai, tr. 34 có 130 tỷ USD (2022)", {1: False}),
           "v24": (0, "Sai/không trả lời đúng ý: không nêu 01 bản chính trong 60 ngày (tr. 24); trích tr. 22–23 không chứa quy định này", {0: False, 1: False})},
    "A6": {"v08": (0, "Sai ô: trả lời ô số 3 ('Xây dựng, công bố công khai quy chế hoạt động'); ô số 2 là 'Chỉ định, công bố công khai đầu mối liên hệ, người đại diện…' (tr. 11, đã đối chiếu ảnh trang). Text layer của sơ đồ không giữ thứ tự ô", {})},
}
UN = {"v25": "Không có Đức trong biểu đồ 1.5 (tr. 30)", "v26": "Mỹ chỉ dự báo đến 2027*", "v27": "Không có Shopee trong biểu đồ du lịch trực tuyến",
      "v28": "Không có Lào", "v29": "Không có chi phí giao hàng tuyệt đối mỗi đơn", "v30": "Không có số doanh nghiệp khảo sát theo tỉnh"}
SEMANTIC_REFUSAL = {("A0", "v27"): "Nêu rõ Shopee không được đề cập trong mảng du lịch; số kèm theo (Traveloka 50%, Agoda 26%, Booking 24%) đúng tr. 47 → coi là từ chối đúng"}
WRONG_UNANS = {("A0", "v26"): "Khẳng định 'Mỹ 2028 dự báo 1.720 tỷ USD' — 1.720 là dự báo 2027*, tài liệu không có 2028"}

for cfg in ("A0", "A6"):
    traces = json.loads((R / cfg / "traces.json").read_text(encoding="utf-8"))
    out = []
    for t in traces:
        qid, cits = t["query_id"], t["citations"]
        if qid in UN:
            if t["status"] == "abstain":
                ok, why = True, UN[qid] + " → từ chối đúng"
            elif (cfg, qid) in SEMANTIC_REFUSAL:
                ok, why = True, SEMANTIC_REFUSAL[(cfg, qid)]
            else:
                ok, why = False, WRONG_UNANS.get((cfg, qid), UN[qid] + " → không từ chối")
            out.append({"query_id": qid, "abstention_correct": ok, "citation_support": [ok] * len(cits), "pass": ok, "reason": why})
            continue
        if t["status"] == "abstain":
            g, why, bad = 0, "Từ chối nhầm câu có đáp án", {}
        else:
            g, why, bad = ANS[cfg].get(qid, (2, OK, {}))
        sup = [bad.get(i, True) for i in range(len(cits))]
        if g == 0 and not bad:
            sup = [False] * len(cits)  # wrong answer: citation does not support the claim made
        out.append({"query_id": qid, "answer_grade": g, "citation_support": sup,
                    "pass": g == 2 and all(sup) and bool(cits), "reason": why})
    (R / cfg / "reviews.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(cfg, "pass", sum(r["pass"] for r in out), "/", len(out))
