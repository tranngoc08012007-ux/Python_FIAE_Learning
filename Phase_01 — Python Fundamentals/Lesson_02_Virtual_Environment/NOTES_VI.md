# GIÁO ÁN — BUỔI 2: Virtual Environment (venv) & pip

**Giai đoạn:** 1 — Python Cơ Bản & Môi Trường Phát Triển Chuyên Nghiệp
**Buổi:** 2 / 34
**Môi trường:** Python 3.14, VS Code, Windows (PowerShell)
**Ngày học:** _______________

---

## I. MỤC TIÊU BUỔI HỌC

Sau buổi học này, có thể:
- Tạo và kích hoạt được virtual environment (venv)
- Hiểu rõ venv cô lập cái gì, phạm vi áp dụng tới đâu
- Cài đặt thư viện bằng `pip`
- Tạo và phân biệt `requirements.txt` vs `requirements-dev.txt`
- Tự xử lý được lỗi PowerShell chặn script

---

## II. KHÁI NIỆM CỐT LÕI

### 1. Virtual Environment (venv) là gì?

> **venv = một "căn phòng ảo"** chứa Python + thư viện riêng cho từng project, tách biệt khỏi Python toàn cục (global) của máy.

**Vì sao cần venv?**
- Tránh xung đột version giữa các project (project A cần Flask 2.0, project B cần Flask 3.0)
- Giữ Python global của máy sạch, không bị "rác hóa"
- Là quy trình chuẩn bắt buộc trong môi trường làm việc thực tế (đặc biệt ở Đức)

**venv KHÔNG tạo bản Python mới** — nó chỉ trỏ về cùng một Python gốc đã cài trên máy. Vì vậy `python --version` trong và ngoài venv thường ra **cùng một số version**. Cái khác nhau thực sự là **đường dẫn** (`where python`) và **nơi chứa thư viện cài bằng pip**.

**Phạm vi cô lập của venv:**
- venv KHÔNG tự "biết" cấu trúc thư mục
- venv chỉ quan tâm: *terminal hiện tại đang activate venv nào*
- Nếu chỉ có 1 venv ở thư mục gốc → nó áp dụng cho TOÀN BỘ project bên dưới
- Muốn cô lập riêng từng project con (vd: Capstone_Project_01 dùng Flask, Capstone_Project_02 dùng Django) → phải **tạo venv riêng bên trong từng thư mục đó**

---

### 2. pip là gì?

> **pip** = công cụ cài đặt thư viện Python, tải từ **PyPI** (Python Package Index — kho lưu trữ thư viện công khai tại pypi.org).

**Điều kiện để `pip install <tên>` chạy đúng:**
- Cần kết nối internet
- Tên thư viện phải chính xác tuyệt đối
- Nên kích hoạt venv trước, nếu không thư viện sẽ bị cài vào Python global thay vì venv

**Khi cài 1 thư viện, pip tự động cài kèm "sub-dependency"** (thư viện phụ thuộc) — ví dụ cài `pytest` sẽ tự kéo theo `colorama`, `pluggy`, `iniconfig`, `packaging`, `Pygments`.

---

### 3. requirements.txt & requirements-dev.txt

> Là file văn bản liệt kê **tên + version chính xác** của thư viện cần cài, để bất kỳ ai (hoặc chính mình ở máy khác) tái tạo lại đúng môi trường chỉ bằng 1 lệnh.

| File | Chứa gì | Khi nào dùng |
|---|---|---|
| `requirements.txt` | Thư viện THẬT cần để app chạy (vd: `requests`, `flask`) | Luôn cần khi deploy/chia sẻ project |
| `requirements-dev.txt` | Công cụ chỉ DEV cần lúc code/test (vd: `pytest`, `black`) | Không cần khi chạy production |

**Lưu ý:** chỉ ghi thư viện **chính** mình chủ động cài — KHÔNG cần ghi thủ công các sub-dependency tự động kéo theo (pip sẽ tự cài lại khi chạy `pip install -r requirements.txt`).

**`requirements.txt` ≠ `main.py`/`README.md`:**
- `requirements.txt` → máy đọc (pip), chỉ chứa `tên==version`
- `README.md` → người đọc, dùng để giải thích phạm vi/ngữ cảnh của venv

---

## III. CHEAT SHEET — CÁC LỆNH QUAN TRỌNG

```powershell
# === TẠO & KÍCH HOẠT VENV ===
python -m venv myenv              # Tạo venv tên "myenv"
myenv\Scripts\activate            # Kích hoạt (Windows)
deactivate                        # Thoát khỏi venv

# === KIỂM TRA ===
python --version                  # Xem version Python đang dùng
where python                      # Xem ĐƯỜNG DẪN Python đang dùng (venv hay global)

# === CÀI ĐẶT THƯ VIỆN ===
pip install <tên_thư_viện>        # Cài thư viện (bản mới nhất)
pip install <tên>==<version>      # Cài đúng 1 version cụ thể

# === REQUIREMENTS ===
pip freeze                        # Xem TẤT CẢ thư viện đang có trong venv
pip freeze > requirements.txt     # Xuất toàn bộ ra file (cách nhanh, không phân loại)
pip install -r requirements.txt   # Cài lại tất cả thư viện liệt kê trong file
```

**Cấu trúc cú pháp (phần nào cố định, phần nào thay đổi):**

| Lệnh | Phần CỐ ĐỊNH | Phần THAY ĐỔI |
|---|---|---|
| `python -m venv myenv` | `python -m venv` | `myenv` (tên tự đặt) |
| `myenv\Scripts\activate` | `\Scripts\activate` | `myenv` (phải khớp tên đã tạo) |
| `pip install pandas` | `pip install` | `pandas` (tên thư viện) |

---

## IV. QUY TRÌNH CHUẨN (LÀM TỪNG BƯỚC)

1. `cd` vào thư mục project
2. `python -m venv myenv` — tạo venv
3. `myenv\Scripts\activate` — kích hoạt
4. `pip install <thư_viện_cần>` — cài thư viện
5. `pip freeze` — kiểm tra danh sách đã cài
6. Tạo `requirements.txt` — chỉ ghi thư viện THẬT
7. Tạo `requirements-dev.txt` — chỉ ghi công cụ DEV
8. Đặt 2 file này **ngang hàng với venv** mà chúng mô tả

---

## V. LỖI ĐÃ GẶP & CÁCH XỬ LÝ (rút từ buổi học)

| Lỗi | Nguyên nhân | Cách sửa |
|---|---|---|
| `PSSecurityException` khi `activate` | PowerShell mặc định chặn chạy file `.ps1` | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` rồi gõ `Y` |
| File tạo ra tên `requirements.txt.txt` | Gõ thêm `.txt` trong khi VS Code đã tự thêm sẵn | Chuột phải file → Rename (F2) → sửa lại đúng tên |
| Nội dung gõ nhầm vào `Untitled-1.txt` | Gõ trực tiếp vào tab chưa lưu, chưa đặt tên | Copy nội dung dán sang file đã tạo đúng tên, xóa file Untitled thừa |
| Tưởng venv cô lập riêng cho 1 file `.py` | Nhầm lẫn phạm vi áp dụng của venv | venv áp dụng theo **terminal đang activate**, không theo từng file |

---

## VI. CÂU HỎI TỰ KIỂM TRA (ôn lại cuối buổi)

1. Vì sao `python --version` trong và ngoài venv thường ra cùng kết quả?
2. `myenv` có phải là một thư viện không? Nếu không thì nó là gì?
3. Vì sao không nên đẩy thư mục venv lên GitHub?
4. `requirements.txt` và `requirements-dev.txt` khác nhau ở điểm nào?
5. Nếu có 2 project cần 2 version khác nhau của cùng 1 thư viện, nên làm gì?

---

## VII. GHI NHỚ QUAN TRỌNG

> 🔑 **venv cô lập THƯ VIỆN, không cô lập Python interpreter.**
> 🔑 **Mỗi project có dependency riêng → nên có venv riêng.**
> 🔑 **requirements.txt = máy đọc. README.md = người đọc.**
> 🔑 **Không bao giờ push thư mục venv lên GitHub — chỉ push `requirements.txt`.**