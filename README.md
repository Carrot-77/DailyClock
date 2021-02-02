# DailyClock 

## 准备环境

1. chrome
2. chromedriver
3. python3.6及以上

## 文件目录data

`data.json` 打卡账号和密码邮箱
`mail.json` 发邮件的邮箱账号和授权码

data.josn格式
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
```
[
    {
        "email": "YourEmail",
        "passwd": "你的邮箱授权码"
    }
]
```
