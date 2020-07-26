# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class SpidersPipeline:
    def process_item(self, item, spider):

        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_time = item['movie_time']

        SaveToFile = f'{movie_name},{movie_type},{movie_time}\n'

        with open('./maoyan_top10.csv', 'a+', encoding='utf-8') as Append:
            Append.write(SaveToFile)
        return item
