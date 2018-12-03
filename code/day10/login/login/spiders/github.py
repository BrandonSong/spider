# -*- coding: utf-8 -*-
import scrapy
import re


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = response.xpath("//inpput[@name='authenticity_token']/@value").extract_first()
        utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        post_data = dict(
            login = "BrandonSong",
            password = "lqs123lqs",
            authenticity_token = authenticity_token,
            utf8 = utf8,
            commit = commit
        )
        yield scrapy.FormRequest("https://github.com/session",
                                 formdata = post_data,
                                 callback = self.after_login)

    def after_login(self, response):
        ret = re.findall("BrandonSong", response.body.decode())
        print(ret)


