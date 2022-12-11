import requests
from bs4 import BeautifulSoup
headers={ "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
              }
url="https://finance.yahoo.com/crypto/"
request_url=requests.request(method="get",url=url,headers=headers)

soup=BeautifulSoup(request_url.content,'lxml')
NameList=soup.find_all('td',class_="Va(m) Ta(start) Px(10px) Fz(s)")
AllElement=soup.find_all('tr',class_="simpTblRow")[:2]
print(len(AllElement))
for element in AllElement:
    all_els=element.c('td',class_="Va(m) Ta(end) Pstart(20px) Fz(s)")
    for el in all_els:
        print(el.text)
