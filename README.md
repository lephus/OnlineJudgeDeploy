Live site: https://luyencode.net/

Phiên bản cải tiến (tùy chỉnh + thêm tiếng Việt), dựa trên mã nguồn mở [QDOJ](https://github.com/QingdaoU/OnlineJudge), nhánh clone của tác giả [Harry-zklcdc](https://github.com/Harry-zklcdc/OnlineJudge)

### Kiến trúc

Hệ thống Online Judge này bao gồm 3 module:
- Judger: https://github.com/luyencode/Judger ([Python wrapper](https://github.com/luyencode/JudgeServer))
- Web Backend: https://github.com/luyencode/OnlineJudge
- Web Frontend: https://github.com/luyencode/OnlineJudgeFE

Các module trên đều được đóng gói Docker và đã đẩy lên Docker Hub. Trong trường hợp cần thiết, bạn có thể sửa từng thành phần!

### Cài đặt trên máy Linux

1. Cài đặt môi trường

    ```bash
    sudo apt-get update && sudo apt-get install -y vim python-pip curl git
    pip install docker-compose
    ```

2. Cài Docker 

   ```bash
   sudo curl -sSL get.docker.com | sh
   ```


3. Clone repo

    ```bash
    git clone -b 2.0 https://github.com/luyencode/OnlineJudgeDeploy.git && cd OnlineJudgeDeploy
    ```

4. Khởi động

    ```bash
    docker-compose up -d
    ```

    > Nếu bạn không dùng user `root`，hãy sử dụng `sudo -E docker-compose up -d`.

Quá trình cài đặt có thể tốn từ 5 đến 30 phút phụ thuộc vào tốc độ mạng!

Sau đó, hãy kiểm tra bằng lệnh `docker ps -a`，nếu không có container nào ở trạng thái `unhealthy` hoặc `Exited (x) xxx` thì là ok rồi đó.

## Sử dụng


Truy cập cổng HTTP 80 hoặc cổng HTTPS 443 của máy chủ thông qua trình duyệt và bạn có thể bắt đầu sử dụng. Đường dẫn trang quản lý là `/admin`, tên người dùng quản trị viên được tự động thêm vào trong quá trình cài đặt là `root` và mật khẩu là `rootroot`. **Vui lòng thay đổi mật khẩu ngay**.

Tài liệu: http://opensource.qduoj.com/

## Tùy chỉnh giao diện
sửa đổi giao diện người dùng
Tham khảo https://github.com/QingdaoU/OnlineJudgefe để phát triển và xây dựng

Sau đó, npm run buildbạn có thể nhận được một thư mục dist, cấu trúc tệp như sau

➜  OnlineJudgeFE git:(master) ✗ tree dist
dist
├── admin
│   └── index.html
├── index.html
└── static
    ├── css
    │   ├── admin.127f3da5b09451926728de2829ebb32e.css
    │   ├── loader.css
    │   ├── oj.0ba722f43ddbeb758cde2f9dc804455e.css
    │   └── vendor.f033d6c4c74b6b40e92ca86f168fd0be.css
    ├── fonts
    │   ├── KaTeX_AMS-Regular.3d8245d.woff2
    │   ├── KaTeX_AMS-Regular.ac1d46d.woff

....
....
### Linux
```
npm install
# we use webpack DllReference to decrease the build time,
# this command only needs execute once unless you upgrade the package in build/webpack.dll.conf.js
export NODE_ENV=development 
npm run build:dll

# the dev-server will set proxy table to your backend
export TARGET=http://Your-backend

# serve with hot reload at localhost:8080
npm run dev
```
### Windows
```
npm install
# we use webpack DllReference to decrease the build time,
# this command only needs execute once unless you upgrade the package in build/webpack.dll.conf.js
set NODE_ENV=development 
npm run build:dll

# the dev-server will set proxy table to your backend
set TARGET=http://Your-backend

# serve with hot reload at localhost:8080
npm run dev
```
- Sau khi tùy chỉnh FE, Run
```
npm run buil
```
- Sau đó build lại docker với lệnh
```
docker-compose up -d
```

distVí dụ, sao chép thư mục vào một thư mục nhất định trên máy chủ, /data/OnlineJudgeDeploy/data/backend/distsau đó sửa đổi nó, thêm một dòng docker-compose.ymlvào trong oj-backendmô-đun (vui lòng thay đổi dòng trước dấu hai chấm thành .volumes- /data/OnlineJudgeDeploy/data/backend/dist:/app/distdocker-compose up -d

Lưu ý rằng phương pháp sửa đổi này sẽ ghi đè lên tệp giao diện người dùng trong vùng chứa. Khi phiên bản mới của giao diện người dùng được phát hành trong tương lai, vui lòng sử dụng phương pháp tương tự để tự cập nhật phiên bản đó.

Video giới thiệu: https://www.bilibili.com/video/av37051523/
