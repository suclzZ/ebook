# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 定义了爬取的字段属性
class QidianItem(scrapy.Item):
    # define the fields for your item here like:
    # collection = table = 'Qidian'
    index = 'ebook'
    type = 'novel'

    bid = scrapy.Field()
    #小说名
    title = scrapy.Field()
    #作者
    author = scrapy.Field()
    #分类
    types = scrapy.Field()
    #数据创建时间
    crtDate = scrapy.Field()
    #小说发布时间
    pubDate = scrapy.Field()
    #小说来源
    comeFrom = scrapy.Field()
    #简介
    introduction = scrapy.Field()
    #封面图片
    image = scrapy.Field()
    #小说内容
    content = scrapy.Field()
    #地址
    url = scrapy.Field()

    # 状态
    state = scrapy.Field()
