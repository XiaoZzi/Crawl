import requests
import re

response = requests.get('https://book.douban.com/')
content = response.text.strip().replace('\\n', '').replace('\\t', '').replace(' ', '')
parttern = re.compile(
    '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?"author">(.*?)</span>.*?"year">(.*?)</span>.*?</li>', re.S)
result = re.findall(parttern, content)
print(result)