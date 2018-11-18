# __author__: liqinsong
# data: 2018/11/18
import requests
from lxml import etree


class QiuBaiSpider:
    def __init__(self):

        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
        }

    def get_url_list(self):
        return [self.url_temp.format(i) for i in range(1, 14)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers = self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@id='content-left']/div")

        content_list = []

        for div in div_list:
            item = dict()
            author_name = div.xpath(".//div[@class='author clearfix']//h2/text()")
            author_name = author_name[0] if len(author_name) > 0 else None

            author_age = div.xpath(".//div[contains(@class, 'articleGender')]/text()")
            author_age = author_age[0] if len(author_age) > 0 else None

            author_gender = div.xpath(".//div[contains(@class, 'articleGender')]/@class")
            author_gender = author_gender[0].split(" ")[-1].replace("Icon", "") if len(author_gender) > 0 else None

            content = div.xpath(".//div[@class='content']/span/text()")

            stats = div.xpath(".//div[@class='stats']/span[1]/i/text()")
            stats = stats[0] if len(stats) > 0 else 0

            commenter_name = div.xpath(".//a[@class='indexGodCmt']/div/span[2]/text()")
            commenter_name = commenter_name[0] if len(commenter_name)> 0 else None

            commenter_content = div.xpath(".//a[@class='indexGodCmt']/div/div/text()")
            commenter_content = commenter_content[0] if len(commenter_content) > 0 else None

            item["author_name"] = author_name
            item["author_age"] = author_age
            item["author_gender"] = author_gender
            item["content"] = content
            item["stats"] = stats
            item["commenter_name"] = commenter_name
            item["commenter_content"] = commenter_content

            content_list.append(item)

        return content_list

    def save_content(self, content):
        print("over")

    def run(self):
        """实现主要逻辑"""
        # 1.构造url列表
        url_list = self.get_url_list()

        # 2.遍历url列表 发送请求 获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.提取数据
            content_list = self.get_content_list(html_str)
            # 4.保存数据
            self.save_content(content_list)


if __name__ == '__main__':
    qiubai = QiuBaiSpider()
    qiubai.run()
