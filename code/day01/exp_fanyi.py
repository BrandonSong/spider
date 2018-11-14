import requests
import json


class BaiduFanyi(object):
    def __init__(self, trans_content):
        self.trans_content = trans_content
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.tans_url = "https://fanyi.baidu.com/basetrans"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36"
        }

    def parse_url(self, url, query_data):
        """发送请求 获取响应"""
        response = requests.post(url, data=query_data, headers=self.headers)
        return response.content.decode()

    def parse_data(self, response):
        """将返回数据转换为json格式数据"""
        json_data = json.loads(response)
        return json_data

    def run(self):
        """程序启动"""
        # 1.获取转换类型
        lan_data = {
            "query": self.trans_content
        }
        lan_response = self.parse_url(self.lang_detect_url, lan_data)
        json_data = self.parse_data(lan_response)
        lan_type = json_data["lan"]

        # 2.发送翻译数据
        tans_data = {
            "query": self.trans_content,
            "from": lan_type,
            "to": "en"
        }
        # 3.获取返回数据
        tans_response = self.parse_url(self.tans_url, tans_data)
        tans_json_data = self.parse_data(tans_response)
        print(tans_json_data["trans"][0]["dst"])


if __name__ == '__main__':
    baidufanyi = BaiduFanyi("今天风很大")
    baidufanyi.run()
