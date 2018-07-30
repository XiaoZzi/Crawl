from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pyquery import PyQuery
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def get_element(d, locate_type, locate_expression):
    try:
        element = WebDriverWait(d, 10).until(
            (lambda x: x.find_element(by=locate_type, value=locate_expression)))
        return element
    except Exception as e:
        raise e


def search(d, search_content):
    d.get('https://www.taobao.com/')
    search_input = get_element(d=d, locate_type='id', locate_expression='q')
    search_button = get_element(d=d, locate_type='xpath', locate_expression='//*[@id="J_TSearchForm"]/div[1]/button')
    search_input.send_keys(search_content)
    search_button.click()
    parse_page(d)


def next_page(d, index):
    insert_page_index_input = get_element(d=d, locate_type='xpath', locate_expression='//*[@id="mainsrp-pager"]/div/div/div/div[2]/input')
    page_button = get_element(d=d, locate_type='xpath', locate_expression='//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]')
    insert_page_index_input.clear()
    insert_page_index_input.send_keys(index)
    page_button.click()
    time.sleep(2)
    parse_page(d)


def parse_page(d):
    doc = PyQuery(d.page_source)
    current_page = doc('.item.active .num').text()
    print(u'正在获取第%s页的信息' % current_page)
    WebDriverWait(d, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        image_lazyload = item.find('.pic .J_ItemPic.img').attr('data-ks-lazyload')
        if image_lazyload:
            product = {
                'image': 'https:' + image_lazyload,
                'price': item.find('.price').text().replace('\n', ''),
                'deal': item.find('.deal-cnt').text()[:-3].replace('\n', ''),
                'item': item.find('.title').text().replace('\n', ''),
                'shop': item.find('.dsrs').text().replace('\n', ''),
                'location': item.find('.location').text().replace('\n', '')
            }
        else:
            product = {
                'image': 'https:' + item.find('.pic .J_ItemPic.img').attr('src').replace('\n', ''),
                'price': item.find('.price').text().replace('\n', ''),
                'deal': item.find('.deal-cnt').text()[:-3].replace('\n', ''),
                'item': item.find('.title').text().replace('\n', ''),
                'shop': item.find('.dsrs').text().replace('\n', ''),
                'location': item.find('.location').text().replace('\n', '')
            }
        print(product)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    search(d=driver, search_content=u'美食')
    total = get_element(d=driver, locate_type='xpath', locate_expression='//*[@id="mainsrp-pager"]/div/div/div/div[1]')
    total = int(total.text[2:5])
    for i in range(2, total + 1):
        print(i)
        next_page(driver, str(i))
    driver.quit()


