# __author__: liqinsong
# data: 2018/12/9
from urllib import parse

url = "http://www.baidu.com/s?wd=python&username=abc#1"

ret1 = parse.urlparse(url)
ret2 = parse.urlsplit(url)

print(ret1)
print(ret2)
