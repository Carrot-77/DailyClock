# DailyClock 

## 功能
自动打卡，可以同时为多人打卡；
当打卡失败时会给打卡失败的人发邮箱提示今天打卡失败了；
打卡完成后会在日志里记录今天打卡成功的人。
如果想删除邮箱功能，可以在Clock.py里删除邮箱部分

## 准备环境

1. chrome
2. chromedriver
3. python3.6及以上
4. 为云主机开放一个端口发送邮箱

> 记得把Clock.py和SendMail.py里的绝对路径改成自己的路径


## 创建一个文件目录data
里面包含两个json文件
`data.json` 打卡账号和密码邮箱
`mail.json` 发邮件的邮箱账号和授权码

data.josn格式
data.json里一个字典就是一个打卡账号
```
[
    {
        "user": "Student Number",
        "passwd": "password",
        "email": "email"
    }, 
    {
        "user": "...",
        "passwd": "..."
        "email": "..."
    },
    ...
]
```

mail.json格式
我使用的QQ邮箱，如果使用其他记得在SendMail.py里更改邮箱服务器
```
[
    {
        "email": "YourEmail",
        "passwd": "你的邮箱授权码"
    }
]
```
