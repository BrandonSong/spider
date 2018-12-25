# 提取数据

## 1.xpath提取数据
 ### 1.工具安装：
 Chrome中安装xpath helper  
 Firefox中安装Try Xpath

 ### 2.1 xpath语法
 ### 2.2 lxml解析html
 #### 2.2.1 将html字符串解析为html 示例代码如下
    ```
    from lxml import etree
    htmlElement = etree.HTML(html_str)
    ```
 #### 2.2.2 将html文件解析为html 示例代码如下
    ```
    from lxml import etree
    htmlElement = etree.parse(file)
    ```
    默认使用xml解析器,解析时可能会出现错误,此时需要指定解析器
    ```
    from lxml import etree
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse(file, parser=parser)
    ```
 

## 2.BeautifulSoup提取数据
### 只能加载html字符串


## 3.正则表达式提取数据
### 正则表达式语法
#### 1.1 匹配某个字符串