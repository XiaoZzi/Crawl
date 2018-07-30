# 完全模拟浏览器操作，可以获取浏览器JavaScript渲染后的源码
# driver.current_url
# driver.get_cookies()
# driver.page_source
# driver.find_element(By.ID,'id')   # 单个元素返回元素
# driver.find_elements(By.ID,'id')   # 多个元素以列表形式返回
# switch_to.frame() switch_to.parent_frame()
# ActionChains.drive_and_drop('source','target').perform()
# drive.execute_script    # 执行javascript
# driver.find_elements(By.ID,'id').get_attribute()   获取属性
# driver.find_elements(By.ID,'id').text   # 获取文本值
# 隐式等待 driver.implicitly_wait(10)
# 显式等待 WebDriverWait(driver, 30).until(
#             (lambda x: x.find_elements(by=locate_type, value=locate_expression))
#         )
# driver.forword()  driver.back()   前进后退
# driver.add_cookie({})  drive.get_cookies() driver.delete_all_cookies()

# driver.execute_script('window.open()')  driver.switch_to_window(driver.window_handles[0])  选项卡管理
