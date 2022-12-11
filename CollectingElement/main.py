from pprint import pprint
import asyncio
from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser
import requests
from time import sleep
async def send_request(url):
    headers={ "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
              }
    request_url=requests.request(method="get",url=url)
    return request_url
async def getelements():
    get_request=await send_request("https://www.coindesk.com/price/bitcoin/")
    soup=BeautifulSoup(get_request.content,'lxml')
    div_elements=soup.find_all('div',class_="Box-sc-1hpkeeg-0 eQeCqF")
    price=[]
    for element in div_elements:
        element_name=soup.find('div',class_="Box-sc-1hpkeeg-0 iHOgZm")
        print("elementName")
        print(element_name.text)
        element_price=element.findNext('div',class_="Box-sc-1hpkeeg-0 jwYVXk")
        el=element_price.find('span',class_="currency-pricestyles__Price-sc-1rux8hj-0 jIzQOt")
        print("elementPrice")
        print(el.text)
        whole_element_24h=element.findNext('div',class_="Box-sc-1hpkeeg-0 bDRvIB")
        element_24h=whole_element_24h.findNext('div',class_="Box-sc-1hpkeeg-0 keDxjI")
        print("24%")
        print(element_24h.text)
        whole_element_24Percent=element.find_all_next('div', class_="Box-sc-1hpkeeg-0 gRAZAN")
        low24_element=whole_element_24Percent[0].findNext('div', class_="Box-sc-1hpkeeg-0 keDxjI")
        print("low")
        print(low24_element.text)
        high24_element=whole_element_24Percent[1].findNext('div',class_="Box-sc-1hpkeeg-0 keDxjI")
        print("high")
        print(high24_element.text)

asyncio.run(getelements())
