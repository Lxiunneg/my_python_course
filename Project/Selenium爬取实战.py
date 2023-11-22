# 从urllib.parse模块中导入urljoin函数，用于处理URL
from urllib.parse import urljoin
# 从selenium模块中导入webdriver，用于驱动浏览器进行操作
# 导入TimeoutException，用于处理超时异常
# 导入By，用于定位页面元素
# 导入expected_conditions和WebDriverWait，用于处理页面加载等待
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# 导入pymongo模块，用于操作MongoDB数据库
import pymongo
# 导入logging模块，用于记录日志
import logging

# 设置日志输出格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s : %(message)s')

# 定义常量INDEX_URL，表示目标网页的URL模板
# 定义常量TIME_OUT，表示页面加载的最大等待时间
# 定义常量TOTAL_PAGE，表示要爬取的总页数
INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIME_OUT = 10
TOTAL_PAGE = 10

# 定义MongoDB连接字符串、数据库名和集合名
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'Selenium'
MONGO_COLLECTION_NAME = 'movies'

# 创建MongoDB客户端对象，用于连接MongoDB数据库
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
# 创建MongoDB数据库对象，用于操作指定的数据库
db = client[MONGO_DB_NAME]
# 创建MongoDB集合对象，用于操作指定的集合
collection = db[MONGO_COLLECTION_NAME]

# 创建Chrome浏览器选项对象，用于设置浏览器的选项
options = webdriver.ChromeOptions()
# 创建Chrome浏览器对象，用于操作Chrome浏览器
browser = webdriver.Chrome(options=options)
# 创建WebDriverWait对象，设置浏览器的显示等待时间
wait = WebDriverWait(browser, TIME_OUT)

# 定义爬取页面的通用函数
def scrape_page(url, condition, locator):
    """
    爬取页面的通用函数
    """
    # 记录开始爬取页面的日志
    logging.info('scraping %s', url)
    try:
        # 访问指定的URL
        browser.get(url)
        # 等待页面加载完成
        wait.until(condition(locator))
    except TimeoutException:
        # 如果出现超时异常，则记录错误日志
        logging.error('error occured while scraping %s', url, exe_info=True)

# 定义爬取详情页的函数
def scrape_index(page):
    """
    爬取详情页的函数
    """
    # 根据页码生成目标URL
    url = INDEX_URL.format(page=page)
    # 调用爬取页面的通用函数，爬取详情页
    scrape_page(url=url, condition=EC.visibility_of_all_elements_located,
                locator=(By.CSS_SELECTOR, '#index .item'))

# 定义解析URL的函数
def parse_index():
    """
    解析URL的函数
    """
    # 定位页面中的电影名称元素
    elements = browser.find_elements(
        by=By.CSS_SELECTOR, value='#index .item .name')
    for element in elements:
        # 获取电影名称元素的href属性，即电影详情页的URL
        href = element.get_attribute('href')
        # 返回完整的电影详情页的URL
        yield urljoin(INDEX_URL, href)

# 定义爬取详情页信息的函数
def scrape_detail(url):
    """
    爬取详情页信息的函数
    """
    # 调用爬取页面的通用函数，爬取详情页
    scrape_page(url=url, condition=EC.visibility_of_all_elements_located,
                locator=(By.CSS_SELECTOR, 'h2'))

# 定义解析详情页信息的函数
def parse_detail():
    """
    解析详情页信息的函数
    """
    # 获取当前页面的URL
    url = browser.current_url
    # 获取电影名称
    name = browser.find_element(by=By.TAG_NAME, value='h2').text
    # 获取电影类别
    categories = [element.text for element in browser.find_elements(
        by=By.CSS_SELECTOR, value='.categories button span')]
    # 获取电影封面图的URL
    cover = browser.find_element(
        by=By.CSS_SELECTOR, value='.cover').get_attribute('src')
    # 获取电影评分
    score = browser.find_element(by=By.CLASS_NAME, value='score').text
    # 获取电影剧情简介
    drama = browser.find_element(by=By.CSS_SELECTOR, value='.drama p').text

    # 返回电影详情信息
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }

# 定义将数据存储到MongoDB的函数
def save_data(data):
    """
    将数据存储到MongoDB的函数
    """
    # 将数据存储到MongoDB中，如果已存在则更新，否则插入
    collection.update_one({'name': data.get('name')},
                          {'$set': data}, upsert=True)

# 定义主函数
def main():
    """
    主函数
    """
    try:
        # 遍历每一页
        for page in range(1, TOTAL_PAGE+1):
            # 爬取详情页
            scrape_index(page)
            # 解析详情页中的电影详情页URL
            detail_urls = parse_index()
            for detail_url in list(detail_urls):
                # 记录开始爬取电影详情页的日志
                logging.info('get detail url %s', detail_url)
                # 爬取电影详情页
                scrape_detail(detail_url)
                # 解析电影详情页信息
                detail_data = parse_detail()
                # 将电影详情信息存储到MongoDB中
                save_data(detail_data)
                # 记录电影详情信息存储成功的日志
                logging.info('detail data saved successful!')
    finally:
        # 关闭浏览器
        browser.close()

# 如果当前文件被直接执行，则调用主函数
if __name__ == '__main__':
    main()
    # 打印爬取成功的消息
    print('seccessful!')