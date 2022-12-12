from pprint import pprint
from WebScrapingClass import Webscrape
webscraping=Webscrape("ETH-USD")
data=webscraping.json_data()
pprint(data)


