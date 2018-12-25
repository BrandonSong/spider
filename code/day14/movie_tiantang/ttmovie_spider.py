# __author__: liqinsong
# data: 2018/12/13
import requests
from lxml import etree
from urllib.parse import urljoin
import re

class TTMovie(object):

    start_url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
    }

    def custom_request(self,url):
        """自己封装的发送url请求的方法"""
        if not url.startswith("http"):
            url = urljoin("http://www.ygdy8.net/html/gndy/dyzz/", url)
        print(url)
        resp = requests.get(url, headers=self.headers)
        html = etree.HTML(resp.content.decode("gbk"))
        return html

    def parse_movie_list(self, html):
        """解析电影列表页"""
        # 当前页面的电影的url
        table_list = html.xpath("//table[@class='tbspan']//a/@href")
        # 下一页的url地址
        next_url = html.xpath("//a[text()='下一页']/@href")
        # 判断下一页url是否存在
        next_url = next_url[0] if len(next_url) > 0 else None
        return table_list, next_url

    def parse_movie_detail(self, html):
        """解析详情页数据"""
        item = dict()
        title = html.xpath("//div[@id='Zoom']/td//text()")
        title = [re.sub(r"[\u3000|\r|\n|, |        |\xa0]", "", i) for i in title]

        title = [ i for i in title if len(i) > 0]
        item["title"] = title
        return item

    def save_movie_info(self, movie_info):
        """保存数据"""
        print(movie_info)

    def run(self):
        html = self.custom_request(self.start_url)
        moive_list, next_url = self.parse_movie_list(html)
        for movie in moive_list:
            movie_html = self.custom_request(movie)
            movie_info = self.parse_movie_detail(movie_html)
            self.save_movie_info(movie_info)

        if next_url is not None:
            html = self.custom_request(next_url)
            moive_list, next_url = self.parse_movie_list(html)
            for movie in moive_list:
                movie_html = self.custom_request(movie)
                movie_info = self.parse_movie_detail(movie_html)
                self.save_movie_info(movie_info)


if __name__ == '__main__':
    tt = TTMovie()
    tt.run()