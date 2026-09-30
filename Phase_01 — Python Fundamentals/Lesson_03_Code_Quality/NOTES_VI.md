# Bài 3: Code Quality Tools

## I. Khái niệm
* **PEP 8** là bộ quy tắc viết code Python chuẩn, được cộng đồng toàn thế giới tuân theo.
* **`black`** (Auto-formatter):
  * Tự động sửa định dạng code.
  * Không cần nghĩ về format, `black` lo hết.
  * Chạy lệnh: `black <file.py>` hoặc `black .`
* **`flake8`** (Linter):
  * Chỉ ra lỗi về style và cú pháp.
  * Không tự sửa, chỉ báo lỗi.
  * Chạy lệnh: `flake8 <file.py>` hoặc `flake8 .`
* **Quy tắc nhớ nhanh:** 
  `black` = thợ sửa | `flake8` = thanh tra

---

## II. Các lệnh quan trọng

```bash
pip install black flake8    # Cài đặt
flake8 <file.py>            # Kiểm tra lỗi
black <file.py>             # Tự động sửa
flake8 .                    # Kiểm tra toàn bộ project
black .                     # Sửa toàn project
```

---

## III. Các file cấu hình trong bài
* **File 1:** `.flake8` — Đặt ở thư mục gốc
  * Nội dung: `max-line-length = 88` (vì phải đồng bộ với `black`)
* **File 2:** `.vscode/settings.json` — Format tự động khi nhấn `Ctrl + S`
  * Lưu ý: File này không push lên GitHub vì là cấu hình cá nhân.

---

## IV. Mã lỗi PEP 8 thường gặp

| Mã lỗi | Ý nghĩa | Sai | Đúng |
| :---: | :--- | :--- | :--- |
| **E225** | Thiếu khoảng cách quanh toán tử | `x=10` | `x = 10` |
| **E231** | Thiếu khoảng cách sau dấu phẩy | `f(a,b)` | `f(a, b)` |
| **E201** | Thừa khoảng trắng sau `(` | `( a, b)` | `(a, b)` |
| **E202** | Thừa khoảng trắng trước `)` | `(a, b )` | `(a, b)` |
| **E302** | Thiếu hai dòng trống trước hàm | 0 dòng trống | 2 dòng trống |
| **E305** | Thiếu hai dòng trống sau hàm | 1 dòng trống | 2 dòng trống |
| **W292** | Thiếu dòng cuối trong file | Không có | 1 dòng trống |

---

## V. Quy trình chuẩn

```text
Viết Code
    │
    ▼
Ctrl + S  ──►  black tự động chạy
    │
    ▼
flake8 .  ──►  kiểm tra lần cuối
    │
    ▼
git add .
git commit -m "feat: ..."
git push
```

---

## VI. Lý do quan trọng trong thực tế
* Trong Betrieb Đức, code được review bởi Ausbilder.
* Code không đúng PEP 8 thể hiện sự thiếu chuyên nghiệp.
* Nhiều công ty có CI/CD tự động reject code không qua được `flake8`.
* `black` giúp cả team không mất thời gian tranh luận về style code.
* Là kĩ năng quan trọng thường được hỏi trong phỏng vấn FIAE.