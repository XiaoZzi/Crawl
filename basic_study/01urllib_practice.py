import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
import requests


# 获取cookie
def get_cookie():
    cookie = http.cookiejar.LWPCookieJar()
    handle = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handle)
    data = bytes(urllib.parse.urlencode({'loginname': '18513510827', 'nloginpwd': '123456', 'chkRememberMe': 'on'}), encoding='utf-8')
    url = 'https://www.51kaihui.com/login/verify'
    request = urllib.request.Request(url=url, data=data)
    opener.open(request)
    cookie.save(filename='cookie.txt', ignore_discard=True, ignore_expires=True)


# 使用cookie
if __name__ == '__main__':
    get_cookie()
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
    # handle = urllib.request.HTTPCookieProcessor(cookie)
    # opener = urllib.request.build_opener(handle)
    header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
              'Connection': 'keep-alive',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    url = 'https://www.51kaihui.com/customer/user/list?'
    # request = urllib.request.Request(headers=header, url=url)
    # response = opener.open(request)
    # print(response.read().decode('utf-8'))
    r = requests.get(url=url, cookies=cookie, headers=header)   # 我不知道为什么得到的内容不是这个网址的是首页的
    print(r.text)




