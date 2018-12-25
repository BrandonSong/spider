# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 写excel文件的类库
from openpyxl import Workbook
import os

class FangdicahnPipeline(object):
    def __init__(self):
        """ 初始化excel信息 """
        self.wb = Workbook()
        self.ws = self.wb.active
        # 设置表头
        self.ws.append(["状态", "项目名称", "项目地址", "总套数", "总面积", "所在区域"])
        self.path = "./fangchan.xlsx"

    def process_item(self, item, spider):
        line = [item["status"], item["project"], item["address"], item["total_num"], item["total_area"], item["zone"]]
        self.ws.append(line)
        self.wb.save(self.path)
        return item
