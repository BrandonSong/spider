# -*- coding: utf-8 -*-
import scrapy
from suning.items import SuningItem


class SnSpider(scrapy.Spider):
    name = 'sn'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        # 获取分类名和分类的url
        ul_list = response.xpath("//ul[@class='book-name-list clearfix']")
        for ul in ul_list:
            item = SuningItem()
            item["category"] = ul.xpath("./li/a/text()")
            category_url = ul.xpath("./li/a/@href")

            yield scrapy.Request(category_url, callback=self.parse_book_list, meta={"item": item})

    def parse_book_list(self, response):
        item = response.meta["item"]

        # 获取当前页的书籍
        li_list = response.xpath("//ul[@class='clearfix']/li")
        for li in li_list:
            book_part_url = li.xpath(".//div[@class='img-block']/a/@href")
            book_url = "https:" + book_part_url
            yield scrapy.Request(book_url, callback=self.parse_book_detail, meta={"item": item})

        # 1.获取下一页url
        # 2.如果下一页url存在,发送请求
        # 3.如果不存在则不发送

    def parse_book_detail(self, response):
        item = response.meta["item"]

        book_name = response.xpath("//h1[@id='itemDisplayName']").extract_first()
        book_author = response.xpath().extract_first()
        publish_house = response.xpath().extract_first()
        publish_date = response.xpath().extract_first()
        book_price = response.xpath().extract_first()


