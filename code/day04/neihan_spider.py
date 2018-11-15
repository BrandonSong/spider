import requests
import re


class NeiHanSpider(object):
    """内涵段子爬虫"""
    def __init__(self):
        self.start_url = "https://www.qiushibaike.com/"
        self.headers = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 70.0.3538.102Safari / 537.36"
        }

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def parse_content(self, html_str):
        content_list = re.findall(r"<div class=\"content\">.*?<span>(.*?)</span>", html_str, re.S)
        return content_list

    def run(self):
        # 1.发送请求获取数据
        html_str = self.parse_url(self.start_url)
        # 2.解析数据
        content_list = self.parse_content(html_str)
        # 3.保存数据
        for item in content_list:
            print(item)


if __name__ == '__main__':
    neihan = NeiHanSpider()
    neihan.run()

