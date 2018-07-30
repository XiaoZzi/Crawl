from bs4 import BeautifulSoup


# 灵活又方便的网页解析库
# python标准库'html.parser'，内置标准库，速度适中，容错能力强
# lxml html解析器,速度快，容错能力强，需要安装c语言库
# lxml xml解析器，速度快，唯一支持xml的解析器，需要安装C语言库
# html5lib 最好的容错性，以浏览器方式解析文档，生成html5格式文档，速度慢，不依赖外部扩展


html = '''
<head><title>The document story</title></head>
<body>
  <!-- Container for the OneGoogleBar HTML. -->
  <div id="one-google" class="hidden">12345</div>

  <div id="ntp-contents">
    <div id="logo">
      <!-- The logo that is displayed in the absence of a doodle. -->
      <div id="logo-default" title="Google"></div>
      <!-- Logo displayed when theme prevents doodles. Doesn't fade. -->
      <div id="logo-non-white" title="Google"></div>
      <!-- A doodle, if any: its link and image. -->
      <div id="logo-doodle">
        <button id="logo-doodle-button">
          <img id="logo-doodle-image"></img>
        </button>
        <iframe id="logo-doodle-iframe" scrolling="no"></iframe>
        <!-- A spinner, visible on dark-themed NTPs, prompting the doodle -->
        <button id="logo-doodle-notifier">
          <div class="outer ball0"><div class="inner"></div></div>
          <div class="outer ball1"><div class="inner"></div></div>
          <div class="outer ball2"><div class="inner"></div></div>
          <div class="outer ball3"><div class="inner"></div></div>
        </button>
      </div>
'''
soup = BeautifulSoup(html, 'lxml')
# print(soup)
# print(soup.prettify())  # 格式化html代码
# print(soup.title.string)

# 标签选择器，非常快
# print(type(soup.title))
# print(soup.title)
# print(soup.head)
# print(soup.div)     # 如果有多个只返回第一个
# 获取标签名称 .name
# print(soup.title.name)
# 获取属性
# print(soup.div.attrs['id'])
# print(soup.div['id'])
# 获取内容 .string
# print(soup.div.string)
# 嵌套选择
# print(soup.head.title.string)
# 子节点以列表返回  .contents
# print(soup.body.contents)
# 子节点以迭代器返回  .children
# print(soup.body.children)
# for i, child in enumerate(soup.body.children):
#     print(i, child)
# 子孙节点以迭代器返回
# print(soup.body.descendants)
# for i, child in enumerate(soup.body.descendants):
#     print(i, child)
# 父节点 .parent
# print(soup.title.parent)
# 所有祖先节点 .parents
# print(soup.div.parents)
# for i, parent in enumerate(soup.div.parents):
#     print(i, parent)  # 倒数第二个为整个html标签，倒数第一个为整个文档
# 后面的兄弟节点，前面兄弟节点
# print(list(enumerate(soup.div.next_siblings)))
# print(list(enumerate(soup.div.previous_siblings)))
# print(list(soup.div.previous_siblings))

# 标签选择器还提供了一些选择方法
# find_all 可提供标签，属性， 内容查找文档，以列表返回所有结果
# print(soup.find_all('div'))  # 标签名
# print(soup.find_all(attrs={'class': 'outer ball0'}))  # 标签名
# print(soup.find_all(class_='outer ball0'))  # 直接用属性 class是类的意思不能直接用，加_
# print(soup.find_all(id="logo-doodle-notifier"))  # 直接用属性 class是类的意思不能直接用，加_
# 利用text文本内同来选择，返回的是text
# print(soup.find_all(text='The document story'))
# find 同find_all方法，返回第一个元素
# find_parent() find_parents() find_next_siblings() find_previous_siblings()
# find_next() find_all_next()
# find_previous() find_all_previous()

# css选择器 通过select()直接传入css选择器可完成选择, 建议使用
# 如果要选择class就在前面加上一个.
print(soup.select('.hidden'))
# 标签前面不需要添加任何内容
print(soup.select('button')[1])
# id使用#
print(soup.select('#logo-doodle button'))
# 获取属性
print(soup.select('#logo-doodle button')[0]['id'])
# 获取内容
print(soup.select('div')[0].get_text())

