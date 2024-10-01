import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/")
# driver.get('https://ehall.fudan.edu.cn/ywtb-portal/fudan/index.html#/hall')

# driver.find_element('.header-login-entry').clear()
# driver.find_element(By.CLASS_NAME,'.header-login-entry').click()
cookies = driver.get_cookies()

time.sleep(2)
# driver.find_element('')

# 添加延时或保持打开
# time.sleep(10)  # 暂停10秒后关闭
input("Press Enter to close the browser·...")  # 按回车键后才关闭