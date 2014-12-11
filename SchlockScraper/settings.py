# -*- coding: utf-8 -*-

# Scrapy settings for Schlock project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'SchlockScraper'

SPIDER_MODULES = ['SchlockScraper.spiders']
NEWSPIDER_MODULE = 'SchlockScraper.spiders'

DOWNLOAD_DELAY = 0.1

FILES_URLS_FIELD = 'image_urls'
FILES_RESULT_FIELD = 'images'

FILES_EXPIRES = 3650

FILES_STORE = "images"

ITEM_PIPELINES = {'SchlockScraper.pipelines.SchlockPipeline':1}



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'SchlockScraper (+http://www.yourdomain.com)'
