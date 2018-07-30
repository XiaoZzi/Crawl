# 正则表达式是对字符串操作的一种逻辑公式，非python模块独有，在re模块中实现
# 在线正则表达式测试
import requests
import re

# match 从第一个字符开始匹配
# 贪婪匹配
content = 'hello 1234567 world_this is a demo'
res = re.match('^he.*(\d+).*demo$', content)
print(res, res.span(), res.group(0), res.group(1))
# 非贪婪匹配 ?表示有或者没有
res2 = re.match('^he.*?(\d+).*demo$', content)
print(res2.group(1))

# 匹配模式 .不能匹配换行符,需要加上re.S
content2 = '''hello 1234567 world_this 
is a demo'''
res3 = re.match('^he.*?(\d+).*?demo$', content2, re.S)
print(res3.group(1))

# 转意字符 \
print(re.match('price is \$5\.0', 'price is $5.0'))


# search 匹配整个字符返回成功的第一个
content3 = '''heygfe hello 1234567 world_this 
is a demo hhahha'''
res3 = re.search('he.*?(\d+).*?demo', content3, re.S)
print(res3.group(1))

# findall 匹配整个字符以列表形式返回所有成功的
# sub 替换，返回新的
content4 = '''heygfe hello 1234567 world_this 
is a demo hhahha'''
res5 = re.sub('\d+', '89', content4)
print(res5)
# 如果要替换的字符换包括原字符串本身，我们可以先匹配源字符串，然后替换
res4 = re.sub('(\d+)', r'\1 89', content4)  # 1指的是第一个括号里的内容
print(res4)


# compile 将正则表达式编译为一个正则表达式对象
pattern = re.compile('BASE_DATA.galleryInfo\s=\s(.*)</script><script>var', re.S)
response = requests.get('https://www.toutiao.com/a6553304734898323972/')
content5 = response.text
result = re.search(pattern, content5).group(1)
print(result)
