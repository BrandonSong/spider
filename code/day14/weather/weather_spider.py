# __author__: liqinsong
# data: 2018/12/17
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

class WeatherSpider(object):
    def __init__(self):
        self.url = "http://www.weather.com.cn/textFC/hb.shtml"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    def get_html_page(self, url):
        response = requests.get(url, self.headers)
        return response.content.decode()

    def parse_provice(self, html_str):
        """ 获取页面中所有省份 """
        provice_list = list()

        soup = BeautifulSoup(html_str, "lxml")
        prov_div = soup.find('div', class_='lqcontentBoxheader')
        ul_list = prov_div.find_all('ul')
        for ul in ul_list:
            aList = ul.find_all('a')
            for a in aList:
                href = a['href']
                provice_list.append(href)
        return provice_list

    def parse_city_weather(self, html_str):
        """解析页面中某个城市的最低气温"""
        item = dict()
        soup = BeautifulSoup(html_str, 'lxml')
        div_list = soup.find_all('div', class_='conMidtab3')
        for div in div_list:
            trs = div.find_all("tr")

            for tr in trs:
                city = trs[0].find("td", class_ = 'rowsPan').string
                tds = tr.find_all("td")
                a = tds[0].find("a")
                if a is None:
                    xian = city
                else:
                    xian = a.string
                temp = tds[-2].string

                item["city"] = city
                item["xian"] = xian
                item["temp"] = temp
                print(item)
        return None

    def run(self):
        """实现爬虫的主要逻辑"""
        # 1.获取所有省份的url地址
        html_str = self.get_html_page(self.url)
        provice_list = self.parse_provice(html_str)

        for provice in provice_list:
            # 2.根据发送的请求 获取每个城市的数据
            provice_url = "http://www.weather.com.cn" + provice
            provice_str = self.get_html_page(provice_url)
            # 3.解析页面中每个市县的最低气温
            min_temp = self.parse_city_weather(provice_str)
            # 保存数据

if __name__ == '__main__':
    weather = WeatherSpider()
    weather.run()