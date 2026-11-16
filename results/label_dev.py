"""Nhãn chấm tay dev (A0–A3). Người soạn: trợ lý AI, đối chiếu ảnh trang gốc; TODO(SV): rà lại.
Quy ước: answer_grade 0/1/2 theo BENCHMARK.md; pass theo ADVANCED.md (đúng+đủ+đơn vị+citation hỗ trợ);
citation_support: mỗi citation có trong context VÀ đọc thấy hỗ trợ ý được trích."""
import json
from pathlib import Path

R = Path(__file__).parent / "agent" / "dev"
# (grade, reason, {citation_index: False}) cho câu có đáp án; mặc định grade 2 + mọi citation đúng
ANS = {
    "A0": {"d08": (0, "Ghi 5.060 triệu (số T1/2022) thay vì 5.158; tăng trưởng 1,90% đúng", {0: False, 1: False}),
           "d10": (1, "47%/57% đúng nhưng 'giảm 10%' sai đơn vị (đúng: 10 điểm %)", {}),
           "d11": (0, "28,8% là tỷ lệ CCDV; đúng: bán hàng 71,2%. Text layer Day 6 ghép nhãn biểu đồ tròn mơ hồ", {0: False}),
           "d12": (0, "Lấy 24 tỷ (Việt Nam 2025*) thay vì 16 tỷ (2023) → 2,58 lần sai", {1: False}),
           "d14": (1, "78% sai (đúng 78,6% người dân dùng Internet); 78% mua sắm đúng", {0: False})},
    "A1": {"d02": (0, "Từ chối nhầm: bảng tr. 83 có thuocsi.vn – Buymed", {}),
           "d08": (1, "Giá trị đúng chữ số nhưng viết '5,158 triệu' (theo cách viết VN = 5,158 triệu người, sai 1000 lần; đúng 5.158 triệu)", {}),
           "d10": (1, "47%/57% đúng nhưng 'giảm 10%' sai đơn vị (đúng: 10 điểm %)", {}),
           "d11": (0, "28,8% sai (đúng 71,2%): chunk V tr. 68 đảo nhãn biểu đồ tròn", {0: False}),
           "d12": (0, "Từ chối nhầm câu multi-hop có đáp án", {})},
    "A2": {"d01": (0, "Từ chối nhầm (kiểm trích dẫn nguyên văn quá chặt)", {}),
           "d04": (0, "Từ chối nhầm (kiểm trích dẫn quá chặt)", {}),
           "d08": (0, "Từ chối nhầm (đoạn trích bị đổi định dạng số)", {}),
           "d10": (0, "Từ chối nhầm (đoạn trích không khớp chunk)", {}),
           "d11": (0, "28,8% sai (đúng 71,2%): chunk V tr. 68 đảo nhãn", {0: False}),
           "d12": (0, "Từ chối nhầm (sai ID p37/p037, đoạn trích diễn đạt lại)", {}),
           "d13": (0, "Từ chối nhầm", {}), "d14": (0, "Từ chối nhầm", {})},
    "A3": {"d08": (1, "Viết '5,158 triệu' (sai thang theo cách viết VN; đúng 5.158 triệu)", {}),
           "d10": (1, "47%/57% đúng nhưng 'giảm 10%' sai đơn vị (đúng: 10 điểm %)", {}),
           "d11": (0, "28,8% sai (đúng 71,2%): chunk V tr. 68 đảo nhãn", {0: False}),
           "d12": (1, "Đáp số 3,875 đúng nhưng số 16 lấy từ PHILIPPINES 2023 (tr. 35), không phải Việt Nam (tr. 37): citation không hỗ trợ ý Việt Nam", {1: False}),
           "d14": (1, "78,6% đúng; '60,7% tham gia mua sắm' sai (đó là tỷ lệ mua sắm hàng tuần tr. 30; đúng 78% tr. 44)", {1: False})},
    "A4": {"d11": (0, "28,8% sai (đúng 71,2%): chunk V tr. 68 đảo nhãn; luật 'B và V mâu thuẫn' không kích hoạt vì B cũng ghép mơ hồ", {0: False}),
           "d14": (1, "78,6% đúng; '60,7% tham gia mua sắm' sai chỉ tiêu (tỷ lệ mua sắm hàng tuần tr. 30; đúng 78% tr. 44) dù đã có luật kiểm chỉ tiêu", {1: False})},
    "A5": {"d03": (0, "Sai: 31,7% là Internet banking; ví điện tử CCDV là 7,5% (tr. 72). A4 trả lời đúng câu này → biến động của model", {0: False}),
           "d11": (0, "28,8% sai (đúng 71,2%): chunk V tr. 68 đảo nhãn", {0: False}),
           "d12": (1, "Đáp số 3,875 đúng nhưng số 16 lấy từ Philippines (p035:B03); kiểm 'đủ citation' không bắt được vì số có trong chunk được trích, sai đối tượng", {1: False}),
           "d14": (1, "78,6% đúng; 60,7% sai chỉ tiêu (mua sắm hàng tuần tr. 30) dù có luật chỉ tiêu", {1: False})},
}
# câu thiếu bằng chứng: True nếu agent từ chối
UNANS = {"d17", "d18", "d19", "d20"}
UN_REASON = {"d17": "Doanh thu B2C 2017 không có (biểu đồ bắt đầu 2018)", "d18": "Không có thời gian giao hàng",
             "d19": "Lazada không có trong biểu đồ giao đồ ăn", "d20": "Không có số người dùng Internet tuyệt đối của VN"}

for cfg in ("A0", "A1", "A2", "A3", "A4", "A5"):
    traces = json.loads((R / cfg / "traces.json").read_text(encoding="utf-8"))
    out = []
    for t in traces:
        qid, cits = t["query_id"], t["citations"]
        if qid in UNANS:
            ok = t["status"] == "abstain"
            reason = UN_REASON[qid] + (" → từ chối đúng" if ok else f" → KHÔNG từ chối, trả lời: {t['answer'][:90]}")
            out.append({"query_id": qid, "abstention_correct": ok, "citation_support": [False] * len(cits),
                        "pass": ok, "reason": reason})
            continue
        if t["status"] == "abstain":
            g, why, bad = ANS[cfg].get(qid, (0, "Từ chối nhầm câu có đáp án", {}))
            g = 0
        else:
            g, why, bad = ANS[cfg].get(qid, (2, "Đúng và đủ, citation đúng trang/vùng (đối chiếu ảnh trang)", {}))
        sup = [bad.get(i, True) for i in range(len(cits))]
        out.append({"query_id": qid, "answer_grade": g, "citation_support": sup,
                    "pass": g == 2 and all(sup) and bool(cits), "reason": why})
    (R / cfg / "reviews.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(cfg, sum(r["pass"] for r in out), "/", len(out))
