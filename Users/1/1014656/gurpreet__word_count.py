## GURPREET SINGH
import scraperwiki
from BeautifulSoup import BeautifulSoup
 
def scrape_table(soup):
          #to define coloumns name used in table
          scraperwiki.sqlite.save('data_columns', ['Word', 'Obama','Clinton', 
           'Reagan'])
          table = soup.find("table", {"class": "in-article sortable"})
          #To each row of table is selected
          rows = table.findAll("tr")
          for row in rows:
                 record = {}
                 #To select table row cells
                 table_td = row.findAll("td")
                 #Each row include six cells
                 if len(table_td) == 4:#Cross checking
                         record['Word'] = table_td[0].text
                         record['Obama'] = \
                         table_td[1].text
                         record['Clinton'] = \
                         table_td[2].text
                         record['Reagan'] = \
                         table_td[3].text
                         print record,
                         print "-" * 10
                         #Save data step by step
                         scraperwiki.sqlite.save(["Word"], record)
#website link
Website = 'http://www.guardian.co.uk/news/datablog/2011/may/25/us-presidents-adressing-parliament-obama-clinton-reagan-speech-word-count'
html = scraperwiki.scrape(Website)
soup = BeautifulSoup(html)
scrape_table(soup)
  ## GURPREET SINGH
import scraperwiki
from BeautifulSoup import BeautifulSoup
 
def scrape_table(soup):
          #to define coloumns name used in table
          scraperwiki.sqlite.save('data_columns', ['Word', 'Obama','Clinton', 
           'Reagan'])
          table = soup.find("table", {"class": "in-article sortable"})
          #To each row of table is selected
          rows = table.findAll("tr")
          for row in rows:
                 record = {}
                 #To select table row cells
                 table_td = row.findAll("td")
                 #Each row include six cells
                 if len(table_td) == 4:#Cross checking
                         record['Word'] = table_td[0].text
                         record['Obama'] = \
                         table_td[1].text
                         record['Clinton'] = \
                         table_td[2].text
                         record['Reagan'] = \
                         table_td[3].text
                         print record,
                         print "-" * 10
                         #Save data step by step
                         scraperwiki.sqlite.save(["Word"], record)
#website link
Website = 'http://www.guardian.co.uk/news/datablog/2011/may/25/us-presidents-adressing-parliament-obama-clinton-reagan-speech-word-count'
html = scraperwiki.scrape(Website)
soup = BeautifulSoup(html)
scrape_table(soup)
  