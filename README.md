How to build
------------

It's a bit messy, but here's how you do it for now:

-   cd in SchlockScraper (the root repository, not the directory of the same name that is inside it)

-   scrape the table of contents:
    
	    scrapy crawl toc -t jsonlines -o toc.json
		
-   then, scrape the comics themselves:
		
		scrapy crawl comics -t jsonlines -o comics.json
		
-   Finally, you can execute the python file *offline_builder.py* to build the html pages :

        python offline_builder.py
		
		
How to read
-----------

Get to one of the numbered pages in your favourite browser.
Each book is entirely contained in one page. I'm currently thinking 
how I could intelligently cut down these pages (by chapter? by year?).

You can use J and K to navigate to the next or previous comic, just like it works
on Facebook or 9gag.

I also implemented another browsing mode which should be more efficient.
D and F can be used to scroll down and up in a smart way, getting to the next comic
if it is small enough to be shown entirely or the screen, or showing progressively longer
comics. This way, you never need to use the mouse or the arrow keys.

You can set a bookmark to a specific comic with the link at the bottom of it.
You can use the link at the top of the page or the B key to go to the bookmark, even
if you're currently on a different page.
