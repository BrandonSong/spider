# __author__: liqinsong
# data: 2018/12/9

from urllib import request
from urllib import parse
#
# resp = request.urlopen("http://www.baidu.com")
#
# print(resp.read())

# request.urlretrieve("http://www.baidu.com", "baidu.html")

# url编码

params = {
    "name": "张三",
    "age": 18,
    "greet": "hello world",
}

result = parse.urlencode(params)
print(result)