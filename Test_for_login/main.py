import time
from email.header import Header

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import requests

#maybe change
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Referer": "https://elife.fudan.edu.cn/app/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9，,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
}


url = 'https://ehall.fudan.edu.cn/ywtb-portal/fudan/index.html#/hall'

data = {'username': '',
        'password': ''}


# session = requests.session()
# cookie_jar = session.post(url=url, data=data, headers=headers).cookies
# cookie_t = requests.utils.dict_from_cookiejar(cookie_jar)
def login():
        driver = webdriver.Edge()
        # driver = webdriver.Chrome()
        driver.get(url)
        # time.sleep(2)
        # driver.find_element(By.CLASS_NAME, 'btnloginbox').click()
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btnloginbox'))).click()
        # cookies = driver.get_cookies()

        time.sleep(1)
        driver.find_element(By.ID, 'username').send_keys(data['username'])
        driver.find_element(By.ID, 'password').send_keys(data['password'])

        driver.find_element(By.ID, 'idcheckloginbtn').click()

        time.sleep(1)
        print('finsih login')
        # driver.find_element(By.ID,'searchbarId').send_keys('体')
        # time.sleep(1)
        # 添加延时或保持打开
        # time.sleep(10)  # 暂停10秒后关闭
        driver.find_element(By.XPATH, '//input[@class="content" and @maxlength="100"]').send_keys('体')
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[@class="btn amp-theme" and @type="button"]').click()
        time.sleep(1)

        driver.find_element(By.CLASS_NAME,'ivu-tooltip-rel').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//div[@class="amp-theme app-enter"]').click()
        time.sleep(2)
        # 添加寻找元素
        #
        #因为切换页面了，所以捕获不到
        #
        # < a
        # style = "color:#c00;font-weight:bold"
        # href = "/public/front/toResourceFrame.htm?contentId=8aecc6ce749544fd01749a31a04332c2" > 立即预订 < / a >
        # < a
        # style = "color:#c00;font-weight:bold"
        # href = "/public/front/toResourceFrame.htm?contentId=8aecc6ce749544fd01749a31a04332c2" > 立即预订 < / a >
        try:
            # 等待并定位链接
            link_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//a[@href="/public/front/toResourceFrame.htm?contentId=8aecc6ce749544fd01749a31a04332c2"]'))
            )

            # 点击 '立即预订' 链接
            link_element.click()

        except Exception as e:
            print(f"发生错误: {e}")

        # 关闭浏览器
        # driver.quit()

        # input("Press Enter to close the browser·...")  # 按回车键后才关闭


# input("Press Enter to close the browser·...")  # 按回车键后才关闭


def search():
        # driver = webdriver.Edge()
        # driver.get(url)
        pass




# driver.get("https://www.bilibili.com")


# driver.find_element('.header-login-entry').clear()
# driver.find_element(By.CLASS_NAME,'header-login-entry').click()\

# 定义任务
# def task():
#     print("任务在北京时间执行:", datetime.now())
#     login()
#     #task 模拟发送post请求

# exit(0)


# 创建调度器
# scheduler = BlockingScheduler()

# 设置任务为每天12:00在北京时间执行
# beijing_timezone = pytz.timezone('Asia/Shanghai')

# scheduler.add_job(task, CronTrigger(hour=14, minute=34, timezone=beijing_timezone))
# scheduler.add_job(task, 'interval', minutes=1)
# print("定时任务已启动...")
# scheduler.start()

if __name__ == '__main__':
    print("here we go!!")
    login()
    search()
