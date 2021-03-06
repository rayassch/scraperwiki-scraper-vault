# All UK Towns and Cities and their coordinates
# Based on a scraper written by Ross Jones

# Town and City names scraped from Wikipedia:
# http://en.wikipedia.org/wiki/List_of_towns_in_the_United_Kingdom
# http://en.wikipedia.org/wiki/List_of_cities_in_the_United_Kingdom
# Towns and Cities geolocated by the Geonames API

import scraperwiki
import lxml.html
from urllib import urlencode
import json
import re


# helper functions

def get_html(title):
    raw_json = scraperwiki.scrape("http://en.wikipedia.org/w/api.php?action=parse&format=json&page=" + title)
    html = json.loads(raw_json)['parse']['text']['*']
    return html

def geocode_location(name):
    u = urlencode({ 'username':'scraperwiki', 'maxRows':1, 'country': 'gb', 'q': name })
    result = scraperwiki.scrape( "http://api.geonames.org/search?" + u )
    page = lxml.html.fromstring( result )
    return [page.cssselect('lat')[0].text_content(), page.cssselect('lng')[0].text_content()]


def scrape_locations():

    locations = []
    cities = [] # we keep a note of cities, to avoid duplicates from the towns pages (stupid Wikipedia)
    
    print 'Scraping cities...'
    
    cities_html = lxml.html.fromstring(get_html('List_of_cities_in_the_United_Kingdom'))
    for table in cities_html.cssselect("table.wikitable.sortable"):
        country = table.getprevious().cssselect('.mw-headline')[0].text
        print '-- scraping cities in ' + country + '...'
        for tr in table.cssselect('tr'):
            if(len(tr.cssselect("td"))):
                name = tr.cssselect('td a')[0].text
                cities.append(name)
                locations.append({'name': name, 'country': country, 'type': 'city'})
    
    
    print 'Scraping towns...'
    
    print '-- scraping towns in England...'
    
    towns_html = lxml.html.fromstring(get_html('List_of_towns_in_England'))
    for table in towns_html.cssselect("table.wikitable.sortable"):    
        for tr in table.cssselect('tr'):
            if(len(tr.cssselect("td"))):
                name = tr.cssselect('td a')[0].text
                if name not in cities:
                    locations.append({'name': name, 'country': 'England', 'type': 'town'})
    
    print '-- scraping towns in Scotland...'
    
    towns_html = lxml.html.fromstring(get_html('List_of_burghs_in_Scotland'))
    for table in towns_html.cssselect("table.wikitable"):
        for tr in table.cssselect('tr'):
            if(len(tr.cssselect("td"))):
                name = tr.cssselect('td a')[0].text
                if name not in cities:
                    locations.append({'name': name, 'country': 'Scotland', 'type': 'town'})
    
    print '-- scraping towns in Wales...'
    
    towns_html = lxml.html.fromstring(get_html('List_of_towns_in_Wales'))
    for h2 in towns_html.cssselect("h2"):
        if not h2.text_content().endswith('See also'):
            for a in h2.getnext().cssselect('a'):
                name = a.text
                if name not in cities:
                    locations.append({'name': name, 'country': 'Wales', 'type': 'town'})
    
    print '-- scraping towns in Northern Ireland...'
    
    towns_html = lxml.html.fromstring(get_html('List_of_towns_and_villages_in_Northern_Ireland'))
    for h2 in towns_html.cssselect("h2"):
        if not h2.text_content().endswith('See also'):
            for a in h2.getnext().cssselect('b a'):
                name = a.text
                if name not in cities:
                    locations.append({'name': name, 'country': 'Northern Ireland', 'type': 'town'})
    
    print 'Saving towns and cities...'
    
    print locations
    
    scraperwiki.sqlite.save(['name','country'], locations, 'towns_and_cities')

    print 'Done!'
    


def geocode_locations():
    
    try:
        locations = scraperwiki.sqlite.select('* from towns_and_cities where lat is null order by name')
    except:
        locations = scraperwiki.sqlite.select('* from towns_and_cities order by name')

    print 'Geocoding ' + str(len(locations)) + ' locations...'

    geocoded = []
    for location in locations:
        temp = location
        try:
            latlng = geocode_location(location['name'])
            temp['lat'] = float(latlng[0])
            temp['lng'] = float(latlng[1])
        except:
            if re.search('and', location['name']) or re.search('&', location['name']):
                print '-- Could not geocode ' + location['name'] + '. Trying ' + location['name'].split(' ')[0] + '...'
                try:
                    latlng = geocode_location(location['name'].split(' ')[0])
                    temp['lat'] = float(latlng[0])
                    temp['lng'] = float(latlng[1])
                except:
                    print '-- Could not geocode ' + location['name'].split(' ')[0]
            else:
                print '-- Could not geocode ' + location['name']

        geocoded.append(temp)

    print 'Saving geocoded locations...'

    print geocoded

    scraperwiki.sqlite.save(['name','country'], geocoded, 'towns_and_cities')

    print 'Done!'


#scrape_locations()
#geocode_locations()



# All UK Towns and Cities and their coordinates
# Based on a scraper written by Ross Jones

# Town and City names scraped from Wikipedia:
# http://en.wikipedia.org/wiki/List_of_towns_in_the_United_Kingdom
# http://en.wikipedia.org/wiki/List_of_cities_in_the_United_Kingdom
# Towns and Cities geolocated by the Geonames API

import scraperwiki
import lxml.html
from urllib import urlencode
import json
import re


# helper functions

def get_html(title):
    raw_json = scraperwiki.scrape("http://en.wikipedia.org/w/api.php?action=parse&format=json&page=" + title)
    html = json.loads(raw_json)['parse']['text']['*']
    return html

def geocode_location(name):
    u = urlencode({ 'username':'scraperwiki', 'maxRows':1, 'country': 'gb', 'q': name })
    result = scraperwiki.scrape( "http://api.geonames.org/search?" + u )
    page = lxml.html.fromstring( result )
    return [page.cssselect('lat')[0].text_content(), page.cssselect('lng')[0].text_content()]


def scrape_locations():

    locations = []
    cities = [] # we keep a note of cities, to avoid duplicates from the towns pages (stupid Wikipedia)
    
    print 'Scraping cities...'
    
    cities_html = lxml.html.fromstring(get_html('List_of_cities_in_the_United_Kingdom'))
    for table in cities_html.cssselect("table.wikitable.sortable"):
        country = table.getprevious().cssselect('.mw-headline')[0].text
        print '-- scraping cities in ' + country + '...'
        for tr in table.cssselect('tr'):
            if(len(tr.cssselect("td"))):
                name = tr.cssselect('td a')[0].text
                cities.append(name)
                locations.append({'name': name, 'country': country, 'type': 'city'})
    
    
    print 'Scraping towns...'
    
    print '-- scraping towns in England...'
    
    towns_html = lxml.html.fromstring(get_html('List_of_towns_in_England'))
    for table in towns_html.cssselect("table.wikitable.sortable"):    
        for tr in table.cssselect('tr'):
            if(len(tr.cssselect("td"))):
                name = tr.cssselect('td a')[0].text
                if name not in cities:
                    locations.append({'name': name, 'country': 'England', 'type': 'town'})
    
    print '-- scraping towns in Scotland...'
    
    towns_html = lxml.html.fromstring(get_html('List_of_burghs_in_Scotland'))
    for table in towns_html.cssselect("table.wikitable"):
        for tr in table.cssselect('tr'):
            if(len(tr.cssselect("td"))):
                name = tr.cssselect('td a')[0].text
                if name not in cities:
                    locations.append({'name': name, 'country': 'Scotland', 'type': 'town'})
    
    print '-- scraping towns in Wales...'
    
    towns_html = lxml.html.fromstring(get_html('List_of_towns_in_Wales'))
    for h2 in towns_html.cssselect("h2"):
        if not h2.text_content().endswith('See also'):
            for a in h2.getnext().cssselect('a'):
                name = a.text
                if name not in cities:
                    locations.append({'name': name, 'country': 'Wales', 'type': 'town'})
    
    print '-- scraping towns in Northern Ireland...'
    
    towns_html = lxml.html.fromstring(get_html('List_of_towns_and_villages_in_Northern_Ireland'))
    for h2 in towns_html.cssselect("h2"):
        if not h2.text_content().endswith('See also'):
            for a in h2.getnext().cssselect('b a'):
                name = a.text
                if name not in cities:
                    locations.append({'name': name, 'country': 'Northern Ireland', 'type': 'town'})
    
    print 'Saving towns and cities...'
    
    print locations
    
    scraperwiki.sqlite.save(['name','country'], locations, 'towns_and_cities')

    print 'Done!'
    


def geocode_locations():
    
    try:
        locations = scraperwiki.sqlite.select('* from towns_and_cities where lat is null order by name')
    except:
        locations = scraperwiki.sqlite.select('* from towns_and_cities order by name')

    print 'Geocoding ' + str(len(locations)) + ' locations...'

    geocoded = []
    for location in locations:
        temp = location
        try:
            latlng = geocode_location(location['name'])
            temp['lat'] = float(latlng[0])
            temp['lng'] = float(latlng[1])
        except:
            if re.search('and', location['name']) or re.search('&', location['name']):
                print '-- Could not geocode ' + location['name'] + '. Trying ' + location['name'].split(' ')[0] + '...'
                try:
                    latlng = geocode_location(location['name'].split(' ')[0])
                    temp['lat'] = float(latlng[0])
                    temp['lng'] = float(latlng[1])
                except:
                    print '-- Could not geocode ' + location['name'].split(' ')[0]
            else:
                print '-- Could not geocode ' + location['name']

        geocoded.append(temp)

    print 'Saving geocoded locations...'

    print geocoded

    scraperwiki.sqlite.save(['name','country'], geocoded, 'towns_and_cities')

    print 'Done!'


scrape_locations()
#geocode_locations()



