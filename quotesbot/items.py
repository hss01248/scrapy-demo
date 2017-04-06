# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanMovie(scrapy.Item):

    movie_name = scrapy.Field()
    movie_director = scrapy.Field()
    movie_writer = scrapy.Field()
    movie_roles = scrapy.Field()
    movie_language = scrapy.Field()
    movie_date = scrapy.Field()
    movie_long = scrapy.Field()
    movie_desc = scrapy.Field()


class DoubanZipai(scrapy.Item):

    name = scrapy.Field()
    title = scrapy.Field()
    urls = scrapy.Field()
    paths = scrapy.Field()

