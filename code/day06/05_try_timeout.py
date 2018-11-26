from selenium import webdriver
import time

driver = webdriver.PhantomJS()

driver.get("https://music.163.com/playlist?id=2520646277")

driver.switch_to.frame("contentFrame")
time.sleep(5)

content = driver.page_source.encode()

with open("./song.html", "wb") as f:
    f.write(content)

print(content)



