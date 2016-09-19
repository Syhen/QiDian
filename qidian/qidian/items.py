# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#小说名称
    author = scrapy.Field()#小说作者
    title_url = scrapy.Field()#小说链接
    bid = scrapy.Field()#小说id
    relate_id = scrapy.Field()#小说存储主键
    refresh_time = scrapy.Field()#索引更新时间