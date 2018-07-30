import requests
import json
import requests.exceptions
from requests.auth import HTTPBasicAuth


# 1.requests使用
# response = requests.get('http://baidu.com')
# print(type(response))
# print(response.text)
# print(response.headers)
# print(response.status_code)
# print(response.cookies)
#
# # requests各种请求方式
# requests.post('http://httpbin.org/post')
# requests.put('http://httpbin.org/put')
# requests.delete('http://httpbin.org/delete')
# requests.head('http://httpbin.org/get')
# requests.options('http://httpbin.org/get')

# requests带参数的请求
# data = {
#     'name': 'gerry',
#     'age': 22
# }
# response = requests.get('http://httpbin.org/get', params=data)
# print(response.text)
#
# # requests解析json
# print(response.json())
# print(json.loads(response.text))

# 获取二进制数据
# response = requests.get('https://github.com/favicon.ico')
# print(type(response.text), type(response.content))
# print(response.text)
# print(response.content)
# with open('github.ico', 'wb') as f:
#     f.write(response.content)
#     f.close()

# 添加headers
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
# response = requests.get('http://www.zhihu.com/explore', headers=header)
# print(response.text)

# 基于post请求
# data = {
#     'name': 'gerry',
#     'age': 22
# }
# response = requests.post(url='http://httpbin.org/post', data=data)
# print(response.text)

# response属性
# response = requests.get('http://baidu.com')
# print(type(response))
# print(response.text)
# print(response.headers)
# print(response.status_code)
# print(response.cookies)   # 获取cookie
# print(response.history)   # 访问的历史记录

# 高级操作 文件上传
# file = {'file': open('github.ico', 'rb')}
# response = requests.post('http://httpbin.org/post', files=file)
# print(response.text)

# 会话维持
# requests.get('http://httpbin.org/cookies/set/number/123456')  # httpbin.org提供的set接口可设置cookie
# response = requests.get('http://httpbin.org/cookies')
# print(response.text)   # 得到空的cookie是因为两次get相当于两个浏览器访问的，得不到
# 改进 使用session模拟一个会话
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)

# 证书验证
# 不进行证书验证
# import urllib3
# urllib3.disable_warnings()  # 去掉警告
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)
# # 使用证书
# response = requests.get('https://www.12306.cn', cert=('/path/server.cert', '/path/key'))
# print(response.status_code)

# 代理设置
# proxy = {
#     'http': 'http://user:password@127.0.0.1:7000/',  # 带用户名密码的
#     'https': '127.0.0.1:7654'    # 不带用户名密码的
# }
# response = requests.get(url='http://www.taobao.com', proxies=proxy)
# print(response.status_code)

# 超时设置 异常处理
# try:
#     response = requests.get(url='http://www.taobao.com', timeout=0.01)
#     print(response.status_code)
# except requests.exceptions.ConnectTimeout:
#     print('TIMEOUT')

# 认证设置  访问时需要认证
response = requests.get(url='http://www.taobao.com', auth=HTTPBasicAuth('user', 'password'))
print(response.status_code)
