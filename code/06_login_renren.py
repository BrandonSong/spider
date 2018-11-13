import requests


session = requests.session()
# http://www.renren.com/ajaxLogin/login
post_url = "http://www.renren.com/PLogin.do"

post_data = {
    "email": "mr_mao_hacker@163.com",
    "password": "alarmchime"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}

# 使用session发送post请求, cookie保存在其中
session.post(post_url, data=post_data, headers=headers)

# 使用session访问登录才能访问的地址
ret = session.get("http://www.renren.com/327550029/profile", headers=headers)

print(ret)
