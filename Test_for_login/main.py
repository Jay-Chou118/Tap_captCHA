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
from datetime import datetime, timedelta

# 获取当前系统时间
current_time = datetime.now()

# 获取当前系统日期
current_date = datetime.now().date()
# 设定 1-3 天的范围
min_date = current_date + timedelta(days=1)
max_date = current_date + timedelta(days=3)

# 标记是否需要切换到下一周
need_next_week = False



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

data = {'username': '23210720160',
        'password': 'guoBB18876322223'}



week = {'1':'one1',
           '2':'one2',
           '3':'oen3',
           '4':'one4',
           '5':'one5',
           '6':'one6',
           '7':'one7'}

# 定义函数来将网页上的日期字符串转换为 datetime 对象
def convert_to_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()


# 定义一个函数来查找页面上的日期并检查是否需要换页
def find_and_click_date(driver,user_date,date_elements):
    while True:
        # 遍历所有日期元素，查找用户输入的日期
        for date_element in date_elements:
            # 提取日期文本并转换为日期对象
            date_text = date_element.text.split("\n")[0].strip()  # 提取日期文本
            print(f"网页上的日期文本: {date_text}")

            try:
                element_date = convert_to_date(date_text)
            except ValueError:
                # 忽略无法转换的文本（例如非日期的元素）
                continue

            # 检查是否是用户输入的日期
            if element_date == user_date:
                print(f"找到日期  点击该元素")
                date_element.click()
                return True

                # 如果没找到，点击下一页按钮
            print(f"日期 {user_date} 不在当前页面，点击 '下一页'")
            try:
                # right_button = driver.find_element(By.XPATH, '//li[@class="right" and @onclick="nextWeek(\'next\')"]')
                # right_button.click()
                driver.find_element(By.XPATH,'//li[@class="right" and @onclick="nextWeek(\'next\')"]').click()
                # 等待页面加载完成
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//ul/li[starts-with(@id, "one")]'))
                )
            except Exception as e:
                print(f"无法点击下一页: {e}")
                return False


# session = requests.session()
# cookie_jar = session.post(url=url, data=data, headers=headers).cookies
# cookie_t = requests.utils.dict_from_cookiejar(cookie_jar)
def login():

        # 让用户输入目标日期，格式为 YYYY-MM-DD
        # user_input_date_str = input("请输入目标日期 (格式为 YYYY-MM-DD): ")
        user_input_date_str = '2024-10-15'
        # 将用户输入的日期字符串转换为 date 对象
        try:
            user_input_date = datetime.strptime(user_input_date_str, "%Y-%m-%d").date()
        except ValueError:
            print("日期格式不正确，请输入正确的 YYYY-MM-DD 格式")
            exit()

        print('当前时间： ',current_time)


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
        # driver.find_element(By.ID,'searchbarId').send_keys('体')
        # time.sleep(1)
        # 添加延时或保持打开
        # time.sleep(10)  # 暂停10秒后关闭
        driver.find_element(By.XPATH, '//input[@class="content" and @maxlength="100"]').send_keys('体')
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[@class="btn amp-theme" and @type="button"]').click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME,'ivu-tooltip-rel').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//div[@class="amp-theme app-enter"]').click()
        time.sleep(1)

        # 获取所有的窗口句柄
        all_windows = driver.window_handles
        for window in all_windows:
            print(window)
        # 切换到新窗口（假设新窗口是最后一个）
        driver.switch_to.window(all_windows[-1])

        try:
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH,
                                            '//a[@href="/public/front/toResourceFrame.htm?contentId=8aecc6ce749544fd01749a31a04332c2"]'))).click()

        except Exception as e:
            print(f"发生错误: {e}")
        # # 获取所有包含日期的 li 元素
        date_elements = driver.find_elements(By.XPATH, '//ul/li[starts-with(@id, "one")]')
        time.sleep(1)



        driver.find_element(By.XPATH, '//li[@class="right" and @onclick="nextWeek(\'next\')"]').click()
        time.sleep(1)

        driver.find_element(By.ID,'one3').click()
        for date_element in date_elements:
             # 提取日期文本并转换为日期对象
            print("date_element " ,date_element)
            # 提取日期文本并转换为日期对象
            date_text = date_element.text.split("\n")[0].strip()  # 仅提取日期部分
            print(f"网页上的日期文本: {date_text}")

            try:
                element_date = convert_to_date(date_text)
            except ValueError:
                # 忽略无法转换的文本（例如非日期的元素）
                continue

            # 检查是否是用户输入的日期
            if element_date == user_input_date:
                print(f"找到日期 {user_input_date}，点击该元素")
                date_element.click()  # 点击日期
                found = True
                break



        # driver.find_element(By.XPATH, '//li[@class="right" and @onclick="nextWeek(\'next\')"]').click()




        #
        # cmd = True
        # # find_and_click_date(driver,user_input_date,date_elements)
        # while (cmd == True):
        #     # 遍历所有日期元素，查找用户输入的日期
        #     for date_element in date_elements:
        #         # 提取日期文本并转换为日期对象
        #         print("date_element " ,date_element)
        #
        #         date_text = date_element.text.split("\n")[0].strip()  # 提取日期文本
        #         print(f"网页上的日期文本: {date_text}")
        #
        #         try:
        #             element_date = convert_to_date(date_text)
        #         except ValueError:
        #             # 忽略无法转换的文本（例如非日期的元素）
        #             continue
        #
        #         # 检查是否是用户输入的日期
        #         if element_date == user_input_date:
        #             print(f"找到日期  点击该元素")
        #             cmd = False
        #             date_element.click()
        #
        #
        #             # 如果没找到，点击下一页按钮
        #     print(f"日期 {user_input_date} 不在当前页面，点击 '下一页'")
        #
        #     try:
        #         right_button = driver.find_element(By.XPATH, '//li[@class="right" and @onclick="nextWeek(\'next\')"]')
        #         right_button.click()
        #         driver.find_element(By.XPATH, '//li[@class="right" and @onclick="nextWeek(\'next\')"]').click()
        #         # 等待页面加载完成
        #         WebDriverWait(driver, 10).until(
        #             EC.presence_of_element_located((By.XPATH, '//ul/li[starts-with(@id, "one")]'))
        #         )
        #     except Exception as e:
        #         print(f"无法点击下一页: {e}")






        # # 提取每个 li 元素中的日期文本
        # for date_element in date_elements:
        #     # 提取日期文本并转换为日期对象
        #     date_text = date_element.text.split("\n")[0].strip()
        #     # print(f"网页上的日期文本: {date_text}")
        #
        #     element_date = convert_to_date(date_text)
        #     # print(f"转换后的日期: {element_date}")
        #
        #     # 检查该日期是否在当前日期的1-3天范围内
        #     if min_date <= element_date <= max_date:
        #         print(f"日期 {element_date} 在当前时间的1-3天范围内，不需要切换")
        #         need_next_week = False
        #         break
        #     else:
        #         print(f"日期 {element_date} 不在范围内，可能需要切换")
        #         need_next_week = True
        #
        # # 如果没有日期在范围内，则点击右侧的 "next" 按钮
        # if need_next_week:
        #     right_button = driver.find_element(By.XPATH, '//li[@class="right" and @onclick="nextWeek(\'next\')"]')
        #     right_button.click()
        #     print("点击了 '下一周' 按钮进行切换")

        # # 计算日期差距
        # date_difference = (user_input_date - current_date).days
        #
        # # 输出当前日期和用户输入的日期差距
        # print(f"当前日期: {current_date}")
        # print(f"用户输入的日期: {user_input_date}")
        # print(f"日期差距: {date_difference} 天")
        #
        # # 根据日期差距决定是否换页
        # # 2024-10-18
        # if date_difference < 1 or date_difference > 3:
        #     print("日期不在当前时间的 1-3 天范围内，执行换页操作")
        #     # 执行换页的 Selenium 操作
        #     right_button = driver.find_element(By.XPATH, '//li[@class="right" and @onclick="nextWeek(\'next\')"]').click()
        #
        # else:
        #     print("日期在当前时间的 1-3 天范围内，无需换页")


        # 关闭浏览器
        # driver.quit()

        input("Press Enter to close the browser·...")  # 按回车键后才关闭


# input("Press Enter to close the browser·...")  # 按回车键后才关闭


# def search():
#         # driver = webdriver.Edge()
#         # driver.get(url)
#         pass




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
    # search()
