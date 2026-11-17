"""Nhãn chấm tay TEST2 (A0 baseline, A4 đã chốt trên dev). Soạn bởi trợ lý AI sau khi đối chiếu ảnh trang gốc
và kiểm nội dung từng chunk được trích trong pgvector; TODO(SV): rà lại từng nhãn.
pass (ADVANCED.md): đúng + đủ + đúng đơn vị/phép tính + citation xác định đúng trang/vùng cho MỌI ý.
Câu thiếu bằng chứng: đạt khi từ chối HOẶC nêu rõ tài liệu không có thông tin, không thêm khẳng định vô căn cứ."""
import json
from pathlib import Path

R = Path(__file__).parent / "agent" / "test2"
OK = "Đúng và đủ; citation chứa đúng số liệu/ý trên trang gốc (đã kiểm trong DB và ảnh trang)"
ANS = {
    "A0": {"u07": (0, "Sai: 'Quyền yêu cầu bồi thường thiệt hại' là ô số 10; ô số 7 là 'Quyền cung cấp dữ liệu' (tr. 21)", {0: False}),
           "u10": (1, "1.218 và 1,1% đúng nhưng tự thêm 'năm 2022 có 1.204' — không có trong chunk được trích hay tài liệu (khẳng định vô căn cứ)", {}),
           "u16": (0, "Sai đối tượng: 60% 'Chuyển khoản' là phương thức thanh toán của NGƯỜI TIÊU DÙNG (tr. 47); câu hỏi về doanh nghiệp: Internet banking 87% (tr. 64)", {0: False}),
           "u18": (1, "Shopee 81% đúng; phần doanh nghiệp vận hành sai (liệt kê các sàn khác thay vì Công ty TNHH Shopee, tr. 83)", {})},
    "A4": {"u07": (0, "Sai: 'Quyền yêu cầu bồi thường thiệt hại' là ô số 10; ô số 7 là 'Quyền cung cấp dữ liệu' (tr. 21)", {0: False}),
           "u18": (1, "Shopee 81% và Công ty TNHH Shopee đều đúng, nhưng chỉ trích tr. 46; tên doanh nghiệp (tr. 83) không có citation → thiếu evidence", {}),
           "u19": (1, "1.144,99 tỷ và 19,2% đều đúng, nhưng chỉ trích tr. 31; 19,2% (tr. 32) không có trong chunk được trích → thiếu evidence", {}),
           "u20": (1, "ShopeeFood/Foody 51% và Công ty Cổ phần Foody đều đúng, nhưng chỉ trích tr. 47; tên doanh nghiệp (tr. 84/83) không có citation → thiếu evidence", {}),
           "u23": (0, "Từ chối nhầm: tr. 25 có 'Trục phát triển hợp đồng điện tử Việt Nam'", {}),
           "u24": (0, "Từ chối nhầm: tr. 11 ô số 4 có đủ thông tin", {})},
}
NEEDS_ALL_EVIDENCE = {("A4", "u18"), ("A4", "u19"), ("A4", "u20")}
UN = {"u25": "Không có Mỹ trong biểu đồ 1.5 (tr. 30)", "u26": "Không có Campuchia", "u27": "Không có Tiki trong biểu đồ giao đồ ăn",
      "u28": "Không có số đơn hàng tuyệt đối", "u29": "Không có phần mềm quản lý kho", "u30": "Không có mức lương"}
# câu thiếu bằng chứng mà agent "answered" nhưng nội dung là nêu rõ tài liệu không có thông tin (không khẳng định vô căn cứ)
SEMANTIC_REFUSAL = {("A0", "u27"): "Nêu rõ Tiki không có trong danh sách giao đồ ăn; các số kèm theo (51%, 50%, 15%, 7%, 13%) đúng tr. 47 → coi là từ chối đúng",
                    ("A0", "u29"): "Nêu rõ tài liệu không nêu phần mềm quản lý kho; các số phần mềm khác đúng tr. 55 → coi là từ chối đúng"}
WRONG_UNANS = {("A4", "u28"): "Khẳng định '61 triệu đơn hàng thành công' — 61 triệu là số NGƯỜI TIÊU DÙNG mua sắm trực tuyến (tr. 40), không phải số đơn hàng"}

for cfg in ("A0", "A4"):
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
            g, why, bad = ANS[cfg].get(qid, (0, "Từ chối nhầm câu có đáp án", {}))
            g = 0
        else:
            g, why, bad = ANS[cfg].get(qid, (2, OK, {}))
        sup = [bad.get(i, True) for i in range(len(cits))]
        passed = g == 2 and all(sup) and bool(cits) and (cfg, qid) not in NEEDS_ALL_EVIDENCE
        out.append({"query_id": qid, "answer_grade": g, "citation_support": sup, "pass": passed, "reason": why})
    (R / cfg / "reviews.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(cfg, "pass", sum(r["pass"] for r in out), "/", len(out))
