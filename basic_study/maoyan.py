# 爬取猫眼电影top100
import urllib.parse
import requests
import re
import time
import json


def get_film_data(offset):
    data = {
        'offset': offset
    }
    base_url = 'http://maoyan.com/board/4?'
    url = base_url + urllib.parse.urlencode(data)
    print(url)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    response = requests.get(url=url, headers=header)
    if response.status_code == 200:
        content = response.text.strip().replace(r'\n', '').replace(r'\t', '').replace(' ', '')
        parttern = re.compile('board-index-(.*?)">.*?data-src="(.*?)".*?"movie-item-info".*?title="(.*?)".*?"star">(.*?)</p>.*?"releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?"fraction">(.*?)</i>', re.S)
        start = time.clock()
        result1 = re.findall(parttern, content)
        print(time.clock() - start)
        for item in result1:
            yield {
                'index': item[0],
                'image': item[1],
                'name': item[2],
                'actor': item[3].strip()[3:],
                'time': item[4][5:],
                'score': item[5]+item[6]
            }
    return response.status_code


def write_to_file(content):
    with open('maoyan.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


# 写到一个文件去就最好不要用多线程了，不然写的乱
if __name__ == '__main__':
    for index in range(10):
        for data in get_film_data(index*10):
            write_to_file(data)