# ChatGPT-Share-Web [演示站点](https://web.planetzero.cn)

欢迎来到我们基于ChatGPT-Share开发的商业版镜像站的部署仓库。本项目旨在提供完全代理ChatGPT官网，包含完整的用户系统，对接官方ChatGPT网站的全部功能，集成无缝支付系统，以及管理员后台面板，实现全面的站点管理。

## 特别鸣谢

本项目的用户聊天系统基于xyhelper的[ChatGPT-Share-Server](https://github.com/xyhelper/chatgpt-share-server)，感谢xyhelper提供的免费接入点！

## 功能特点

- **完整的用户系统**：图形验证码、邮箱、手机号注册、登录、忘记密码及管理个人资料。
- **1:1的官网UI**：跟随官网更新的UI系统，提供与官网一模一样的体验感。
- **全面的ChatGPT功能接入**：直接从我们的平台访问ChatGPT的所有特性：3.5, 4.0, 插件，联网，画图，高级分析等全部官网功能。
- **账号池机制**：以账号池为基石，用户随意切换流动于所有开放的账户，用最高效的运营模式，确保最大化收益。
- **支付系统集成**：填入相关服务参数即可实时收款、购买积分或服务。
- **管理员后台**：从集中的面板管理用户、创建营销活动、查看分析数据和控制站点设置。
  
## 用户前台展示

### 简洁高效的注册登录页面

- **登录页面**

  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/9785df93-050b-43ae-8b63-b70507f3515f" width="640">

- **注册页面**

  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/58fd2eb7-2297-42f1-a917-892345c0e004" width="640">

- **重置密码**

  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/c82fdd69-678b-4f31-bae2-7b266e4dad5d" width="640">

### 正版体验

- **深浅主题切换**

  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/554a97c4-813d-41f8-aab9-625287156818" width="640">
  
  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/6471267a-aa36-4a6e-a805-f2d31bf196c1" width="640">
- **语言切换**

  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/99bc4722-aa18-4cb5-9146-95d860ac0e03" width="640">

### 更多界面展示

- **插件系统**

  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/9be33c1e-833e-4cc3-ade6-30eafe31e8d3" width="640">

- **个人中心**

  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/537f6bf8-d7cb-49f7-a182-fcbde8be13a0" width="320">

- **可弹出公告**

  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/8d8742d6-5dca-431a-8a7e-882a1dafa62d" width="640">

- **套餐选择**

  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/0ca61af0-9e0e-452b-853c-d583bfc275f2" width="640">

- **支付界面**

  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/a7841868-c98a-4f99-9fd8-5b235e1e79e9" width="640">

- **手机端界面展示**

  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/1f38f52f-c883-4cd7-ad7c-3e302a475e32" width="320">

## 管理员面板

### 仪表盘

简洁高效的界面，方便分析销售和运营数据。

<img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/155861ac-dddf-4fdf-bd2e-7630b5cc7c20" width="640">

### 用户管理

创建、修改、删除或封禁用户。

<img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/aa3bec4d-3814-4802-881a-8438397be81d" width="640">

### 商品管理

实时更新商品信息，随意定制价格及时长。

<img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/acb5d9d6-223c-4026-85c5-9fbb96373d88" width="640">

### 订单管理

查看所有订单信息，便于对账。

<img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/63320fe8-ca00-420b-8976-bad218be1982" width="640">

### 配置中心

模块化管理：基础配置、邮箱配置、运营配置、支付配置、公告配置。

<img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/63cfef41-cb5e-4493-9fca-f268566e4df0" width="640">

## 前提条件

- **操作系统**：支持 Ubuntu, CentOS（其他系统暂未测试）
- **Docker**

## 安装

1. 克隆此部署库:
   
   ```bash
   git clone https://github.com/realnoob007/ChatGPT-Share-Web.git
   ```

2. 进入ChatGPT-Share-Web文件夹

   ```bash
   cd ChatGPT-Share-Web
   ```
3. 将授权文件放在 ChatGPT-Share-Web 文件夹中

4. 填写config.py与config.yaml中的内容

5. 请提前配置好反代，确保域名能够正常访问，数据库需要能够访问share来初始化管理员
   
6. 运行deploy.sh
   
  ```bash
  sudo chmod +x deploy.sh
  ./deploy.sh
  ```

7. 查看初始管理员账号密码: （若能查看到管理员账号和密码，说明已部署成功）
   
  ```bash
  docker compose logs web
  ```

 ### 8. 成功部署后，请务必将docker-compose.yml中的web环境变量中的FIRST_RUN改为False

<img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/37624778/7c66da07-6d60-4b73-8747-65e661930a31" width="320">

### 此步骤尤为重要，否则可能导致后续更新项目时，重建数据库，导致数据丢失。请确保完成该步骤！否则后续数据丢失无法恢复！切记！！！


## 定价

v1.0.0 版本目前的定价为 ￥400/年。随着版本更新和功能的增加，价格可能会进行相应的调整。

## 联系方式

想了解商业版授权，或有任何关于这个项目的问题？欢迎联系我们！

- **微信**: lebronajams101

  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/87698941/cd942031-ddff-4a9c-8444-5867207b585c" width="320">
- **微信**: Csg1271932463

  <img src="https://github.com/realnoob007/ChatGPT-Share-Web/assets/37624778/8423d852-239d-4e09-a093-9359f3a7f7c5" width="320">

我们期待与您的联系，共同探讨合作机会。



