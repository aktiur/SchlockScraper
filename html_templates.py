# -*- coding: utf8 -*-
from __future__ import unicode_literals

# helper functions
def indent(s, n):
    lines = s.split('\n')
    lines = [(n * ' ') + line for line in lines]
    s = '\n'.join(lines)
    return s


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

BOOK = """
<h1>Schlock Mercenary offline</h1>
<h2>Book {book_number}: {book_title}</h2>

<div id="bookmark">You don't have set a bookmark yet!</div>

{comics}
""".lstrip()

CHAPTER = """
<h3><a name="{chapter_anchor}"></a>{chapter_title}</h3>
""".lstrip()

COMIC = """
{new_chapter}

<div id="{date_anchor}" class="comic">
  <h4><a name="{date_anchor}"></a>{date}</h4>
  <div class='images'>
    {images}
  </div>
  {footnote}
  <div class='links'>
    <a href="#" class="setbookmark" data-anchor="{date_anchor}">Put bookmark here!</a> | <a href='{original_link}'>See original page</a>
  </div>
</div>
""".lstrip()

IMAGE = "<img src='images/{path}' alt='{alt}' />\n"

HTML5 = """
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