# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    def process_item(self, item, spider):
<<<<<<< HEAD
        if spider.name == "itcast":
            # 判断对应的爬虫 来做对应的处理
            pass
        return item


class MyspiderPipeline2(object):
    def process_item(self, item, spider):
        return item
=======
        return item
>>>>>>> 11aad4ff309b4be9d324895c51401dc959ccf32a
