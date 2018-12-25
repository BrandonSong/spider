# __author__: liqinsong
# data: 2018/12/12

from lxml import etree

text = """
        
"""
# 将字符串转换为htmlElement对象
def parse_text(text):
    htmlElement = etree.HTML(text)
    print(etree.tostring(htmlElement, encoding = "utf-8").decode())

# 将html文件转换为htmlElement对象
def parse_file(file_path):
    htmlElement = etree.parse(file_path)
    print(etree.tostring(htmlElement, encoding = "utf-8").decode())

if __name__ == '__main__':
    parse_file()