# __author__: liqinsong
# data: 2018/11/18
import requests
import re
from lxml import etree


class BiBiSpider(object):
    def __init__(self, url):
        self.start_url = url
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile"}
        self.danmu_url = "https://comment.bilibili.com/{}.xml"

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_cid_list(self, html_str):
        cid_list = re.findall("\"cid\":(\d+),", html_str)
        return set(cid_list)

    def parse_content_list(self, content):
        xml = etree.HTML(content.encode())
        d_list = xml.xpath("//d")

        danmu_list = []

        for d in d_list:
            item = dict()
            item["content"] = d.xpath(".//text()")[0]
            danmu_list.append(item)
        return danmu_list

    def run(self):
        """实现主要逻辑"""
        # 发送请求
        html_str = self.parse_url(self.start_url)
        # 通过正则表达式 从请求中获取cid获取cid
        cid_list = set(self.get_cid_list(html_str))
        # 发送弹幕请求
        for cid in cid_list:
            content_list = self.parse_url(self.danmu_url.format(cid))
            # 获取弹弹幕数据
            danmu_list = self.parse_content_list(content_list)
            # 保存数据
            print(danmu_list)


if __name__ == '__main__':
    start_url = "https://m.bilibili.com/bangumi/play/ep35266"
    bibi = BiBiSpider(start_url)
    bibi.run()
