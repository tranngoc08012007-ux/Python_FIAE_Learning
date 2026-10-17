# Giáo án Lesson 09: Cấu trúc điều khiển (Control Flow)

## 1. Thông tin chung

| Mục | Nội dung |
|-----|----------|
| Chủ đề | `if` / `elif` / `else`, toán tử logic, toán tử so sánh, biểu thức ternary |
| Thời lượng đề xuất | 90–120 phút (học + làm bài tập) |
| Kiến thức nền | Lesson 06: biến, kiểu dữ liệu, ép kiểu, `input()`, `print()` và f-string |
| Tài liệu đi kèm | `main.py` (bài học), `exercises.md` (đề bài), `solutions.py` (lời giải) |

## 2. Mục tiêu bài học

Sau bài học, người học có thể:
- Giải thích cách chương trình ra quyết định dựa trên điều kiện `True` hoặc `False`.
- Viết chương trình rẽ nhánh bằng `if` / `elif` / `else`.
- Kết hợp nhiều điều kiện bằng `and`, `or`, `not` và hiểu thứ tự ưu tiên của chúng.
- Dùng đúng các toán tử so sánh, kể cả với chuỗi và số thực.
- Rút gọn một `if / else` đơn giản thành biểu thức ternary.
- Xử lý dữ liệu nhập từ người dùng bằng các điều kiện (kèm ép kiểu).

## 3. Phân bổ thời gian

| Phần | Nội dung | Thời gian |
|------|----------|-----------|
| 1 | `if` / `elif` / `else` | 20 phút |
| 2 | Toán tử logic, short-circuit, truthy/falsy | 20 phút |
| 3 | Toán tử so sánh | 15 phút |
| 4 | Biểu thức ternary | 10 phút |
| 5 | Bài tổng hợp: máy tính giảm giá | 10 phút |
| 6 | Bài tập (`exercises.md`) | 30–45 phút |

## 4. Nội dung chi tiết

### 4.1. `if` / `elif` / `else`

Cú pháp:

```python
if condition_1:
    ...  # runs if condition_1 is True
elif condition_2:
    ...  # runs if condition_1 is False and condition_2 is True
else:
    ...  # runs if none of the conditions above is True
```

Các dạng thường gặp:
- **`if`:** chỉ chạy khối lệnh khi điều kiện đúng.
- **`if / else`:** chọn một trong hai khối lệnh.
- **`if / elif / else`:** chọn một trong nhiều khối lệnh.
- **`if` lồng nhau (nested if):** đặt `if` bên trong `if`, nên hạn chế lồng quá sâu.

Quy tắc quan trọng:
- Cuối dòng điều kiện **bắt buộc** có dấu `:`.
- Khối lệnh của mỗi nhánh được xác định bằng **thụt lề** (4 dấu cách).
- Python kiểm tra từ trên xuống dưới và **chỉ chạy nhánh đúng đầu tiên**, các nhánh còn lại bị bỏ qua.
- `elif` và `else` là tùy chọn.

Ví dụ đèn giao thông:

```python
light = "yellow"
if light == "green":
    print("Go.")
elif light == "yellow":
    print("Slow down.")  # Runs, because light == "yellow"
elif light == "red":
    print("Stop.")
else:
    print("Invalid light color.")
```

Kết hợp với `input()`: `input()` luôn trả về chuỗi, nên phải ép kiểu trước khi so sánh số:

```python
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("The number is zero.")
```

### 4.2. Toán tử logic: `and`, `or`, `not`

| Toán tử | Ý nghĩa | Ví dụ |
|---------|---------|-------|
| `and` | Đúng khi **cả hai** vế đều đúng | `age >= 18 and has_id` |
| `or` | Đúng khi **ít nhất một** vế đúng | `day == "Sat" or day == "Sun"` |
| `not` | Đảo ngược giá trị | `not is_raining` |

Bảng chân trị:

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

**Thứ tự ưu tiên:** toán tử so sánh → `not` → `and` → `or`. Khi không chắc, hãy dùng dấu ngoặc để thể hiện rõ ý định:

```python
print(True or False and False)    # True
print((True or False) and False)  # False
```

**Lỗi kinh điển `x == 1 or 2`:**
- Python hiểu đây là `(x == 1) or 2`.
- Vì `2` là truthy nên biểu thức luôn cho kết quả đúng.
- Cách viết đúng: `x == 1 or x == 2`.

**Short-circuit (đoản mạch):**
- `A and B`: nếu `A` sai thì `B` **không được tính**.
- `A or B`: nếu `A` đúng thì `B` **không được tính**.
- Ứng dụng: tránh lỗi khi vế phải chỉ an toàn nếu vế trái đúng.

```python
name = ""
if name and name[0] == "N":  # name[0] would raise IndexError on ""
    print("The name starts with N.")
else:
    print("The name is empty or does not start with N.")  # Runs, no error
```

**Truthy và falsy:** trong điều kiện, Python tự chuyển mọi giá trị sang `bool`.
- Giá trị falsy (xem như `False`): `False`, `None`, `0`, `0.0`, `""`, `[]`.
- Mọi giá trị còn lại là truthy.

### 4.3. Toán tử so sánh

Toán tử so sánh luôn trả về `True` hoặc `False`.

| Toán tử | Ý nghĩa | Ví dụ (`x = 7`, `y = 12`) | Kết quả |
|---------|---------|---------------------------|---------|
| `==` | Bằng | `x == y` | `False` |
| `!=` | Khác | `x != y` | `True` |
| `>` | Lớn hơn | `x > y` | `False` |
| `<` | Nhỏ hơn | `x < y` | `True` |
| `>=` | Lớn hơn hoặc bằng | `x >= 7` | `True` |
| `<=` | Nhỏ hơn hoặc bằng | `y <= 10` | `False` |

Điểm cần nhớ:
- `=` là **gán** giá trị, `==` là **so sánh** hai giá trị.
- **So sánh nối tiếp** giống cách viết trong toán học:

```python
month = 10
print(1 <= month <= 12)  # True
```

- Khác kiểu dữ liệu: `5 == 5.0` là `True` (int và float có thể bằng nhau), nhưng `'5' == 5` là `False` (chuỗi khác số).
- Chuỗi được so sánh từng ký tự và phân biệt chữ hoa, chữ thường: `'apple' == 'Apple'` là `False`, `'apple' < 'banana'` là `True`.
- **Số thực:** tránh dùng `==` vì sai số làm tròn:

```python
print(0.1 + 0.2 == 0.3)                # False
print(round(0.1 + 0.2, 2) == 0.3)      # True
```

### 4.4. Biểu thức ternary

Cú pháp: `value_if_true if condition else value_if_false`

```python
score = 72

# Long version (4 lines)
if score >= 50:
    result = "Passed"
else:
    result = "Failed"

# Short version (1 line), same result
result = "Passed" if score >= 50 else "Failed"
```

Một số cách dùng:
- Đặt trong f-string: `f"You have {count} {'item' if count == 1 else 'items'}."`
- Chọn giá trị mặc định: `display_name = nickname if nickname else "Guest"`

Khi nào dùng:
- Dùng cho lựa chọn **đơn giản** giữa hai giá trị.
- Ternary lồng nhau (`"A" if score >= 90 else "B" if score >= 80 else "C"`) chạy được nhưng rất khó đọc, nên dùng `if / elif / else` thông thường.

### 4.5. Bài tổng hợp: máy tính giảm giá

Quy tắc giảm giá trong `main.py`:

| Điều kiện | Giảm giá |
|-----------|----------|
| Thành viên và giá từ 100 | 20% |
| Thành viên, giá dưới 100 | 10% |
| Không phải thành viên, giá từ 200 | 5% |
| Còn lại | 0% |

Bài này kết hợp `input()` và ép kiểu, `and`, `elif`, `if` lồng nhau và định dạng số thực bằng f-string (`:.2f`). Thứ tự các nhánh rất quan trọng: nhánh `is_member and shop_price >= 100` phải đứng trước nhánh `is_member`, nếu không mọi thành viên sẽ chỉ được giảm 10%.

## 5. Lỗi thường gặp

| Lỗi | Nguyên nhân | Cách sửa |
|-----|-------------|----------|
| `SyntaxError` | Quên dấu `:` sau `if`, `elif`, `else` | Thêm `:` cuối dòng |
| `IndentationError` | Thụt lề sai hoặc thiếu | Dùng 4 dấu cách, nhất quán trong cả khối |
| Nhầm `=` với `==` | Gán thay vì so sánh | Dùng `==` để so sánh |
| `x == 1 or 2` luôn đúng | `2` là truthy | Viết `x == 1 or x == 2` |
| `TypeError` khi so sánh `input()` với số | Chưa ép kiểu từ `str` sang `int` | Dùng `int(input(...))` |
| `IndexError` với chuỗi rỗng | Truy cập `name[0]` khi `name == ""` | Kiểm tra `name and ...` trước |
| So sánh số thực bằng `==` | Sai số làm tròn | Dùng `round()` trước khi so sánh |
| Dùng nhiều `if` thay vì `elif` | Các `if` đều được kiểm tra, kết quả bị ghi đè | Dùng `elif` khi các nhánh loại trừ nhau |
| Sắp xếp `elif` sai thứ tự | Nhánh rộng đứng trước nhánh hẹp | Kiểm tra điều kiện hẹp (ví dụ `>= 90`) trước |
| `ValueError` khi người dùng nhập chữ | `int("abc")` không hợp lệ | Sẽ học cách xử lý ở bài về xử lý lỗi |

Ví dụ về lỗi sắp xếp `elif` sai thứ tự:

```python
score = 95

# Wrong: the broad condition comes first, so the others never run
if score >= 60:
    grade = "D"
elif score >= 90:
    grade = "A"

print(grade)  # D (unexpected)
```

## 6. Tóm tắt nhanh

- `if / elif / else` chạy **đúng một nhánh**, kiểm tra từ trên xuống.
- `and`, `or`, `not` kết hợp điều kiện. Thứ tự ưu tiên: so sánh → `not` → `and` → `or`.
- Short-circuit giúp tránh lỗi và tránh tính toán không cần thiết.
- Giá trị falsy: `False`, `None`, `0`, `0.0`, `""`, `[]`.
- Toán tử so sánh trả về `bool`: `==`, `!=`, `>`, `<`, `>=`, `<=`. Có thể so sánh nối tiếp, và nên tránh dùng `==` với số thực.
- Ternary: `a if condition else b`, chỉ dùng cho lựa chọn đơn giản.
- `input()` luôn trả về `str`, cần ép kiểu trước khi so sánh số.

## 7. Bài tập

Làm 7 bài trong `exercises.md` theo thứ tự, tự giải trước khi đối chiếu với `solutions.py`:

| Bài | Nội dung | Kiến thức chính |
|-----|----------|-----------------|
| 1 | Phân loại độ tuổi | `if / elif / else` |
| 2 | Kiểm tra đăng nhập | `and` |
| 3 | Cửa hàng mở hay đóng | So sánh nối tiếp, `not` |
| 4 | Xác định mùa theo tháng | `or`, `elif` |
| 5 | Dạng số ít, số nhiều | Ternary |
| 6 | Kéo, búa, bao | Nhiều điều kiện kết hợp |
| 7 | Phí vận chuyển | `elif`, điều kiện lồng nhau |

## 8. Câu hỏi tự kiểm tra

1. Kết quả của `True or False and False` là gì?
2. Vì sao `if x == 1 or 2:` luôn đúng, và cách viết đúng là gì?
3. Vì sao `if name and name[0] == "N":` không gây lỗi khi `name = ""`?
4. `0.1 + 0.2 == 0.3` cho kết quả gì, và nên so sánh như thế nào cho đúng?
5. `5 == 5.0` và `'5' == 5` lần lượt cho kết quả gì?
6. Viết lại bằng ternary: nếu `count == 1` thì `word = "item"`, ngược lại `word = "items"`.
7. Với `score = 95`, vì sao đặt `elif score >= 60` trước `elif score >= 90` là sai?

**Đáp án:**
1. `True` (vì `and` được tính trước `or`).
2. Python hiểu là `(x == 1) or 2`, mà `2` là truthy nên luôn đúng. Cách viết đúng: `x == 1 or x == 2`.
3. Vì `name` là chuỗi rỗng (falsy) nên vế trái sai và vế phải `name[0]` không được tính (short-circuit).
4. `False` do sai số làm tròn. Nên viết `round(0.1 + 0.2, 2) == 0.3`.
5. `True` và `False`.
6. `word = "item" if count == 1 else "items"`
7. Vì `95 >= 60` đúng nên Python chạy nhánh đó và bỏ qua các nhánh còn lại, kết quả sẽ là `"D"` thay vì `"A"`. Phải kiểm tra điều kiện hẹp hơn (`>= 90`) trước.
