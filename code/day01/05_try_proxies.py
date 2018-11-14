import requests


proxies = {
    "http": "http://117.191.11.77"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}


ret = requests.get("http://www.baidu.com", proxies=proxies, headers=headers)

print(ret.status_code)
