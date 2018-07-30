import requests

url = 'http://toutiao.com/group/6428359204088660226/'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
content = requests.get(url=url, headers=header).text
print(content)