# apple-order-checker

## Description
新买的MacBook Pro 2021迟迟没有发货，之前每天一有时间就会手动登到苹果官网上看一下。      
这两天写了个脚本，每五分钟帮我检查一下订单有没有更新，有的话就通过Push+推送消息到我的微信。      
虽然并不会缩短等待的时间，但是至少可以让我在等待的时候更安心些，因为你知道一有新消息他就会第一时间推送给你。


## How To Use
* 安装并配置Python环境
* 安装并配置Selenium环境
* 安装requests依赖
* 注册Push+(微信消息推送需要，详情可参考[Push+](https://pushplus.hxtrip.com/))
* 根据实际情况更新配置文件conf.ini
* 运行脚本apple_order_checker.py
* 首次登录需在命令行提示后，在浏览器中输入二次认证验证码，并勾选信任当前浏览器，完成后按回车

### P.S 2021.11.18 我的MBP已经发货了，祝大家心仪的装备也能尽快到来。
