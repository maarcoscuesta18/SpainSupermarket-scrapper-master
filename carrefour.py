from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import threading
import csv
def search_products(inicio,final):
    eanCodeLists = []
    for i in range(inicio,final):
        eanCodeLists.append(str(i))

    productsinfo=[]
    productsprice=[]
    productspriceperkg=[] 
    productslinks=[]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "es-ES,es;q=0.5","Accept-Encoding": "gzip, deflate"}

    for i in range(len(eanCodeLists)):  
        urlopen = requests.get('https://www.carrefour.es/supermercado/c?No='+str(eanCodeLists[i])+'').text
        soup = bs(urlopen,'html.parser')
        ProductInfo = soup.find("p", {"class": "title-product"}).text # .text will give us the text underlying that HTML element
        productsinfo.append(str(ProductInfo).strip())
        
        ProductLink = soup.find("a",{"class": "js-gap-product-click-super"})['href']
        productslinks.append("www.carrefour.es"+ProductLink.strip())
            
        try:
            ProductPrice = soup.find("span", {"class": "price"}).text  # .text will give us the text underlying that HTML element
            buggy_name = str(ProductPrice).rstrip(ProductPrice[-1])
            inner_text = float(buggy_name.replace(',','.'))
            productsprice.append(float(str(inner_text).strip()))
        except:
            ProductPrice2 = soup.find("span", {"class": "strike-price"}).text  # .text will give us the text underlying that HTML element
            buggy_name2 = str(ProductPrice2).rstrip(ProductPrice2[-1])
            inner_text2 = float(buggy_name2.replace(',','.'))
            productsprice.append(float(str(inner_text2).strip()))

        ProductPricePerKg = soup.find("p", {"class": "format-price"}).text# .text will give us the text underlying that HTML element
        productspriceperkg.append(ProductPricePerKg.strip())  
        
        print("Product Nº: ",eanCodeLists[i], " -->\t Name: ",productsinfo[i],"\t Link: ",productslinks[i],"\t Price: ",productsprice[i],"\t Price Per Kg/L/Ud: ",productspriceperkg[i])
        
    
    table_dict = {'id':'','product_name': productsinfo, 'link':productslinks,'price':productsprice,'price_per_kg': productspriceperkg}
    df = pd.DataFrame(table_dict)
    df.to_csv('carrefour_products.csv',mode='a',index=False)

threads = list()
t = threading.Thread(target=search_products,args=(0,1000))
threads.append(t)
t.start()
t = threading.Thread(target=search_products,args=(1001,2000))
threads.append(t)
t.start()
t = threading.Thread(target=search_products,args=(2001,3000))
threads.append(t)
t.start()
t = threading.Thread(target=search_products,args=(3001,4000))
threads.append(t)
t.start()
t = threading.Thread(target=search_products,args=(4001,5000))
threads.append(t)
t.start()
t = threading.Thread(target=search_products,args=(5001,6000))
threads.append(t)
t.start()
t = threading.Thread(target=search_products,args=(6001,7000))
threads.append(t)
t.start()
t = threading.Thread(target=search_products,args=(7001,8000))
threads.append(t)
t.start()
t = threading.Thread(target=search_products,args=(8001,9000))
threads.append(t)
t.start()