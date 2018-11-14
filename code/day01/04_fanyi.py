import requests
import json


headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36"
}

post_data = {
    "query": "人生苦短, 我用Python",
    "from": "zh",
    "to": "en"
}

post_url = "https://fanyi.baidu.com/basetrans"

response = requests.post(post_url, data=post_data, headers=headers)

html_str = response.content.decode()

dict_ret = json.loads(html_str)

ret = dict_ret["trans"][0]["dst"]

print("result is:", ret)
