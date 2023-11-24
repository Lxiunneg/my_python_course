from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建Chrome浏览器对象
webdriver_service = Service('/usr/bin/chromedriver')
browser = webdriver.Chrome(service=webdriver_service)

# 访问指定的URL
browser.get('https://www.baidu.com')

# 输出页面标题
print(browser.title)

# 关闭浏览器
browser.close()
