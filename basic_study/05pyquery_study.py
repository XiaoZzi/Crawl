# 同jquery,接口一样
from pyquery import PyQuery as pq

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
# 字符串初始化
doc = pq(html)
print(doc('div'))

# url初始化
# doc1 = pq(url='http://www.baidu.com')
# print(doc1('head'))

# 文件初始化
# doc2 = pq(filename='demo.html')

# 基本css选择器  #id .class li
print(doc('#logo-doodle button'))   # 空格表示 嵌套的，此id下的button, 只要满足就返回
# 对于class而言，是多属性的，本身class就包含有空格，所以我们用点表示
print('===================================')
print(doc('#logo-doodle .outer.ball0'))
print('==============================')

# 查找元素
print(doc('#logo-doodle').find('div'))

# children 查找直接子元素
print(doc('#logo-doodle').children('div'))

# 父元素
print(doc('#logo-doodle').parent())

# 所有的祖先节点
print(doc('#logo-doodle').parents())

# 兄弟元素
print(doc('#logo-doodle').siblings())

# 遍历元素
print(doc('#logo-doodle').items())   # 返回generator，使用for循环

# 获取属性
print(doc('#logo-doodle .outer.ball0').attr('class'))

# 获取文本
print(doc('head title').text())

# 获取html，比如文章的
print(doc('head').html())

# DOM操作
# addClass removeClass
print(doc('#logo-doodle-notifier .outer.ball0').attr('class'))
print(doc('#logo-doodle-notifier .outer.ball0').removeClass('outer'))
print(doc('#logo-doodle-notifier .ball0').attr('class'))
print(doc('#logo-doodle-notifier .ball0').add_class('outer'))
print(doc('#logo-doodle-notifier .outer.ball0').attr('class'))
print(doc('#logo-doodle-notifier .ball0').remove_attr)

# attr('attr','value') 修改属性
print(doc('#logo-doodle-notifier .outer.ball0').attr('class', 'heiyu'))
print(doc('#logo-doodle-notifier .heiyu').attr('class'))
# css('css','value')   修改css style
doc('#logo-doodle-notifier .heiyu').css('font-size', '14px')

# 移除标签
html = '''
<div class='wrap'>
    Hello World<p>This is a demo</p>
</div>
'''
doc = pq(html)
print(doc('.wrap').remove('p').text())

# 伪类选择器
# li = doc('li:first-child')
# li = doc('li:last-child')
# li = doc('li:nth-child(2)') 获取第二个
# li = doc('li:gt(2)') 获取第二个以后
# li = doc('li:nth-child(2n)')  获取偶数
# li = doc('li:contains(second)')  包含文本


doc = '''
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
        <li class="item active"><span class="num">2</span></li>
      </div>
'''
print('========================================')
t = pq(doc)
print(t('.item.active .num').text())

