import time
from email.header import Header

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
from datetime import datetime

from selenium import webdriver
import requests

from selenium.webdriver.common.by import By


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

url = 'https://www.bilibili.com'

data = {'username': '23210720160',
        'password': 'guoBB18876322223'}

# session = requests.session()
# cookie_jar = session.post(url=url, data=data, headers=headers).cookies
# cookie_t = requests.utils.dict_from_cookiejar(cookie_jar)
def login():
        driver = webdriver.Chrome()
        driver.get('https://ehall.fudan.edu.cn/ywtb-portal/fudan/index.html#/hall')
        driver.find_element(By.CLASS_NAME, 'btnloginbox').click()
        # cookies = driver.get_cookies()

        time.sleep(1)
        driver.find_element(By.ID, 'username').send_keys(data['username'])
        driver.find_element(By.ID, 'password').send_keys(data['password'])

        driver.find_element(By.ID, 'idcheckloginbtn').click()

        time.sleep(1)

        # driver.find_element(By.ID,'searchbarId').send_keys('体')
        time.sleep(1)
        # 添加延时或保持打开
        # time.sleep(10)  # 暂停10秒后关闭
        input("Press Enter to close the browser·...")  # 按回车键后才关闭


# print("cookies = " , cookie_t)

# driver.get("https://www.bilibili.com")


# driver.find_element('.header-login-entry').clear()
# driver.find_element(By.CLASS_NAME,'header-login-entry').click()\

# 定义任务
def task():
    print("任务在北京时间执行:", datetime.now())
    login()
    #task 模拟发送post请求

    # exit(0)


# 创建调度器
scheduler = BlockingScheduler()

# 设置任务为每天12:00在北京时间执行
beijing_timezone = pytz.timezone('Asia/Shanghai')

scheduler.add_job(task, CronTrigger(hour=14, minute=34, timezone=beijing_timezone))

print("定时任务已启动...")
scheduler.start()
