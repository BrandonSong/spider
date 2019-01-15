# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Item
import pymongo


class MtmsPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.Mongo_Url = crawler.settings.get('MONGO_URL', )
        cls.DB_Name = crawler.settings.get('DB_NAME')

    def open_spider(self):
        self.client = pymongo.MongoClient(self.Mongo_Url)
        self.db = self.client[self.DB_Name]

    def close_spider(self):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        item = dict(item) if isinstance(item, Item) else item
        collection.insert(item)
        return item
