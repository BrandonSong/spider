# __author__: liqinsong
# data: 2018/12/9

from urllib import request

url = "https://www.lagou.com/shanghai-zhaopin/?utm_source=m_cf_cpt_baidu_pc1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
}

# 构造一个带请求头的请求
req = request.Request(url, headers = headers)

# 发送请求 获取结果
rep = request.urlopen(req)

print(rep.read())

