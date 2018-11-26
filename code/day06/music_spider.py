import requests
from lxml import etree
from selenium import webdriver
import time


class WyMusicSpider:
    """网易云音乐下的所有歌单和歌单详细"""
    def __init__(self):
        self.start_url = "https://music.163.com/discover/playlist"
        self.sheet_part_url = "https://music.163.com/discover/playlist/?cat={}"
        self.detail_part_url = "https://music.163.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
            "Referer": "https://music.163.com/",
        }
        self.driver = webdriver.PhantomJS()

    def parse_url(self, url):
        print(url)
        content = requests.get(url, headers=self.headers).content
        return content

    def get_cat(self, content):
        """获取每个大分类和小分类"""
        html_str = etree.HTML(content)
        dl_list = html_str.xpath("//dl[@class='f-cb']")
        category = dict()

        for dl in dl_list:
            top_category = dl.xpath("./dt/text()")[0]
            second_category = dl.xpath("./dd/a/text()")
            category[top_category] = second_category
        return category

    def get_songsheet(self, sheet_content):
        html_str = etree.HTML(sheet_content)
        div_list = html_str.xpath("//div[@class='u-cover u-cover-1']")

        sheet_url_list = list()

        for div in div_list:
            sheet_url = div.xpath(".//a[@class='msk']/@href")[0]
            sheet_url_list.append(sheet_url)

        next_page_url = html_str.xpath("//a[@class='zbtn znxt']/@href")[0] if len(html_str.xpath("//a[@class='zbtn znxt']/@href")) > 0 else None
        return sheet_url_list, next_page_url

    def get_detail_content(self, url):
        """使用selenium获取到歌单页面内容"""
        print(url)
        self.driver.get(url)
        self.driver.switch_to.frame("contentFrame")

        time.sleep(10)

        detail_content = self.driver.page_source
        return detail_content

    def parse_detail(self, detail_content, item):
        """解析歌单页面内容 提取数据"""
        print("开始解析歌单数据")
        song_list = list()

        html_str = etree.HTML(detail_content)
        item["sheet_name"] = html_str.xpath("//div[@class='cnt']//h2/text()")[0]
        item["sheet_author"] = html_str.xpath("//div[@class='user f-cb']/span[@class='name']/a/text()")[0]
        create_date = html_str.xpath("//div[@class='user f-cb']/span[@class='time s-fc4']/text()")[0]
        item["create_date"] = "".join(create_date.encode("utf-8").decode().split()).replace("创建", "")

        tr_list = html_str.xpath("//table/tbody/tr")
        for tr in tr_list:
            song_info = dict()
            song_info["song_name"] = tr.xpath("./td[2]//span[@class='txt']/a/b/@title")[0]
            song_info["song_time"] = tr.xpath("./td[@class=' s-fc3']/span/text()")[0]
            song_info["singer_name"] = tr.xpath("./td[4]/div/span/@title")[0]
            album_name = tr.xpath("./td[5]/div/a/@title")[0]
            song_info["album_name"] = "".join(album_name.split())

            song_list.append(song_info)

        item["song_info"] = song_list
        return item

    def save_data(self, item):
        print(item)

    def run(self):
        # 1.通过start_url获取歌单页面
        content = self.parse_url(self.start_url)
        # 2.解析页面获取分类
        category = self.get_cat(content)

        # 3.1 获取分类下歌单列表
        for top_category, second_category_list in category.items():
            for second_category in second_category_list:
                item = dict()
                item["top_category"] = top_category
                item["second_category"] = second_category

                # 获取每个分类下的第一页数据
                sheet_content = self.parse_url(self.sheet_part_url.format(second_category))
                sheet_url_list, next_page_url = self.get_songsheet(sheet_content)
                for sheet_url in sheet_url_list:
                    # 3.1 获取歌单详情页面
                    detail_content = self.get_detail_content(self.detail_part_url + sheet_url)
                    # 3.2解析歌单页面
                    item = self.parse_detail(detail_content, item)
                    # 3.3 保存数据
                    self.save_data(item)

                next_page_url = ""
                # 如果有下一页,就继续获取下一页
                while next_page_url is not None:
                    next_page = self.parse_url(next_page_url)
                    sheet_url_list, next_page_url = self.get_songsheet(next_page)
                    for sheet_url in sheet_url_list:
                        # 3.1 获取歌单详情页面
                        detail_content = self.get_detail_content(self.detail_part_url + sheet_url)
                        # 3.2解析歌单页面
                        item = self.parse_detail(detail_content, item)
                        # 3.3 保存数据
                        self.save_data(item)


if __name__ == '__main__':
    wy = WyMusicSpider()
    wy.run()
