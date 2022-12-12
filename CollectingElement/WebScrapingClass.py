import requests
from bs4 import BeautifulSoup


class Webscrape:
    def __init__(self,name):
        self.Data={}
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            }
        self.search=name
        self.url="https://finance.yahoo.com/quote/"
    def __seturl(self):
        return self.url+"/"+f"{self.search}"+"?"+"p="+f"{self.search}"
    def json_data(self):
        set_url=self.__seturl()
        request_url = requests.request(method="get", url=set_url, headers=self.headers)
        soup = BeautifulSoup(request_url.content, 'lxml')
        NameList = soup.find('div', class_="D(ib) Va(m) Maw(65%) Ov(h)")
        self.Data["Name"]=f"{self.search}"
        PriceText = NameList.find('fin-streamer', class_="Fw(b) Fz(36px) Mb(-4px) D(ib)")
        self.Data["Price"] = PriceText.text
        RegularMarketChange = NameList.find_all('fin-streamer', class_="Fw(500) Pstart(8px) Fz(24px)")
        self.Data["RagularMarketChange"] = RegularMarketChange[0].text
        RegularMarketChangePercent = RegularMarketChange[1].text
        self.Data["RegularMarketChangePercent"] = RegularMarketChangePercent
        Tabel = soup.find_all('tr', class_="Bxz(bb)")
        for tr in Tabel:
            name_td = tr.find_next('td', class_="C($primaryColor) W(51%)").text
            value_td = tr.find_next('td', class_="Ta(end) Fw(600) Lh(14px)").text
            self.Data[f"{name_td}"] = f"{value_td}"
        return self.Data



