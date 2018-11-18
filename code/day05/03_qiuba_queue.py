# __author__: liqinsong
# data: 2018/11/18
import requests
from lxml import etree
from queue import Queue
from threading import Thread


class QiuBaiSpider:
    def __init__(self):

        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
        }
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        for i in range(1, 14):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers = self.headers).content.decode()
            self.html_queue.put(response)
            self.url_queue.task_done()  # get和task_done一起使用才能使队列中元素个数减1

    def get_content_list(self):
        while True:
            html_str = self.html_queue.get()
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

            self.content_queue.put(content_list)
            self.html_queue.task_done()

    def save_content(self, content):
        while True:
            content = self.content_queue.get()
            for i in content:
                pass
            self.content_queue.task_done()

    def run(self):
        """实现主要逻辑"""
        thread_list = []
        # 1.构造url列表
        t_url = Thread(target = self.get_url_list)
        thread_list.append(t_url)
        # 2.遍历url列表 发送请求 获取响应
        t_parse = Thread(target = self.parse_url)
        thread_list.append(t_parse)

        # 3.提取数据
        t_content = Thread(target = self.get_content_list)
        thread_list.append(t_content)
        # 4.保存数据
        t_save = Thread(target = self.save_content)
        thread_list.append(t_save)

        for i in thread_list:
            i.setDaemon(True) # 设置子进程为守护线程,改线程不重要,主线程结束,子线程结束
            i.start()

        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()

if __name__ == '__main__':
    qiubai = QiuBaiSpider()
    qiubai.run()
