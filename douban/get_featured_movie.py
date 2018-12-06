import requests
import re
from bs4 import BeautifulSoup


def get_featured_movie_url_set():
    # 定义http请求
    target = 'https://movie.douban.com/'
    # 打开请求
    req = requests.get(url=target)
    # 获取网页html
    html = req.text
    # 生成BeautifulSoup对象
    soup = BeautifulSoup(html, 'html.parser')
    featured_movie = soup.find_all('a', {"class": "slide-page"})

    url_set = set()
    for movie_item in featured_movie:
        movie_url = movie_item['href']
        print(movie_url)
        if re.match('^https://movie.douban.com/subject/.*/?tag=%E7%83%AD%E9%97%A8&from=gaia_video$', movie_url):
            url_set.add(movie_url)

    return url_set


# main函数
if __name__ == "__main__":
    for url in get_featured_movie_url_set():
        print(url)
