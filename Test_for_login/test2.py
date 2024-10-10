import requests
from bs4 import BeautifulSoup

# Step 1: 发送 GET 请求获取页面 HTML
url_login_page = 'https://ehall.fudan.edu.cn/ywtb-portal/fudan/index.html#/hall'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
session = requests.Session()
response = session.get(url_login_page, headers=headers)

# print(response.text)

url_getByCardsPages = 'https://ehall.fudan.edu.cn/jsonp/ywtb/home/getByCardsPages?_=1728265897764'
url_getPortal = 'https://ehall.fudan.edu.cn/jsonp/ywtb/home/getPortalPage?_=1728265897891'
url_getUserInfo = 'https://ehall.fudan.edu.cn/jsonp/ywtb/info/getUserInfoAndSchoolInfo.json?_=1728265898003'
url_getfirst = 'https://ehall.fudan.edu.cn/jsonp/getUserFirstLogin?_=1728266262996'
response = session.get(url_getUserInfo, headers=headers)
print(response.text)

# # Step 2: 解析 CSRF token
soup = BeautifulSoup(response.text, 'html.parser')
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
