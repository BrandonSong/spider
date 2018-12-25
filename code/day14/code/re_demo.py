# __author__: liqinsong
# data: 2018/12/18
import re

# 1.匹配某个字符串 局限只会从开头进行匹配
# text = "hello"
# ret = re.match("he", text)
# print(ret.group())

# 2 .匹配任意字符

# 3. \d匹配任意的数字(0-9)

# 4. \D匹配任意的非数字

# 5. \s 匹配空白字符(\n \t \r 空格)

# 6. \w 匹配的是a-z A-Z 数字和下划线

# *可以匹配0或多个字符
# +可以匹配1个或者多个字符
# ?可以匹配1个或者0个 要么没有 要么就只有一个
# {m} 匹配m个字符
# {m, n} 匹配m-n个字符

# ****** 案例 ******
# 1.验证手机号码
# phone = "18578900987"
# phone_regex = "1[34578]\d{9}"
# ret = re.match(phone_regex, phone)
# print(ret.group())

# 2.验证邮箱
# email_text = "1437050555@qq.com"
# email_regex = "[A-Za-z0-9]+@[A-Za-z0-9]+\.[com|cn]"
# ret1 = re.match(email_regex, email_text)
# print(ret1.group())

# 3.验证URL
# text = "http://www.baidu.com"
# ret = re.match("(http|https|ftp])://[^\s]+", text)
# print(ret.group())

# 4.验证身份证
# text = ""
# ret = re.match("[\d]{17}[\dxX]", text)
# print(ret.group())

text = "99"
ret = re.match("[1-9]\d?$|100$", text)
print(ret.group())
