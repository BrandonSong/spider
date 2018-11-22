from lxml import etree


text = '''
    <div>
        <ul>
            <li class="item-1"><a href="link1.html">first item</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a>
        </ul>
    </div>
'''

html = etree.HTML(text)

print(html)

# 查看element对象中包含的字符串
print(etree.tostring(html).decode())

# 获取class为item-1 li下的a的href
ret1 = html.xpath("//li[@class='item-1']/a/@href")
print(ret1)


