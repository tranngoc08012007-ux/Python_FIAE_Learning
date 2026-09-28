#  Giáo án Python — Buổi 1
**Lộ trình Fachinformatiker Anwendungsentwicklung**
_Giai đoạn 1 | Buổi 1 | 17/6/2026_

---

##  Thông tin buổi học

| | |
|---|---|
| **Chủ đề** | Cài đặt môi trường & Hello World |
| **Thời lượng** | 1–2 giờ |
| **Mục tiêu** | Chạy được file Python, hiểu print(), comment và biến |
| **Công cụ** | VS Code, PowerShell/Terminal, Python 3.11+ |

---

## ① Terminal & Cách Python chạy code

Python cần một phiên dịch viên (interpreter) để hiểu và thực thi code.
Bạn giao tiếp với nó qua terminal.

Kiểm tra Python đã cài chưa:
```bash
python --version
```

In dữ liệu ra màn hình:
```python
print("Hello, World!")
print("Tôi đang học Python!")
print(2 + 3)          # Python tự tính kết quả
```

Chạy file Python:
```bash
python hello.py
```

---

## ② Comment — Ghi chú trong code

Comment là ghi chú cho người đọc. Python bỏ qua hoàn toàn khi chạy.
Dùng dấu `#` để tạo comment.

```python
# Comment trên dòng — phổ biến nhất
print("Xin chào")  # Comment cuối dòng — cũng dùng nhiều
```

>  **Lưu ý:**
> - Không được chen comment vào giữa lệnh
> - Trong môi trường Ausbildung → nên viết comment bằng tiếng Đức

---

## ③ Biến (Variable) — Ô chứa dữ liệu

Biến là ô nhớ có tên. Lưu giá trị vào để tái sử dụng nhiều lần.
Trong Python không cần khai báo kiểu dữ liệu.

**Cú pháp:**
```python
tên_biến = giá_trị
```

**Ví dụ:**
```python
name = "Trần Nguyên Ngọc"       # Mein Name
beruf = "Fachinformatiker..."    # Mein Beruf
geburtsjahr = 2007               # Mein Geburtsjahr
alter = 2026 - geburtsjahr       # Mein Alter
print(alter)                     # → 19
```

**Quy tắc đặt tên biến:**
- Dùng `snake_case` — chữ thường, nối bằng dấu `_` (ví dụ: `nam_sinh`)
- Không bắt đầu bằng số
- Không dùng khoảng trắng
- Có thể ghi đè: `alter = 20` → giá trị mới thay giá trị cũ

---

##  Nguyên tắc quan trọng

- **Don't Repeat Yourself** — dùng biến thay vì gõ cứng giá trị nhiều lần
- Dùng biến để tính biến → nếu thay đổi chỉ cần sửa 1 chỗ
- Comment tiếng Đức → chuẩn bị cho môi trường làm việc tại Đức

---

##  10 từ tiếng Đức quan trọng

| # | Tiếng Đức | Tiếng Việt | Ví dụ |
|---|---|---|---|
| 1 | **die Variable** | biến | `name = "Ngọc"` |
| 2 | **der Wert** | giá trị | 19 là Wert của alter |
| 3 | **der Kommentar** | comment / ghi chú | `# Mein Name` |
| 4 | **die Ausgabe** | đầu ra / kết quả | Terminal hiển thị Ausgabe |
| 5 | **der Befehl** | lệnh | print() là ein Befehl |
| 6 | **zuweisen** | gán (giá trị) | `alter = 19` → zuweisen |
| 7 | **überschreiben** | ghi đè | `alter = 20` überschreibt |
| 8 | **ausführen** | chạy / thực thi | `python hello.py` ausführen |
| 9 | **der Speicher** | bộ nhớ | Biến lưu im Speicher |
| 10 | **die Umgebung** | môi trường | Python-Umgebung |

---

##  Tổng kết buổi 1

- `python hello.py` — chạy file Python qua terminal
- `print()` — in dữ liệu ra màn hình
- `#` — comment, ghi chú cho người đọc, Python bỏ qua
- **Biến** — tạo, gán, tái sử dụng, ghi đè giá trị
- **snake_case** — quy tắc đặt tên biến chuẩn Python

---

_Buổi tiếp theo: **Virtual Environment & pip (venv)**_