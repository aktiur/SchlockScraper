# -*- coding: utf8 -*-
from __future__ import unicode_literals

from datetime import datetime, date, timedelta
import json
from codecs import open
import markdown

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
		
	bs = BOOK_STRING.format(
		book_number = book['number'],
		book_title = book['title'],
		comics = cs
	)
	return HTML5_TEMPLATE.format(
		page_title = 'Book ' + unicode(book['number']) + ': ' + book['title'],
		page_contents = markdown.markdown(bs)
	)
	
	
def build_comic(comic, chapter = None):
	images = '\n'.join(map(lambda i: '![comic image](images/' + i['path'] + ')', comic['images']))
	if chapter:
		chs = CHAPTER_STRING.format(
			chapter_title = chapter['title'],
			chapter_anchor = anchor_from_name(chapter['title'])
		)
	else:
		chs = ''
	return COMIC_STRING.format(
		date_anchor = comic['date'],
		date = datetime.strptime(comic['date'], '%Y-%m-%d').strftime(DATE_FORMAT),
		images = images,
		footnote = comic.get('note', ''),
		original_link = ORIGINAL_SITE + comic['date'],
		new_chapter = chs
		).lstrip()

def anchor_from_name(name):
	return name
		
# characters strings for toc

TOC_STRING = """
Schlock Mercenary offline!
==========================

Table of contents
-----------------

{books}
""".lstrip()

TOC_BOOK_STRING = """
* [Book {book_number}: {book_title}]({book_link})
{chapters}
""".lstrip()

TOC_CHAPTER_STRING = """
    * [{chapter_title}]({chapter_link})
""".lstrip()

# character strings for books

BOOK_STRING = """
Schlock Mercenary offline!
==========================

## Book {book_number}: {book_title}

<div id="bookmark">You don't have set a bookmark yet!</div>

{comics}
""".lstrip()

CHAPTER_STRING = """
### <a name="{chapter_anchor}"></a>{chapter_title}
""".lstrip()

COMIC_STRING = """
{new_chapter}

#### <a name="{date_anchor}" class="comic"></a>{date}

{images}

{footnote}

<a href="#" class="setbookmark" data-anchor="{date_anchor}">Put bookmark here!</a> | [See original page]({original_link})

""".lstrip()

HTML5_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
	<title>{page_title}</title>
	<link rel="stylesheet" type="text/css" href="resources/style.css">
	<script src="resources/jquery-1.11.1.min.js"></script>
	<script src="resources/jquery.scrollTo.min.js"></script>
	<script src="resources/script.js"></script>
</head>
<body>
{page_contents}
</body>
</html>
""".lstrip()

if __name__ == '__main__':
	main()