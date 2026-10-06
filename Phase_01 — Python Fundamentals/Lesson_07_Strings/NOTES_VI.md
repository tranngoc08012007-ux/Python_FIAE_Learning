# GIÁO ÁN BUỔI 7 — Chuỗi (String) trong Python
> Lộ trình FIAE • Giai đoạn 1 — Python Cơ Bản

---

## 1. F-string

Chèn biến/biểu thức vào chuỗi bằng `f"...{}..."`.

```python
name = "Ngọc"
age = 20
print(f"Xin chào {name}, bạn {age} tuổi")       # chèn biến
print(f"Năm sau bạn {age + 1} tuổi")             # chèn biểu thức
print(f"Giá: {19.5:.2f} EUR")                    # Giá: 19.50 EUR
```

> `.2f` → định dạng số thực, giữ 2 chữ số sau dấu thập phân.

Ưu điểm so với nối chuỗi bằng `+`: ngắn gọn, không cần `str()`, dễ đọc hơn khi có nhiều biến.

---

## 2. Index & Slicing

**Index bắt đầu từ 0**, index âm đếm từ cuối (`-1` = ký tự cuối).

```python
text = "Python"
#        P  y  t  h  o  n
#        0  1  2  3  4  5
#       -6 -5 -4 -3 -2 -1
```

**Cú pháp slicing:** `string[start:stop:step]` — `start` bao gồm, `stop` **không** bao gồm.

```python
text[0:3]     # "Pyt"   → 3 ký tự đầu
text[:5]      # "Pytho" → bỏ start = từ đầu
text[2:]      # "thon"  → bỏ stop = đến cuối
text[-4:]     # "thon"  → 4 ký tự cuối
text[::2]     # "Pto"   → step=2, cách 1 ký tự
text[::-1]    # "nohtyP" → đảo ngược chuỗi
```

> 💡 Ghi nhớ: `text[::-1]` = reverse string — pattern rất hay dùng.

---

## 3. String Methods thường dùng

| Method | Công dụng | Ví dụ | Kết quả |
|---|---|---|---|
| `.strip()` | Xoá khoảng trắng đầu/cuối | `"  Hi  ".strip()` | `"Hi"` |
| `.split(sep)` | Chuỗi → List | `"Berlin,DE".split(",")` | `["Berlin","DE"]` |
| `sep.join(list)` | List → Chuỗi | `", ".join(["a","b"])` | `"a, b"` |
| `.upper()` | Chữ hoa | `"py".upper()` | `"PY"` |
| `.lower()` | Chữ thường | `"PY".lower()` | `"py"` |
| `.replace(old,new)` | Thay thế | `"Hi World".replace(" ","_")` | `"Hi_World"` |

**Lưu ý:**
- `strip()` không xoá khoảng trắng **ở giữa** chuỗi.
- `split()` mặc định tách theo khoảng trắng nếu không truyền tham số.
- `join()` được gọi từ separator: `"-".join(["2026","08","11"])` → `"2026-08-11"`.

---

## 4. So sánh chuỗi (String Comparison)

```python
"apple" == "apple"    # True
"Apple" == "apple"    # False — phân biệt hoa/thường
"Apple" < "apple"     # True — so sánh theo giá trị Unicode
```

> ⚠️ String comparison **phân biệt chữ hoa/thường**. Khi xử lý input người dùng, nên chuẩn hoá bằng `.lower()` trước khi so sánh:
```python
if user_input.lower() == "admin":
    print("Welcome!")
```

---

## 5. Kết hợp nhiều Method (thực tế)

```python
location = "   Berlin, Germany   "
parts = location.strip().split(",")
city = parts[0].strip()
country = parts[1].strip().upper()
print(city)      # Berlin
print(country)   # GERMANY
```

Quy trình xử lý chuỗi thực tế: **Raw Input → Clean (strip) → Parse (split) → Normalize (upper/lower) → Compare/Process → Output**.

---

## 6. Bài Tập

1. **Formatted Greeting** — dùng f-string (không `+`), in: `Xin chào Ngọc, năm sau bạn sẽ 21 tuổi.`
2. **Structured ID** — với `data = "VN-2026-123456"`, dùng **slicing** (không `split()`) lấy `Country code`, `Year`, `ID`.
3. **Clean Location** — với `"   Berlin, Germany   "`, dùng `strip()`, `split()`, `upper()` để lấy `City: Berlin` và `Country: GERMANY`.

---

## 7. Tổng kết — 4 nhóm cần nhớ

```
FORMAT     → f-string                          → tạo output đẹp
ACCESS     → index + slicing                    → lấy dữ liệu từ string
MANIPULATE → strip/split/join/upper/lower/replace → làm sạch & biến đổi
COMPARE    → == != < >                           → kiểm tra dữ liệu
```
