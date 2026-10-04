# Bài 5: Git nâng cao: Branch and Pull Request

## 1. Khái niệm cốt lõi: Branch là gì?
* Hãy tưởng tượng project của bạn là một cuốn sách đang viết, khi đó:
  * `main` = bản gốc của cuốn sách, luôn phải sạch và hoàn chỉnh.
  * `branch` = bản photo - bạn viết thử trên đó.
* $\rightarrow$ Nếu hay: gộp vào bản gốc (`merge`).
* Nếu tệ: xé bỏ, bản gốc vẫn y nguyên.

* **Quy tắc vàng:**
  * `main`: luôn phải chạy được, luôn phải clean.
  * Mọi tính năng mới $\rightarrow$ làm trên branch riêng.
  * Chỉ `merge` vào `main` khi đã `review` và `approve`.

---

## 2. Các lệnh git branch cơ bản

### 2.1. Xem và tạo branch
* `git branch` # xem đang ở branch nào (dấu `*` chỉ branch hiện tại, ví dụ: `* main`)
* `git switch -c feat/tên-tính-năng` # tạo branch mới và chuyển ngay sang đó
  * Git cũ: `git checkout -b feat/tên-tính-năng`
* `git switch main` # chuyển về branch main
  * Git cũ: `git checkout main`

### 2.2. Đổi tên branch
* `git branch -m tên-mới`

### 2.3. Cập nhật branch main trước khi tạo branch mới
* `git switch main` # chuyển về branch main
* `git pull origin main` # lấy phiên bản mới nhất từ GitHub

### 2.4. Push branch lên GitHub lần đầu
* `git push --set-upstream origin tên-branch`

### 2.5. Merge branch vào main (ít dùng trong doanh nghiệp)
* `git switch main` # chuyển về branch main
* `git merge feat/tên-tính-năng` # gộp branch vào main
> **Lưu ý:** Trong doanh nghiệp, thường merge thông qua **Pull Request** trên GitHub/GitLab thay vì dùng lệnh này.

### 2.6. Xóa branch sau khi xong
* `git branch -d feat/tên-tính-năng` # xóa branch trên máy
* `git push origin --delete feat/tên-tính-năng` # xóa branch trên GitHub
---

## 3. Pull Request = lời đề nghị: *"Tôi muốn merge branch của tôi vào main - ai review giúp tôi không?"*

* **Trong môi trường Betrieb thực tế tại Đức:**
  1. Developer tạo branch $\rightarrow$ làm việc $\rightarrow$ push lên Github.
  2. Developer mở Pull Request.
  3. Senior developer đọc code, comment yêu cầu sửa nếu cần.
  4. Sau khi `approve` $\rightarrow$ `merge` vào `main`.
* $\rightarrow$ PR tạo ra lịch sử rõ ràng: ai làm gì, khi nào, tại sao.

### 3.1. Tạo Pull Request trên Github
* **b1:** 
  * Vào Github
  * Bấm vào thông báo màu vàng
* **b2:** Điền thông tin:
  * `title`: `feat: add lesson 05 branch demo`
  * `Description`: mô tả ngắn bằng tiếng Anh những gì sẽ làm
* **b3:** Bấm *"Create pull request"*
* **b4:** Bấm *"Merge pull request"* $\rightarrow$ code vào `main`.
* *Đóng mà không merge:* bấm *"Close pull request"* $\rightarrow$ `main` không bị ảnh hưởng.

---

## 4. Toàn bộ workflow chuyên nghiệp
* **Branch Workflow - thứ tự đúng:**
  `main` $\rightarrow$ tạo `branch` $\rightarrow$ làm việc $\rightarrow$ `commit` $\rightarrow$ `push` $\rightarrow$ `Pull Request` $\rightarrow$ `review` $\rightarrow$ `merge` (hoặc `close`) $\rightarrow$ xóa `branch`

---

## 5. Lý do quan trọng
* `main` phải luôn chạy được - một commit lỗi trực tiếp = hệ thống `production` sập.
* Branch cho phép nhiều người làm việc song song mà không xung đột.
* Pull Request = cơ chế kiểm soát chất lượng trước khi code vào `main`.
* IHK kiểm tra kỹ năng này trong kì thi.
* Mọi Betrieb ở Đức đều áp dụng workflow này hàng ngày.

---

## 6. Ghi nhớ quan trọng
* Không bao giờ `commit` thẳng vào `main`.
* Không bao giờ sửa file trực tiếp trên Github.
* Luôn luôn: tạo `branch` $\rightarrow$ làm việc `local` $\rightarrow$ `push` $\rightarrow$ `PR`.
* Branch đã `merge` xong $\rightarrow$ xóa đi cho gọn.