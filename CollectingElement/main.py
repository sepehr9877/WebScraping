from pprint import pprint
from WebScrapingClass import Webscrape
webscraping=Webscrape()
data=webscraping.json_data("ETH-USD")
pprint(data)


