from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://mail.qq.com")

# 切换到iframe
driver.switch_to.frame("login_frame")

driver.find_element_by_id("u").send_keys("1245")

time.sleep(3)

driver.quit()
