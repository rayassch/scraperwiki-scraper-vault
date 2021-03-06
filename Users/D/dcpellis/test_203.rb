# Blank Ruby

puts "Hello, coding in the cloud!"

html = ScraperWiki.scrape("http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm")

require 'nokogiri'

doc = Nokogiri::HTML(html)
for v in doc.search("div[@align='left'] tr.tcont")
  cells = v.search('td')
  data = {
    'country' => cells[0].inner_html,
    'years_in_school' => cells[4].inner_html.to_i
  }
  puts data.to_json
end

ScraperWiki.save_sqlite(unique_keys=['country'], data=data)# Blank Ruby

puts "Hello, coding in the cloud!"

html = ScraperWiki.scrape("http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm")

require 'nokogiri'

doc = Nokogiri::HTML(html)
for v in doc.search("div[@align='left'] tr.tcont")
  cells = v.search('td')
  data = {
    'country' => cells[0].inner_html,
    'years_in_school' => cells[4].inner_html.to_i
  }
  puts data.to_json
end

ScraperWiki.save_sqlite(unique_keys=['country'], data=data)