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

#输入自己的账号和密码
data = {'username': '23210720160',
        'password': 'guoBB18876322223'}

# 初始化找到的标志
found = False

week = {   '1':'one1',
           '2':'one2',
           '3':'oen3',
           '4':'one4',
           '5':'one5',
           '6':'one6',
           '7':'one7'}

# 定义函数来将网页上的日期字符串转换为 datetime 对象
def convert_to_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()


# 定义函数来遍历页面元素并查找日期
def find_date_and_click(driver,user_input_date):
    global found

    while not found:
        # 获取当前页面上所有日期元素
        date_elements = driver.find_elements(By.XPATH, '//ul/li[starts-with(@id, "one")]')

        for date_element in date_elements:
            print("date_element: ", date_element)
            date_text = date_element.text.split("\n")[0].strip()  # 提取日期文本
            print(f"网页上的日期文本: {date_text}")

            try:
                element_date = convert_to_date(date_text)
            except ValueError:
                # 如果不是有效日期，跳过该元素
                continue

            # 如果日期与用户输入的日期匹配
            if element_date == user_input_date:
                print(f"找到日期 {user_input_date}，点击该元素")

                # 获取用户输入的日期对应的星期几（1是星期一，7是星期日）
                weekday_number = user_input_date.isoweekday()

                # 根据星期几，获取对应的one ID
                one_id = week.get(str(weekday_number))

                if one_id:
                    # 通过ID找到并点击对应的li元素
                    driver.find_element(By.ID, one_id).click()
                    found = True
                    break

        # 如果未找到，点击“下一页”按钮继续翻页
        if not found:
            print(f"日期 {user_input_date} 不在当前页面，点击 '下一页'")
            try:
                next_button = driver.find_element(By.XPATH, '//li[@class="right" and @onclick="nextWeek(\'next\')"]')
                next_button.click()

                # 等待页面加载完成
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//ul/li[starts-with(@id, "one")]'))
                )
            except Exception as e:
                print(f"无法点击下一页: {e}")
                break


# session = requests.session()
# cookie_jar = session.post(url=url, data=data, headers=headers).cookies
# cookie_t = requests.utils.dict_from_cookiejar(cookie_jar)
def login():

        # 让用户输入目标日期，格式为 YYYY-MM-DD
        user_input_date_str = input("请输入目标日期 (格式为 YYYY-MM-DD): ")
        # user_input_date_str = '2024-10-15'

        # 将用户输入的日期字符串转换为 date 对象
        try:
            user_input_date = datetime.strptime(user_input_date_str, "%Y-%m-%d").date()
            # weekday_number = user_input_date.isoweekday()
            # print(weekday_number)
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
        # 获取所有包含日期的 li 元素
        # date_elements = driver.find_elements(By.XPATH, '//ul/li[starts-with(@id, "one")]')
        # time.sleep(1)



        # driver.find_element(By.XPATH, '//li[@class="right" and @onclick="nextWeek(\'next\')"]').click()
        # time.sleep(1)

        # driver.find_element(By.ID,'one3').click()

        find_date_and_click(driver,user_input_date)



        # driver.find_element(By.XPATH, '//li[@class="right" and @onclick="nextWeek(\'next\')"]').click()




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
