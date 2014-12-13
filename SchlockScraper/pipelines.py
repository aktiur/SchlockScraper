# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from __future__ import unicode_literals

from scrapy.contrib.pipeline.files import FilesPipeline
import re

class SchlockPipeline(FilesPipeline):
	def file_path(self, request, response=None, info=None):
		mo = re.search(r"/(schlock([0-9]{4})([0-9]{2})[0-9]{2}[-a-zA-Z0-9 %]*\.([a-zA-Z ]+))", request.url)
		if mo:
			return mo.group(2) + '/' + mo.group(3) + '/' + mo.group(1)
		else:
			return 'weird/' + request.url.split('?')[0].split('/')[-1]
