import requests

s = requests.Session()
url = 'https://www.51kaihui.com/login/verify'
data = {
    'loginname': '18513510827',
    'nloginpwd': '123456',
    'chkRememberMe': 'on'
}
s.post(url=url, data=data)
response = s.get('https://www.51kaihui.com/customer/user/list?')
print(response.text)
