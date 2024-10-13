import time

import requests
from bs4 import BeautifulSoup, FeatureNotFound

import base64

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Step 1: 发送 GET 请求获取页面 HTML
url_login_page = 'https://ehall.fudan.edu.cn/ywtb-portal/fudan/index.html#/hall'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Referer": "https://elife.fudan.edu.cn/app/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}

sso_url = "https://elife.fudan.edu.cn/sso/login?targetUrl=base64aHR0cHM6Ly9lbGlmZS5mdWRhbi5lZHUuY24vYXBw"
app_url = "https://elife.fudan.edu.cn/app/"

error_string = "您将登录的是："

data = {
        "username": "",
        "password": ""
    }

session = requests.Session()
session.headers.update(headers)
response = requests.get(sso_url, allow_redirects=True,
                                    headers={
                                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15"},
                                    cookies=None)

login_url = response.url

print(login_url)
session.get(app_url, allow_redirects=True)
response = session.get(login_url, allow_redirects=True)
# print(response.text)

soup = BeautifulSoup(response.text, "lxml")
inputs = soup.find_all("input")

for input in inputs[2::]:
    data[input.get("name")] = input.get("value")
session.headers.update({"Referer": "https://uis.fudan.edu.cn/"})
response = session.post(login_url, data=data, allow_redirects=True)

print(response.text)
print(response.cookies)
print(response.url)


if error_string in response.text:
    print("UIS Login Failed")
    raise Exception("UIS Login Failed")

print("UIS Login Successful")
# driver = webdriver.Edge()


# driver = webdriver.Chrome()
# driver.get('https://ehall.fudan.edu.cn/ywtb-portal/fudan/index.html#/hall')
# time.sleep(10)
# url_getByCardsPages = 'https://ehall.fudan.edu.cn/jsonp/ywtb/home/getByCardsPages?_=1728265897764'
# url_getPortal = 'https://ehall.fudan.edu.cn/jsonp/ywtb/home/getPortalPage?_=1728265897891'
# url_getUserInfo = 'https://ehall.fudan.edu.cn/jsonp/ywtb/info/getUserInfoAndSchoolInfo.json?_=1728265898003'
# url_getfirst = 'https://ehall.fudan.edu.cn/jsonp/getUserFirstLogin?_=1728266262996'
# response = session.get(url_getUserInfo, headers=headers)
# print(response.text)

# # Step 2: 解析 CSRF token
# soup = BeautifulSoup(response.text, 'html.parser')

#
# print(soup)
# import requests
# from bs4 import BeautifulSoup
#
# # Step 1: 发送 GET 请求获取页面 HTML
# url_login_page = 'https://ehall.fudan.edu.cn/ywtb-portal/fudan/index.html#/hall'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
# }
# session = requests.Session()
# response = session.get(url_login_page, headers=headers)
#
# print(response.text)
#
# # Step 2: 解析 CSRF token
# soup = BeautifulSoup(response.text, 'html.parser')
#
# print(soup)

# csrf_token = soup.find('input', {'name': 'csrf_token'})['value']  # 需要根据实际页面结构找到正确的字段名称
#
# # Step 3: 使用 CSRF token 进行 POST 请求
# login_url = 'https://example.com/login'
# login_data = {
#     'username': 'your_username',
#     'password': 'your_password',
#     'csrf_token': csrf_token
# }
# response = session.post(login_url, headers=headers, data=login_data)
#
# # 检查登录是否成功
# if 'success' in response.text:
#     print("登录成功")
# else:
#     print("登录失败")
