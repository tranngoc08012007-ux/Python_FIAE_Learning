# GIÁO ÁN BUỔI 6 — Biến & Kiểu Dữ Liệu trong Python
> Lộ trình FIAE • Giai đoạn 1 — Python Cơ Bản

---

## 1. Biến (Variable) là gì?

Biến là một cái tên bạn đặt để **lưu trữ một giá trị trong bộ nhớ máy tính**, để dùng lại về sau. Python tự động nhận diện kiểu dữ liệu khi bạn gán giá trị — không cần khai báo kiểu như Java hay C#.

**Cú pháp:**
```
ten_bien = gia_tri
```

**Ví dụ:**
```python
name = "Ngoc"       # gán chuỗi "Ngoc" vào biến name
age = 18             # gán số nguyên 18 vào biến age
height = 1.75        # gán số thực 1.75 vào biến height
```

> 💡 Tên biến trong Python nên dùng **snake_case** (chữ thường, cách nhau bằng dấu gạch dưới). Ví dụ: `ten_san_pham`, `so_luong`, `nam_sinh`.

---

## 2. Kiểu Dữ Liệu Cơ Bản

Python có 5 kiểu dữ liệu cơ bản cần nắm vững:

| Kiểu dữ liệu | Ví dụ | Ý nghĩa |
|---|---|---|
| `int` | `age = 18` | Số nguyên (không có phần thập phân) |
| `float` | `height = 1.75` | Số thực (có phần thập phân) |
| `str` | `name = "Ngoc"` | Chuỗi ký tự văn bản |
| `bool` | `is_graduated = False` | Giá trị True hoặc False |
| `None` | `note = None` | Không có giá trị — chưa được gán |

**Ví dụ khai báo đầy đủ:**
```python
name = "Ngoc"            # str
age = 18                 # int
height = 1.75             # float
is_graduated = False      # bool
note = None               # NoneType
```

> ⚠️ `bool` chỉ có 2 giá trị: `True` hoặc `False` — **viết hoa chữ đầu**. Viết `true` hay `TRUE` đều báo lỗi.

> ⚠️ `None` khác với `0`, `""` (chuỗi rỗng), hay `False`. `None` nghĩa là hoàn toàn chưa có giá trị.

---

## 3. Kiểm Tra Kiểu Dữ Liệu với `type()`

Hàm `type()` dùng để kiểm tra một biến đang thuộc kiểu dữ liệu nào. Rất hữu ích khi debug hoặc khi nhận dữ liệu từ bên ngoài (người dùng nhập, file, API).

```python
print(type(name))           # <class 'str'>
print(type(age))            # <class 'int'>
print(type(height))         # <class 'float'>
print(type(is_graduated))   # <class 'bool'>
print(type(note))           # <class 'NoneType'>
```

> 💡 `type()` trả về một giá trị — không bắt buộc phải nằm trong `print()`. Bạn có thể gán vào biến hoặc dùng trong điều kiện `if`.

---

## 4. Phép Toán Số Học

| Phép toán | Ký hiệu | Ví dụ | Kết quả |
|---|---|---|---|
| Cộng | `+` | `18 + 5` | `23` |
| Trừ | `-` | `18 - 5` | `13` |
| Nhân | `*` | `7.5 * 20` | `150.0` |
| Chia (float) | `/` | `18 / 3` | `6.0` |
| Chia lấy nguyên | `//` | `18 // 3` | `6` |
| Chia lấy dư | `%` | `18 % 3` | `0` |

> ⚠️ `float * int` hoặc `float / int` → kết quả **luôn là float**. Ví dụ: `7.5 * 20 = 150.0` (không phải `150`).

**Ví dụ:**
```python
total = age + 5          # 23 (int)
division = age / 3       # 6.0 (float — chia luôn ra float)
floor_div = age // 3     # 6 (int — chỉ lấy phần nguyên)
remainder = age % 3      # 0 (int — phần dư)
print(f"Kết quả: {total}, {division}, {floor_div}, {remainder}")
```

---

## 5. Ép Kiểu (Type Casting)

Ép kiểu là chuyển đổi một biến từ kiểu dữ liệu này sang kiểu khác. Cần thiết khi bạn nhận dữ liệu dưới dạng `str` nhưng cần tính toán.

**Các hàm ép kiểu phổ biến:**
- `int()` → chuyển sang số nguyên (cắt bỏ phần thập phân, **không làm tròn**)
- `float()` → chuyển sang số thực
- `str()` → chuyển sang chuỗi

**Ví dụ:**
```python
diem = "85"              # str (nhận từ input)
diem_so = int(diem)      # int: 85

chieu_cao = int(1.99)    # int: 1 (không phải 2 — cắt, không làm tròn!)
tuoi_str = str(18)       # str: "18"
```

---

## 6. f-string — Chèn Biến vào Chuỗi Văn Bản

f-string là cách gọn gàng nhất để chèn giá trị biến vào trong một chuỗi. Thêm chữ `f` trước dấu nháy mở, rồi đặt biến hoặc biểu thức trong cặp ngoặc nhọn `{}`.

**Cú pháp:**
```
f"văn bản {biến} văn bản {biểu_thức}"
```

**Ví dụ:**
```python
name = "Ngoc"
age = 18
print(f"Tôi tên {name}, năm nay {age} tuổi.")
# Output: Tôi tên Ngoc, năm nay 18 tuổi.

# Tính toán trực tiếp bên trong {}
print(f"Sang năm tôi {age + 1} tuổi.")
# Output: Sang năm tôi 19 tuổi.
```

> 💡 Trước f-string, cần nối chuỗi bằng dấu `+`, rất rườm rà:
> `"Tôi tên " + name + ", " + str(age) + " tuổi."`
> f-string giải quyết vấn đề này gọn gàng hơn nhiều.

---

## 7. `input()` — Nhận Dữ Liệu từ Người Dùng

`input()` dừng chương trình lại, chờ người dùng gõ gì đó và nhấn Enter, rồi trả về giá trị đó dưới dạng `str`.

> ⚠️ `input()` **LUÔN LUÔN trả về `str`** — dù người dùng gõ số hay chữ. Đây là nguyên nhân phổ biến gây lỗi `TypeError` khi tính toán.

**Ví dụ lỗi điển hình:**
```python
user_age = input("Nhập tuổi: ")   # user_age là str, ví dụ "18"
print(user_age + 1)                # LỖI: không cộng str với int được!
```

**Cách đúng — ép kiểu ngay khi nhận input:**
```python
age = int(input("Nhập tuổi: "))    # ép sang int luôn trong 1 dòng
print(f"Sang năm bạn {age + 1} tuổi.")  # OK
```

---

## 8. `print()` Nâng Cao — `sep` và `end`

### 8.1 Tham số `sep` (separator)

`sep` quyết định ký tự nào sẽ được chèn **giữa các giá trị** khi bạn in nhiều thứ cùng lúc trong một lệnh `print()`. Mặc định `sep=" "` (dấu cách).

```python
print("Python", "FAE", "2026")            # Python FAE 2026
print("Python", "FAE", "2026", sep="-")   # Python-FAE-2026
print("Python", "FAE", "2026", sep=" | ") # Python | FAE | 2026
```

### 8.2 Tham số `end`

`end` quyết định ký tự nào được thêm vào **sau khi `print()` in xong** nội dung. Mặc định `end="\n"` (xuống dòng mới).

```python
print("Đang xử lý", end="...")
print("hoàn tất!")
# Output: Đang xử lý...hoàn tất!  (trên cùng 1 dòng)
```

> 💡 `sep` áp dụng **giữa các phần tử** trong cùng một lệnh `print()`.
> `end` áp dụng **ở cuối** của lệnh `print()` đó.

---

## 9. Tổng Kết — Những Điều Cần Nhớ

- Python tự nhận diện kiểu dữ liệu — không cần khai báo kiểu như Java/C#
- 5 kiểu cơ bản: `int`, `float`, `str`, `bool`, `None`
- `float * int` hoặc `float / int` → kết quả **luôn là `float`**
- `input()` luôn trả về `str` — **phải ép kiểu** trước khi tính toán
- `int()` cắt phần thập phân, **không làm tròn**: `int(1.99) = 1`
- f-string dùng `f"...{biến}..."` — gọn hơn nối chuỗi bằng `+`
- `sep` áp dụng giữa các phần tử; `end` áp dụng ở cuối `print()`

---

## 10. Bài Tập Tự Luyện

> ⚠️ Viết từng bài tập ra vở tay trước khi gõ vào máy — giúp não ghi nhớ cú pháp lâu hơn nhiều.

1. Khai báo đủ 5 kiểu dữ liệu, dùng `type()` in kiểu của từng biến
2. Nhận `input()` tên và năm sinh, tính tuổi, in theo format: `Name: [tên] | Age: [tuổi]` bằng `sep`
3. In 3 câu `print()` liên tiếp nhưng kết quả hiện trên cùng 1 dòng, dùng `end`
4. Tính tổng tiền từ đơn hàng, in kết quả bằng f-string, kiểm tra `type()` của tổng tiền
