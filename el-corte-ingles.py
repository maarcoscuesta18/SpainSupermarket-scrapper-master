from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re
eanCodeLists = []
for i in range(1):
    eanCodeLists.append(str(i+1))
productsinfo=[]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "es-ES,en;q=0.5","Accept-Encoding": "gzip, deflate"}

for items in eanCodeLists:
    urlopen = requests.get('https://www.elcorteingles.es/supermercado/buscar/'+str(1)+'/',headers=headers).text
    soup = bs(urlopen,'html.parser')
    print(soup)
    container = soup.find_all("div",{"class":"c12 js-grid-container"})
    print(container)
    for i in container:
        title = i.find("a", {"class":"event js-product-link"}).get_text(strip=True)
        print(title)

