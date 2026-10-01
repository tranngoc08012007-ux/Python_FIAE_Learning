# Bài 4: Git cơ bản

## I. Git là gì và tại sao lại cần nó?

-   Git là một **hệ thống quản lý phiên bản (Version Control System)**
    giúp theo dõi toàn bộ lịch sử thay đổi của dự án. Mỗi lần developer
    lưu một "checkpoint" (gọi là **commit**), Git sẽ ghi lại: ai thay
    đổi, thay đổi gì và khi nào thay đổi. Nếu code bị lỗi hoặc muốn quay
    lại phiên bản trước, Git có thể khôi phục rất dễ dàng.
-   Git hoạt động hoàn toàn trên máy tính của bạn. **GitHub** chỉ là nơi
    lưu trữ Git repository trên cloud để backup, chia sẻ với người khác
    và làm việc nhóm.
-   **Luồng cơ bản:** `Folder trên máy` → `git add` → `git commit` →
    `git push` → `GitHub`
-   **Tại sao quan trọng?** Hầu hết các công ty phát triển phần mềm đều
    sử dụng Git để quản lý mã nguồn. Trong quá trình làm việc nhóm, mọi
    thay đổi đều được lưu bằng Git. Một GitHub có lịch sử commit rõ ràng
    cũng giúp nhà tuyển dụng đánh giá quá trình học tập và làm việc của
    ứng viên.

## II. Git hoạt động như thế nào?

``` text
Working Directory
        │
     git add
        │
   Staging Area
        │
   git commit
        │
 Git Repository
```

-   **Working Directory:** nơi bạn đang chỉnh sửa code.
-   **Staging Area:** vùng chờ, nơi bạn chọn những thay đổi sẽ được lưu
    trong commit tiếp theo.
-   **Git Repository:** nơi Git lưu toàn bộ lịch sử commit của dự án.

Có thể hiểu đơn giản: - Working Directory = bàn làm việc. - Staging Area
= giỏ đồ chuẩn bị gửi. - Repository = kho lưu trữ lâu dài.

## III. Các lệnh Git cơ bản

### 1. `git init`

-   Dùng để khởi tạo Git cho một project và tạo thư mục ẩn `.git/`.
-   Thư mục `.git/` chứa toàn bộ lịch sử của dự án.
-   Chỉ dùng một lần khi bắt đầu dự án.

### 2. `git status`

-   Kiểm tra trạng thái hiện tại của project.
-   Cho biết file mới, file đã sửa, file đã được thêm vào Staging Area
    và còn gì cần commit.

### 3. `git add`

-   Đưa file vào **Staging Area**.
-   Chưa lưu lịch sử, chỉ đánh dấu file sẽ được commit.

Ví dụ:

``` bash
git add main.py
git add main.py README.md
git add .
```

### 4. `git commit`

-   Lưu một phiên bản của project vào lịch sử Git.

Ví dụ:

``` bash
git commit -m "feat: create login interface"
```

### 5. `git log`

-   Xem lịch sử commit.

``` bash
git log
git log --oneline
```

### 6. `git diff`

-   Xem chính xác những dòng code đã thay đổi.
-   `-` là dòng bị xóa.
-   `+` là dòng được thêm.

``` diff
- print("Hello World!")
+ print("Hello.")
```

-   `git diff`: so sánh Working Directory với Staging Area.
-   `git diff --staged`: so sánh Staging Area với commit gần nhất.

### 7. `git restore`

-   Khôi phục những thay đổi **chưa commit**.

``` bash
git restore main.py
```

> Lưu ý: Chỉ dùng cho các thay đổi chưa commit.

### 8. `git rm`

-   Xóa file khỏi máy và đồng thời đánh dấu việc xóa để chuẩn bị commit.

``` bash
git rm test.py
git commit -m "chore: remove test file"
```

-   Nếu chỉ muốn Git ngừng theo dõi file nhưng vẫn giữ file trên máy:

``` bash
git rm --cached .env
```

### 9. `git clone`

-   Tải một Git repository từ GitHub về máy.

``` bash
git clone https://github.com/user/project.git
```

> Sau khi clone **không cần** chạy `git init`.

### 10. `git push`

-   Đưa commit từ máy lên GitHub.

``` bash
git push origin main
```

### 11. `git pull`

-   Lấy thay đổi mới nhất từ GitHub về máy.

``` bash
git pull origin main
```

## IV. `.gitignore`

-   `.gitignore` là danh sách các file/thư mục Git sẽ bỏ qua.

Ví dụ:

``` gitignore
.venv/
__pycache__/
*.pyc
.env
.vscode/
```

## V. Commit Message Convention

  Type         Dùng khi nào
  ------------ --------------------
  `feat`       Thêm tính năng
  `fix`        Sửa lỗi
  `docs`       Sửa tài liệu
  `style`      Chỉ sửa format
  `refactor`   Viết lại code
  `test`       Thêm hoặc sửa test
  `chore`      Bảo trì

### Quy tắc

-   Viết bằng tiếng Anh.
-   Viết ngắn gọn.
-   Một commit chỉ nên có một mục đích.

Ví dụ:

``` text
feat: add login page
fix: correct password validation
docs: update lesson 4
style: format code with black
chore: remove unused files
```

## VI. Quy trình làm việc cơ bản với Git

``` text
Chỉnh sửa file
      │
git status
      │
git diff
      │
git add
      │
git status
      │
git commit
      │
git log
      │
git push
      │
GitHub
```
