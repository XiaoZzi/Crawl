import requests
import urllib.parse
from requests.exceptions import RequestException
import json
import re
from bs4 import BeautifulSoup
from json.decoder import JSONDecodeError
import time


def index_page(index, keyword):
    data = {
        'offset': index,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urllib.parse.urlencode(data)
    try:
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.text
        else:
            return response.status_code
    except RequestException:
        print('请求索引页出错')
        return None


def parse_index_page(content):
    data = json.loads(content)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            if 'article_url' in item.keys():
                yield item.get('article_url')


def get_picture(content):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    for url in parse_index_page(content):
        response = requests.get(url=url, headers=header)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            title = soup.select('title')[0].get_text()
            partern = re.compile('gallery:JSON.parse(.*?)sib', re.S)
            sub_image = re.search(partern, response.text.replace(r'\n', '').replace(r'\t', '').replace(' ', ''))
            if sub_image:
                sub_image = sub_image.group(1)[2:-4].replace('\\', '')
                try:
                    sub_image = json.loads(sub_image)
                except JSONDecodeError:
                    print('=====', sub_image)
                try:
                    sub_image.keys()
                except AttributeError:
                    print('====', sub_image)
                if 'count' in sub_image.keys() and 'sub_images' in sub_image.keys():
                    image_number = sub_image.get('count')
                    images = [item.get('url') for item in sub_image.get('sub_images')]
                    yield {
                        'title': title,
                        'url': url,
                        'number': image_number,
                        'images': images
                    }
    time.sleep(10)


if __name__ == '__main__':
    for offset in range(10):
        html = index_page(20*offset, u'街拍')
        for image_info in get_picture(html):
            print(image_info)
