# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import json
import urllib


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com', 'p.3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath("//div[@class='mc']/dl/dt") # 大分类列表

        for dt in dt_list:
            item = dict()

            item["b_cate"] = dt.xpath("./a/text()").extract_first()
            # xpath获取下一个兄弟节点 使用follow-sibling::标签名[index]
            em_list = dt.xpath("./following-sibling::dd[1]/em")

            # 小分类列表循环
            for em in em_list:
                item["s_herf"] = em.xpath("./a/@href").extract_first()
                item["s_cate"] = em.xpath("./a/text()").extract_first()

                if item["s_herf"] is not None:
                    url = "https:" + item["s_herf"]
                    yield scrapy.Request(url, callback = self.extract_book_list, meta = {"item": deepcopy(item)})
                    break

    def extract_book_list(self, response):
        """提取每个小分类下的图书的url地址"""
        item = response.meta["item"]

        li_list = response.xpath("//div[@id='plist']/ul/li")

        for li in li_list:
            item["book_img"] = li.xpath(".//div[@class='p-img']//img/@src").extract_first()
            if item["book_img"] is None:
                item["book_img"] = li.xpath(".//div[@class='p-img']//img/@data-lazy-img").extract_first()
            item["book_name"] = li.xpath(".//div[@class='p-name']/a/em/text()").extract_first().strip()
            item["book_author"] = li.xpath(".//span[@class='author_type_1']/a/text()").extract()
            item["book_press"] = li.xpath(".//span[@class='p-bi-store']/a/@title").extract_first()
            item["book_publish_date"] = li.xpath(".//span[@class='p-bi-date']/text()").extract_first().strip()
            item["book_sku"] = li.xpath(".//div/@data-sku").extract_first()
            yield scrapy.Request(
                "https://p.3.cn/prices/mgets?skuIds=J_{}".format(item["book_sku"]),
                callback = self.parse_book_price,
                meta = {"item": deepcopy(item)}
            )

        next_url = response.xpath("//a[@class='pn-next']/@href").extract_first()
        if next_url is not None:
            # 此处的url地址并为在初始的domain中包含  需要添加至domain中 否则爬虫无法抓取此url地址
            next_url = urllib.parse.urljoin(response.url, next_url)
            yield scrapy.Request(
                next_url,
                callback = self.extract_book_list,
                meta = {"item": deepcopy(item)}
            )

    def parse_book_price(self, response):
        """获取图书的价格"""
        item = response.meta["item"]
        item["book_price"] = json.loads(response.body.decode())[0].get("op")
        print(item)

