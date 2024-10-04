import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By



url_login = 'https://ehall.fudan.edu.cn/ywtb-portal/fudan/index.html#/hall'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
data = {
    'username': '23210720160',
    'password': 'guoBB18876322223'
}

session = requests.session()

# Step 1: 获取登录页面，可能包含 CSRF token
response = session.get(url_login, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 假设页面有一个 CSRF token，需要解析它
# csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
# data['csrf_token'] = csrf_token

# Step 2: 使用正确的请求地址发送登录请求
url_post = 'https://ehall.fudan.edu.cn/casp-ioc//api/clientIp'   # 从抓包分析中获取
response = session.post(url_post, data=data, headers=headers)
print(response.text)
# Step 3: 检查登录是否成功
if '成功' in response.text:
    print("登录成功")

    # Step 4: 进行后续请求
    url_target = 'https://ehall.fudan.edu.cn/jsonp/ywtb/fudan/getAppDetail?appId=7235408347493195'
    response = session.get(url_target, headers=headers)
    print(response.text)

    # url_ser = 'https://ehall.fudan.edu.cn/jsonp/ywtb/card/sendRecUseApp?appId=7235408347493195&_=1728062745898'
    # response = session.get(url_ser, headers=headers)
    # print(response.text)

else:
    print("登录失败")
