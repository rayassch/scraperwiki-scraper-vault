###############################################################################
# START HERE: Tutorial 3: More advanced scraping. Shows how to follow 'next' 
# links from page to page: use functions, so you can call the same code 
# repeatedly. SCROLL TO THE BOTTOM TO SEE THE START OF THE SCRAPER.
###############################################################################

import scraperwiki
import urlparse
import lxml.html

# scrape_table function: gets passed an individual page to scrape
def scrape_table(root):
    rows = root.cssselect("div#body_right")  # selects all <tr> blocks within <table class="data">
    for row in rows:
        # Set up our data record - we'll need it later
        record = {}
        table_cells = row.cssselect("p")
        if table_cells: 
            record['Quote'] = table_cells[2].text
            # Print out the data we've gathered
            print record, '------------'
            # Finally, save the record to the datastore - 'Artist' is our unique key
            scraperwiki.sqlite.save(["Quote"], record)
        
# scrape_and_look_for_next_link function: calls the scrape_table
# function, then hunts for a 'next' link: if one is found, calls itself again
def scrape_and_look_for_next_link(url):
    html = scraperwiki.scrape(url)
    print html
    root = lxml.html.fromstring(html)
    rows = root.cssselect("div#body_right")  # selects all <tr> blocks within <table class="data">
    for row in rows:
        # Set up our data record - we'll need it later
        scrape_table(root)
        next_link = row.cssselect("a")
        print next_link
        if next_link:
            next_url = urlparse.urljoin(base_url, next_link[1].attrib.get('href'))
            print next_url
            scrape_and_look_for_next_link(next_url)

# ---------------------------------------------------------------------------
# START HERE: define your starting URL - then 
# call a function to scrape the first page in the series.
# ---------------------------------------------------------------------------
base_url = 'http://www.sgi-usa.org/encouragement/index.php/'
starting_url = urlparse.urljoin(base_url, '?')
scrape_and_look_for_next_link(starting_url)
###############################################################################
# START HERE: Tutorial 3: More advanced scraping. Shows how to follow 'next' 
# links from page to page: use functions, so you can call the same code 
# repeatedly. SCROLL TO THE BOTTOM TO SEE THE START OF THE SCRAPER.
###############################################################################

import scraperwiki
import urlparse
import lxml.html

# scrape_table function: gets passed an individual page to scrape
def scrape_table(root):
    rows = root.cssselect("div#body_right")  # selects all <tr> blocks within <table class="data">
    for row in rows:
        # Set up our data record - we'll need it later
        record = {}
        table_cells = row.cssselect("p")
        if table_cells: 
            record['Quote'] = table_cells[2].text
            # Print out the data we've gathered
            print record, '------------'
            # Finally, save the record to the datastore - 'Artist' is our unique key
            scraperwiki.sqlite.save(["Quote"], record)
        
# scrape_and_look_for_next_link function: calls the scrape_table
# function, then hunts for a 'next' link: if one is found, calls itself again
def scrape_and_look_for_next_link(url):
    html = scraperwiki.scrape(url)
    print html
    root = lxml.html.fromstring(html)
    rows = root.cssselect("div#body_right")  # selects all <tr> blocks within <table class="data">
    for row in rows:
        # Set up our data record - we'll need it later
        scrape_table(root)
        next_link = row.cssselect("a")
        print next_link
        if next_link:
            next_url = urlparse.urljoin(base_url, next_link[1].attrib.get('href'))
            print next_url
            scrape_and_look_for_next_link(next_url)

# ---------------------------------------------------------------------------
# START HERE: define your starting URL - then 
# call a function to scrape the first page in the series.
# ---------------------------------------------------------------------------
base_url = 'http://www.sgi-usa.org/encouragement/index.php/'
starting_url = urlparse.urljoin(base_url, '?')
scrape_and_look_for_next_link(starting_url)
