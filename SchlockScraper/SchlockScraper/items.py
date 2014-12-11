# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Comic(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	date = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field()
	note = scrapy.Field()
	
class Bookmark(scrapy.Item):
	type = scrapy.Field()
	number = scrapy.Field()
	title = scrapy.Field()
	beginning = scrapy.Field()
