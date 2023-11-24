# 导入Selenium库中的webdriver模块，用于控制浏览器
from selenium import webdriver
# 导入Selenium库中的By模块，用于指定元素的定位方式
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 创建Chrome浏览器的选项对象
option = webdriver.ChromeOptions()
# 设置Chrome浏览器的选项，使得浏览器在脚本执行完后不会关闭
option.add_experimental_option("detach", True)
webdriver_service = Service('/usr/bin/chromedriver')
# 创建一个Chrome浏览器对象，并传入之前设置的选项
browser = webdriver.Chrome(options=option,service=webdriver_service)

# 定义要访问的网页地址
url = 'https://spa2.scrape.center/'
# 让浏览器打开指定的网页
browser.get(url)

# 使用find_element方法通过类名定位到页面上的元素
input = browser.find_element(by=By.CLASS_NAME, value='logo-title')

# 打印找到的元素的id属性
print(input.id)
# 打印找到的元素的标签名
print(input.tag_name)
# 打印找到的元素的大小
print(input.size)