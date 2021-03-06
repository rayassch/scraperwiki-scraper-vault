import scraperwiki
import lxml.html
import json
import urllib



index = 'http://en.wikipedia.org/w/api.php?action=parse&format=json&page=List_of_Occupy_movement_protest_locations_in_California';
print 'Scraping ' + index + '...'
raw_json = scraperwiki.scrape(index)
python_json = json.loads(raw_json)
html = python_json['parse']['text']['*']

print 'Extracting HTML...'
print html

root = lxml.html.fromstring(html)
for tr in root.cssselect("table.wikitable.sortable tr"):
    if(len(tr.cssselect("td")) and tr[0].text_content() != ""):
        print 'Saving data for ' + tr[0].text_content() + '...'
        data = {"city":tr[0].text_content(), "start_date":tr[1].text_content(), "estimated_attendance": tr[2].text_content(), "latitude":'', "longitude":''}
        scraperwiki.sqlite.save(unique_keys=["city"], data=data, table_name="cities")




print 'Geocoding locations...'

locations = scraperwiki.sqlite.select("* from cities where longitude='' order by city")

for location in locations:
    print 'Geocoding ' + location['city'] + '...'
    raw_json = scraperwiki.scrape('http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=' + urllib.quote(location['city'].encode('utf-8')) + ',+CA')
    geo_object = json.loads(raw_json)
    lat = geo_object['results'][0]['geometry']['location']['lat']
    lng = geo_object['results'][0]['geometry']['location']['lng']
    print 'Saving ' + location['city'] + '...'
    scraperwiki.sqlite.execute('update cities set latitude="' + str(lat) + '", longitude="' + str(lng) + '" where city="' + location['city'] + '"')
    scraperwiki.sqlite.commit()



import scraperwiki
import lxml.html
import json
import urllib



index = 'http://en.wikipedia.org/w/api.php?action=parse&format=json&page=List_of_Occupy_movement_protest_locations_in_California';
print 'Scraping ' + index + '...'
raw_json = scraperwiki.scrape(index)
python_json = json.loads(raw_json)
html = python_json['parse']['text']['*']

print 'Extracting HTML...'
print html

root = lxml.html.fromstring(html)
for tr in root.cssselect("table.wikitable.sortable tr"):
    if(len(tr.cssselect("td")) and tr[0].text_content() != ""):
        print 'Saving data for ' + tr[0].text_content() + '...'
        data = {"city":tr[0].text_content(), "start_date":tr[1].text_content(), "estimated_attendance": tr[2].text_content(), "latitude":'', "longitude":''}
        scraperwiki.sqlite.save(unique_keys=["city"], data=data, table_name="cities")




print 'Geocoding locations...'

locations = scraperwiki.sqlite.select("* from cities where longitude='' order by city")

for location in locations:
    print 'Geocoding ' + location['city'] + '...'
    raw_json = scraperwiki.scrape('http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=' + urllib.quote(location['city'].encode('utf-8')) + ',+CA')
    geo_object = json.loads(raw_json)
    lat = geo_object['results'][0]['geometry']['location']['lat']
    lng = geo_object['results'][0]['geometry']['location']['lng']
    print 'Saving ' + location['city'] + '...'
    scraperwiki.sqlite.execute('update cities set latitude="' + str(lat) + '", longitude="' + str(lng) + '" where city="' + location['city'] + '"')
    scraperwiki.sqlite.commit()



