# -*- coding: utf-8 -*-
import scrapy


class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,  # 自动从response中寻找form表单
            formdata = {"": ""},
            callback = self.after_login
        )

    def after_login(self):
        pass