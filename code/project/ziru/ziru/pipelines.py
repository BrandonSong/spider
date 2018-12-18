# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZiruPipeline(object):
    def process_item(self, item, spider):
        """ 对数据进行清洗 """
        item["room_addr"] = item["room_addr"].replace("\n", "")
        item["room_area"] = item["room_area"].replace(" ", "").replace("\n", "")
        item["room_traffic"] = [i.replace(" ","").replace("\n", "") for i in item["room_traffic"]]
        item["room_traffic"] = [i for i in item["room_traffic"] if len(i) > 0]
        print(item)