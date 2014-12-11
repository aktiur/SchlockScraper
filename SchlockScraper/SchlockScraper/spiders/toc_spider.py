# -*- coding: utf8 -*-
from __future__ import unicode_literals

import scrapy
import re
import datetime
from SchlockScraper.items import Bookmark

class TOCSpider(scrapy.Spider):
	name = "toc"
	allowed_domains = "schlockmercenary.com"
	start_urls = ["http://www.schlockmercenary.com/pages/archives"]
	
	def parse(self, response):
		blinks = map(lambda l: (l.xpath("@href").extract()[0], l), response.xpath("//h4//a"))
		books = dict()
		for (d, l) in blinks:
			dd = d[1:]
			ll = re.sub(r"<[^<>]+>", "", l.extract())
			if dd in books:
				ll = books[dd] + " " + ll
				ll = re.sub(r"\s{2,}", " ", re.sub(r"(^\s+)|(\s+$)", "", ll))
				books[dd] = ll
			else:
				books[dd] = ll
				
		for d, l in books.iteritems():
			mt = re.match(r"^Book ([0-9]+): (.+)$", l)
			book = Bookmark()
			book['type'] = 'book'
			book['number'] = int(mt.group(1))
			book['beginning'] = d
			book['title'] = mt.group(2)
			yield book

		clinks = response.xpath('//h4|//h5|//p/a[starts-with(@href,"/") or starts-with(@href,"http://www.schlockmercenary.com/")][not(img)]')
		chapters = dict()
		prefix = ""
		
		for c in clinks:
			if c.xpath('self::h4'):
				prefix = ""
			elif c.xpath('self::h5'):
				prefix = re.sub(r"(^\s+)|(\s+$)", "", re.sub(r"<[^<>]+>", "", c.extract())) + ': '
			else:
				chapter = Bookmark()
				chapter['type'] = 'chapter'
				chapter['beginning'] = c.xpath('@href').extract()[0].split('/')[-1]
				chapter['title'] = prefix + re.sub(r"<[^<>]+>", "", c.extract())
				yield chapter

