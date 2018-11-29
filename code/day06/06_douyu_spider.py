# __author__: liqinsong
# data: 2018/11/21
from selenium import webdriver
import time


class DouyuSpider:
    """ 爬取斗鱼所有房间的主播名和人气值"""
    def __init__(self):
        # self.driver = webdriver.PhantomJS(r"D:\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe")
        self.driver = webdriver.Chrome()
        self.strat_url = "https://www.douyu.com/directory/all"

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@id='live-list-contentbox']/li")

        content_list = []
        for li in li_list:
            item = {}
            item["img_url"] = li.find_element_by_xpath(".//span[@class='imgbox']/img").get_attribute("src")
            item["room_title"] = li.find_element_by_xpath("./a").get_attribute("title")
            item["room_cate"] = li.find_element_by_xpath(".//div[@class='mes-tit']/span").text
            item["anchor_name"] = li.find_element_by_xpath(".//p/span[1]").text
            item["room_stars"] = li.find_element_by_xpath(".//p/span[2]").text

            print(item)
            content_list.append(item)
        # 获取下一页的元素
        next_url = self.driver.find_element_by_xpath("//a[@class='shark-pager-next']")
        next_url = next_url[0] if next_url > 0 else None
        return content_list, next_url

    def save_content_list(self, content_list):
        pass

    def run(self):
        # 1.start_url
        #  2.获取页面元素
        self.driver.get(self.strat_url)

        # 3.提取数据,提取下一页的元素
        content_list, next_url = self.get_content_list()

        # 4.保存数据
        self.save_content_list(content_list)
        # 点击下一页元素
        while next_url is not None:
            next_url.click()
            time.sleep(3)
            content_list, next_url = self.get_content_list()
            self.save_content_list(content_list)


if __name__ == '__main__':
    douyu = DouyuSpider()
    douyu.run()
