import requests


response = requests.get("http://a.xnimg.cn/nx/apps/login/cssimg/logo-big.jpg")

with open("a.jpg", 'wb') as f:
    f.write(response.content)
