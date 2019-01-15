# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Item
import pymongo
from scrapy.conf import settings



class MtmsPipeline(object):

    def __init__(self):
        self.MONGO_URL = settings.get("MONGO_URL")
        self.MONGO_PORT = settings.get("MONGO_PORT")
        self.DB_NAME = settings.get("DB_NAME")

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.MONGO_URL, self.MONGO_PORT)
        self.db = self.client[self.DB_NAME]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        dict_item = dict(item) if isinstance(item, Item) else item

        print("准备插入")
        collection.insert(dict_item)
        return item
