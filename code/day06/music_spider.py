import requests
from lxml import etree


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

    def parse_detail(self, sheet_detail_content):
        html_str = etree.HTML(sheet_detail_content)
        song_name_list = html_str.xpath("//ul[@class='f-hide']/li/a/text()")
        return song_name_list

    def run(self):
        # 1.通过start_url获取歌单页面
        content = self.parse_url(self.start_url)
        # 2.解析页面获取分类
        category = self.get_cat(content)

        # 3.1 获取分类下歌单列表
        for top_category, second_category_list in category.items():
            for second_category in second_category_list:
                next_page_url = ""
                # 如果有下一页,就继续获取下一页
                while next_page_url is not None:
                    sheet_content = self.parse_url(self.sheet_part_url.format(second_category))
                    sheet_url_list, next_page_url = self.get_songsheet(sheet_content)
                    for sheet_url in sheet_url_list:
                        sheet_detail_content = self.parse_url(self.detail_part_url + sheet_url)
                    # # 3.2 获取每个歌单明细
                        song_name_list = self.parse_detail(sheet_detail_content)
                    # # 3.3 保存数据
                        print(song_name_list)


if __name__ == '__main__':
    wy = WyMusicSpider()
    wy.run()
