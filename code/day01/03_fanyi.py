import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}

data = {
    "from": "en",
    "to": "zh",
    "query": "hola",
    "transtype": "translang",
    "simple_means_flag": "3",
    "sign": "822331.552714",
    "token": "e9cc2ab861db1d53baa92ee6e9344263"
}

post_url = "https://fanyi.baidu.com/v2transapi"

response = requests.post(post_url, data=data, headers=headers)

print(response.content.decode())
