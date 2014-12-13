# -*- coding: utf8 -*-
from __future__ import unicode_literals

from datetime import datetime, date, timedelta
import json
from codecs import open

import html_templates

DATE_FORMAT = "%A %B %d, %Y"
ORIGINAL_SITE = "http://www.schlockmercenary.com/"

TOC_FILE = "toc.json"
COMICS_FILES = ['comics.json']

def main():
	books = import_toc()
	comics = import_comics()
	
	for b in books:
		bf = build_book(b, comics)
		with open('book{0:02d}.html'.format(b['number']),'w', 'utf8') as f:
			f.write(bf)
	
def import_toc(file = TOC_FILE):
	toc_data = []
	with open(file, encoding = 'utf8') as f:
		for line in f:
			toc_data.append(json.loads(line))
			
	books = sorted(filter(lambda e: e['type'] == 'book', toc_data), key = lambda b: b['beginning'])
	chapters = sorted(filter(lambda e: e['type'] == 'chapter', toc_data), key = lambda b: b['beginning'])
	book_dates = map(lambda b: b['beginning'], books) + [(date.today()+timedelta(days=1)).strftime('%Y-%m-%d')]
	
	for i in xrange(0,len(books)):
		books[i]['chapters'] = filter(lambda c: book_dates[i] <= c['beginning'] < book_dates[i+1], chapters)
		books[i]['end'] = book_dates[i+1]

	return books

def import_comics(files = COMICS_FILES):
	comics = []
	for filename in files:
		with open(filename, encoding = 'utf8') as f:
			for line in f:
				comics.append(json.loads(line))
	
	comics.sort(key = lambda c: c['date'])
	return comics

def build_book(book, comics):
	comics = filter(lambda c: book['beginning'] <= c['date'] < book['end'], comics)
	chapters = {ch['beginning']: ch for ch in book['chapters']}
	
	cs = ""
	
	for c in comics:
		cs += build_comic(c, chapters.get(c['date']))
		
	bs = html_templates.BOOK.format(
		book_number = book['number'],
		book_title = book['title'],
		comics = cs
	)
	return html_templates.HTML5.format(
		page_title = 'Book ' + unicode(book['number']) + ': ' + book['title'],
		page_contents = bs
	)
	
	
def build_comic(comic, chapter = None):
	images = '\n'.join(map(lambda i: html_templates.IMAGE.format(path = i['path'], alt = 'comic images for ' +comic['date']), comic['images']))
	if chapter:
		chs = html_templates.CHAPTER.format(
			chapter_title = chapter['title'],
			chapter_anchor = anchor_from_name(chapter['title'])
		)
	else:
		chs = ''
	return html_templates.COMIC.format(
		date_anchor = comic['date'],
		date = datetime.strptime(comic['date'], '%Y-%m-%d').strftime(DATE_FORMAT),
		images = images,
		footnote = comic.get('note', ''),
		original_link = ORIGINAL_SITE + comic['date'],
		new_chapter = chs
		).lstrip()

def anchor_from_name(name):
	return name.replace(' ', '_')

if __name__ == '__main__':
	main()