# Giáo án Lesson 08: Cấu trúc điều khiển (Control Flow)

## 1. Thông tin chung

| Mục | Nội dung |
|-----|----------|
| Chủ đề | `if` / `elif` / `else`, toán tử so sánh, toán tử logic, biểu thức ternary |
| Thời lượng đề xuất | 90–120 phút (học + làm bài tập) |
| Kiến thức nền | Lesson 06: biến, kiểu dữ liệu, ép kiểu, `input()`, `print()` |
| Tài liệu đi kèm | `main.py` (bài học), `exercises.md` (đề bài), `solutions.py` (lời giải) |

## 2. Mục tiêu bài học

Sau bài học, người học có thể:
- Giải thích toán tử so sánh trả về giá trị `bool` như thế nào.
- Viết chương trình rẽ nhánh bằng `if` / `elif` / `else`.
- Kết hợp nhiều điều kiện bằng `and`, `or`, `not` và hiểu thứ tự ưu tiên của chúng.
- Rút gọn một `if / else` đơn giản thành biểu thức ternary.
- Xử lý dữ liệu nhập từ người dùng bằng các điều kiện (kèm ép kiểu).

## 3. Phân bổ thời gian

| Phần | Nội dung | Thời gian |
|------|----------|-----------|
| 1 | Toán tử so sánh | 10 phút |
| 2 | `if` / `elif` / `else` | 20 phút |
| 3 | Toán tử logic, short-circuit, truthy/falsy | 25 phút |
| 4 | Biểu thức ternary | 10 phút |
| 5 | `input()` kết hợp điều kiện | 10 phút |
| 6 | Bài tập (`exercises.md`) | 30–45 phút |

## 4. Nội dung chi tiết

### 4.1. Toán tử so sánh

Toán tử so sánh luôn trả về `True` hoặc `False`.

| Toán tử | Ý nghĩa | Ví dụ | Kết quả |
|---------|---------|-------|---------|
| `==` | Bằng | `10 == 3` | `False` |
| `!=` | Khác | `10 != 3` | `True` |
| `>` | Lớn hơn | `10 > 3` | `True` |
| `<` | Nhỏ hơn | `10 < 3` | `False` |
| `>=` | Lớn hơn hoặc bằng | `10 >= 10` | `True` |
| `<=` | Nhỏ hơn hoặc bằng | `3 <= 2` | `False` |

Điểm cần nhớ:
- `=` là **gán** giá trị, `==` là **so sánh** hai giá trị.
- Python cho phép so sánh nối tiếp, giống cách viết trong toán học:

```python
age = 18
print(18 <= age < 65)  # True
```

- Chuỗi được so sánh từng ký tự và phân biệt chữ hoa, chữ thường: `"apple" == "Apple"` là `False`.

### 4.2. `if` / `elif` / `else`

Cú pháp:

```python
if condition_1:
    ...  # runs if condition_1 is True
elif condition_2:
    ...  # runs if condition_1 is False and condition_2 is True
else:
    ...  # runs if none of the conditions above is True
```

Quy tắc quan trọng:
- Cuối dòng điều kiện **bắt buộc** có dấu `:`.
- Khối lệnh của mỗi nhánh được xác định bằng **thụt lề** (4 dấu cách).
- Python kiểm tra từ trên xuống dưới và **chỉ chạy nhánh đúng đầu tiên**, các nhánh còn lại bị bỏ qua.
- `elif` và `else` là tùy chọn.
- Có thể đặt `if` bên trong `if` (nested if), nhưng nên hạn chế lồng quá sâu vì khó đọc.

Ví dụ xếp loại điểm:

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)  # C
```

### 4.3. Toán tử logic: `and`, `or`, `not`

| Toán tử | Ý nghĩa |
|---------|---------|
| `and` | Đúng khi **cả hai** vế đều đúng |
| `or` | Đúng khi **ít nhất một** vế đúng |
| `not` | Đảo ngược giá trị (`True` thành `False` và ngược lại) |

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

**Short-circuit (đoản mạch):**
- `A and B`: nếu `A` sai thì `B` **không được tính**.
- `A or B`: nếu `A` đúng thì `B` **không được tính**.
- Ứng dụng: tránh lỗi chia cho 0.

```python
divisor = 0
if divisor != 0 and 10 / divisor > 1:
    print("Result is greater than 1.")
else:
    print("Safe: 10 / divisor was never evaluated.")
```

**Truthy và falsy:** trong điều kiện, Python tự chuyển mọi giá trị sang `bool`.
- Giá trị falsy (xem như `False`): `0`, `0.0`, `""`, `[]`, `None`.
- Mọi giá trị còn lại là truthy.

```python
shopping_list = []
if shopping_list:
    print("The list has items.")
else:
    print("The list is empty.")  # runs, because [] is falsy
```

### 4.4. Biểu thức ternary

Cú pháp: `value_if_true if condition else value_if_false`

```python
# Long version
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Short version, same result
status = "adult" if age >= 18 else "minor"
```

Khi nào dùng:
- Dùng cho lựa chọn **đơn giản** giữa hai giá trị, nhất là khi cần gán giá trị hoặc đặt trong f-string.
- Nếu logic cần nhiều dòng hoặc nhiều nhánh, hãy dùng `if / elif / else` thông thường.
- Tránh ternary lồng nhau vì rất khó đọc.

### 4.5. `input()` kết hợp điều kiện

`input()` luôn trả về chuỗi (`str`), nên phải ép kiểu trước khi so sánh số:

```python
user_score = int(input("Enter your score (0-100): "))

if user_score < 0 or user_score > 100:
    print("Invalid score. Please enter a number between 0 and 100.")
elif user_score >= 50:
    print("Result: Passed")
else:
    print("Result: Failed")
```

## 5. Lỗi thường gặp

| Lỗi | Nguyên nhân | Cách sửa |
|-----|-------------|----------|
| `SyntaxError` | Quên dấu `:` sau `if`, `elif`, `else` | Thêm `:` cuối dòng |
| `IndentationError` | Thụt lề sai hoặc thiếu | Dùng 4 dấu cách, nhất quán trong cả khối |
| Nhầm `=` với `==` | Gán thay vì so sánh | Dùng `==` để so sánh |
| `x == 1 or 2` luôn đúng | `2` là truthy nên vế phải luôn đúng | Viết `x == 1 or x == 2` |
| `TypeError` khi so sánh `input()` với số | Chưa ép kiểu từ `str` sang `int` | Dùng `int(input(...))` |
| Dùng nhiều `if` thay vì `elif` | Các `if` đều được kiểm tra, kết quả bị ghi đè | Dùng `elif` khi các nhánh loại trừ nhau |
| Sắp xếp `elif` sai thứ tự | Nhánh rộng đứng trước nhánh hẹp | Kiểm tra điều kiện hẹp (ví dụ `>= 90`) trước |
| `ValueError` khi người dùng nhập chữ | `int("abc")` không hợp lệ | Sẽ học cách xử lý ở bài về xử lý lỗi |

Ví dụ về lỗi dùng nhiều `if`:

```python
score = 95

# Wrong: every if is checked, so the last matching one wins
if score >= 90:
    grade = "A"
if score >= 60:
    grade = "D"

print(grade)  # D (unexpected)
```

## 6. Tóm tắt nhanh

- Toán tử so sánh trả về `bool`: `==`, `!=`, `>`, `<`, `>=`, `<=`.
- `if / elif / else` chạy **đúng một nhánh**, kiểm tra từ trên xuống.
- `and`, `or`, `not` kết hợp điều kiện. Thứ tự ưu tiên: `not` → `and` → `or`.
- Short-circuit giúp tránh lỗi và tránh tính toán không cần thiết.
- Giá trị falsy: `0`, `0.0`, `""`, `[]`, `None`.
- Ternary: `a if condition else b`, chỉ dùng cho lựa chọn đơn giản.
- `input()` luôn trả về `str`, cần ép kiểu trước khi so sánh số.

## 7. Bài tập

Làm 7 bài trong `exercises.md` theo thứ tự, tự giải trước khi đối chiếu với `solutions.py`:

| Bài | Nội dung | Kiến thức chính |
|-----|----------|-----------------|
| 1 | Dương, âm hay bằng 0 | `if / elif / else` |
| 2 | Chẵn hoặc lẻ | Ternary |
| 3 | Năm nhuận | `and`, `or` |
| 4 | Xếp loại điểm | `elif`, kiểm tra dữ liệu không hợp lệ |
| 5 | Số lớn nhất trong ba số | So sánh, `and` |
| 6 | Kiểm tra tam giác | Nhiều điều kiện kết hợp |
| 7 | Giá vé | Điều kiện lồng nhau, ternary, `and` |

## 8. Câu hỏi tự kiểm tra

1. Kết quả của `True or False and False` là gì?
2. `bool("")` và `bool([0])` lần lượt trả về gì?
3. Vì sao `if divisor != 0 and 10 / divisor > 1:` không gây lỗi khi `divisor = 0`?
4. Viết lại bằng ternary: nếu `n` chia hết cho 2 thì `result = "even"`, ngược lại `result = "odd"`.
5. `5 > 3 > 1` và `5 > 3 > 4` cho kết quả gì?
6. Vì sao `if age >= 18 or 65:` luôn đúng, và cách viết đúng là gì?

**Đáp án:**
1. `True` (vì `and` được tính trước `or`).
2. `False` và `True` (chuỗi rỗng là falsy, list có phần tử là truthy dù phần tử là `0`).
3. Vì `divisor != 0` sai nên vế phải không được tính (short-circuit).
4. `result = "even" if n % 2 == 0 else "odd"`
5. `True` và `False`.
6. Vì `65` là truthy nên vế phải luôn đúng. Cách viết đúng tùy ý định, ví dụ `age >= 18 or age == 65` hoặc `age >= 18 and age <= 65`.
