import requests
import re
from bs4 import BeautifulSoup


def get_article(article_url):
    target = article_url
    req = requests.get(url=target)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    article = soup.findAll('div', id="link-report")
    return article


def get_today_featured_article_url_set():
    # 定义http请求
    target = 'https://www.douban.com/explore/'
    # 打开请求
    req = requests.get(url=target)
    # 获取网页html
    html = req.text
    # 生成BeautifulSoup对象
    soup = BeautifulSoup(html, 'html.parser')
    today_featured_articles = soup.find_all('a', target='_blank')

    url_set = set()
    for article in today_featured_articles:
        article_url = article['href']
        if re.match('^https://www.douban.com/note/', article_url):
            url_set.add(article_url)

    return url_set


# main函数
if __name__ == "__main__":
    for url in get_today_featured_article_url_set():
        BeautifulSoup(get_article(url), 'html.parser')
        print()
