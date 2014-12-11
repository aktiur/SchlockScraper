# -*- coding: utf8 -*-
from __future__ import unicode_literals

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

import re
import datetime

from SchlockScraper.items import Comic

class ComicsSpider(CrawlSpider):
	name = 'comics'
	allowed_domains = ["schlockmercenary.com", "www.schlockmercenary.com"]
	start_urls = ["http://www.schlockmercenary.com/2000-06-12"] # first comic !
	
	rules = (
		Rule(LinkExtractor(restrict_xpaths = '//a[@id="nav-next"]'), callback = 'parse_comic', follow = True),
		)
	
	def __init__(self, start = None, year = None, *args, **kwargs):
		if year:
			self.start_urls = ["http://www.schlockmercenary.com/" + year + "-01-01"]
			self.rules = (
				Rule(LinkExtractor(restrict_xpaths = '//a[@id="nav-next"][contains(@href,"/'+year+'-")]'), callback = 'parse_comic', follow = True),)
		if start:
			self.start_urls = ["http://www.schlockmercenary.com/" + start]
		
		super(ComicsSpider, self).__init__(*args, **kwargs)	
	
	def parse_comic(self, response):
		comic = Comic()
		
		md = re.search(r"/([0-9]{4})-([0-9]{2})-([0-9]{2})$", response.url)
		
		if md:
			comic['date'] = datetime.date(int(md.group(1)), int(md.group(2)), int(md.group(3)))
		else:
			comic['date'] = response.xpath('//div[@id="calendar"]/a[last()]/@href').extract()[0][1:]
		
		comic['image_urls'] = response.xpath('//div[@id="comic"]/img/@src').extract()
		
		note = response.xpath('//div[@class="post footnote"]')
		
		if note:
			comic['note'] = note.extract()[0]
		
		return comic
	
	parse_start_url = parse_comic