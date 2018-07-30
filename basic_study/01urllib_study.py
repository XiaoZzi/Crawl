import urllib.request
import urllib.parse
import urllib.error
import socket
import http.cookiejar

# 1.get类型的请求
# response1 = urllib.request.urlopen('http://www.baidu.com')
# print(response1.read().decode('utf-8')) # 通过read()方法获得相应体的内容，为字节流

# 2.post类型的请求 如果加了data参数就是以post形式发送
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response2 = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response2.read().decode('utf-8'))

# 3.超时设置，timeout
# try:
#     response3 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):   # 判断错误原因
#         print('TIMEOUT')
#     else:
#         raise e

# 4.响应
# response4 = urllib.request.urlopen('http://httpbin.org')
# print(type(response4))
# print(response4.status)
# print(response4.getheaders())
# print(response4.getheader('Server'))   # 获取特定的响应头

# 5.如果要发送一个headers怎么做？ 在urlopen中是没有headers参数的
# 这时需要借助url.request.Request来构造一个请求，然后使用urlopen发送这个请求
# url = 'http://httpbin.org/post'
# headers = {'Host': 'httpbin.org',
#            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
# dic = {'name': 'Merry'}
# data = bytes(urllib.parse.urlencode(dic), encoding='utf-8')
# request = urllib.request.Request(url=url, headers=headers, data=data, method='POST')
# # request.add_header('Host','httpbin.org')  # 了解一下，这个好像只能添加一个嘛，多个的话只能用for循环
# response5 = urllib.request.urlopen(request)
# print(response5.read().decode('utf-8'))

# handler辅助工具设置比如代理
# proxy_handle = urllib.request.ProxyHandler({
#     'http': '127.0.0.1:1234',
#     'https': '127.0.0.1:5678'
# })
# opener = urllib.request.build_opener(proxy_handle)
# request = urllib.request.Request(url='http://httobin.org/get')
# response6 = opener.open(request)
# print(response6.read())

# cookie 作用是维持登录状态
# 获取cookie
# cookie = http.cookiejar.CookieJar()
# handle = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handle)
# request = urllib.request.Request(url='http://www.baidu.com')
# response7 = opener.open(request)
# for item in cookie:   # 在网页打开后cookie被自动赋值，打印cookie
#     print(item.name + '=' + item.value)
# 保存cookie
# filename = 'cookie.txt'
# # cookie = http.cookiejar.MozillaCookieJar(filename)    # 火狐浏览器的保存格式
# cookie = http.cookiejar.LWPCookieJar(filename)   # LWP2.0的保存格式
# handle = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handle)
# request = urllib.request.Request(url='http://www.baidu.com')
# response7 = opener.open(request)
# cookie.save(ignore_discard=True, ignore_expires=True)
# 使用cookie
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie.txt', ignore_expires=True,ignore_discard=True)
# handle = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handle)
# request = urllib.request.Request(url='http://www.baidu.com')
# response7 = opener.open(request)
# print(response7.read().decode('utf-8'))

# 异常处理
# try:
#     response = urllib.request.urlopen('http://cuiqingcai.com/index.htm')
# except urllib.error.URLError as e:
#     print(e.reason)

# try:
#     response = urllib.request.urlopen('http://cuiqingcai.com/index.htm')
# except urllib.error.HTTPError as e:  # 首先捕获子类异常
#     print(e.reason, e.code, e.headers, sep='\n')
# except urllib.error.URLError as e:  # 然后依次捕捉父类异常
#     print(e.reason)
# else:
#     print('Request Successful')

# try:
#     response = urllib.request.urlopen('http://www.baidu.com', timeout=0.01)
# except urllib.error.URLError as e:
#     print(type(e.reason))
#     if isinstance(e.reason, socket.timeout):
#         print('TIMEOUT')

# urlparse 解析
# result = urllib.parse.urlparse('www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)
# result2 = urllib.parse.urlparse(url='www.baidu.com/index.html;user?id=5#comment', scheme='https')
# print(result2)  # 如果网址有协议类型信息，指定类型是不生效的
# result3 = urllib.parse.urlparse(url='www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
# print(result3)

# urlunparse 将url拼接的
# data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urllib.parse.urlunparse(data))

# urljoin 将两个url拼接，url的七个部分，在后面的url中有，则使用后面的，否则使用前面的
# print(urllib.parse.urljoin('www.baidu.com/index.html;user?id=5#comment', 'https://www.baidu.com/index.html;user?id=6#comment'))

# urlencode 可以将字典对象转化为get请求参数
params = {
    'name': 'hahah',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urllib.parse.urlencode(params)
print(url)