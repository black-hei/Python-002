import scrapy
from ..items import SpidersItem
from scrapy.selector import Selector



class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    #def parse(self, response):
    #    pass

    def start_requrests(self):
        #for i in range(0, 10):
        url = 'https://maoyan.com/films?showType=3'

        headers = {'Cookie': '__mta=45994395.1595690098372.1595734425100.1595734442454.6; uuid_n_v=v1; uuid=99AC2AA0CE8911EABD387F49F1B5315944522B9656C74D378D7B79FAC7E93D90; _csrf=d64b6a8ba49f22757b4ca6b8c9578ef7f30437aafea7190adb52ec8041633d73; __guid=17099173.2936009470033159700.1595690097928.3718; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595690098; _lxsdk_cuid=173868a9e90c8-0c60114e6d5354-376b4502-e1000-173868a9e90c8; _lxsdk=99AC2AA0CE8911EABD387F49F1B5315944522B9656C74D378D7B79FAC7E93D90; mojo-uuid=d6dc8cb0bae886c6914da5158b4edb16; monitor_count=12; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595755828; __mta=45994395.1595690098372.1595734442454.1595755828252.7; _lxsdk_s=1738accfdba-ffa-358-e7a%7C%7C1'}

        yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):

        # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔

        movies = Selector(response).xpath('//div[@class="movie-hover-info"]')[0:10]
        for movie in movies:
            item = SpidersItem()
            item['movie_name'] = movie.xpath('./div[1]/span[1]/text()').extract_first()
            item['movie_type'] = movie.xpath('./div[2]/text()').extract()[1].strip()
            item['movie_time'] = movie.xpath('./div[4]/text()').extract()[1].strip()

            yield item




