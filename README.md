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

Get to one of the pages in your favourite browser.
You can use J and K to navigate between comics.

You can also set a bookmark to a specific comic with the link at the bottom of it.
You can use the link at the top of the page or the B key to get to the bookmark.