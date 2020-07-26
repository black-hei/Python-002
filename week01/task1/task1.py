# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
# bs4是第三方库需要使用pip命令安装


def drop_space(s: str):
    """
    辅助函数
    只获取电影类型和时间
    :param s:
    :return:
    """
    return s.split(':')[1].strip()


def save_csv(movie_list):
    """
    使用pandas保存到csv文件
    :param movie_list:
    :return:
    """

    movies = pd.DataFrame(movie_list)

    movies.to_csv('movies1', sep='\n', encoding='utf8', index=False, header=False)


def scrapy_html():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    cookie = 'uuid=99AC2AA0CE8911EABD387F49F1B5315944522B9656C74D378D7B79FAC7E93D90'
    myurl = 'https://maoyan.com/films?showType=3'

    header = {'User-Agent': user_agent, 'CooKie': cookie, }
    response = requests.get(myurl,headers=header)

    bs_info = bs(response.text, 'html.parser')
    movie_list = []

    movielist = bs_info.find_all('div', attrs={'class': 'movies-list'})
    tags = movielist[0].find_all('dl', attrs={'class': 'movie-list'})[0]
    movies_info = tags.find_all('div', attrs={'class': 'movie-hover-info'})


    # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
    for i in range(10):
        movie_name = movies_info[i].find_all('span', attrs={'class': 'name'})[0].text

        tmp = movies_info[i].find_all('div', attrs={'class': 'movie-hover-title'})
        #print(tmp[2].text)
        movie_type = drop_space(tmp[1].text.strip())

        movie_time = drop_space(tmp[3].text.strip())

        movie_list.append([f'电影名称：{movie_name}', f'电影类型：{movie_type}', f'上映时间：{movie_time}', '-------------------------'])
    return movie_list


if __name__ == '__main__':
    movie_list = scrapy_html()
    save_csv(movie_list)
