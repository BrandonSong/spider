# __author__: liqinsong
# data: 2018/12/11

from urllib import request


url = "http://httpbin.org/ip"
# 构建一个代理对象实例
handler = request.ProxyHandler({"http": "111.11.98.58:9000"})

# 使用handler来创建一个opener
opener = request.build_opener(handler)

# 构建一个请求对象
resq = opener.open(url)

print(resq.read())


