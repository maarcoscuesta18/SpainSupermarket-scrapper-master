from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
eanCodeLists = []
for i in range(296):
    eanCodeLists.append(str(i))

productsinfo=[]
productsprice=[]
productspriceperkg=[]
productslinks=[]

for items in eanCodeLists:
    urlopen = requests.get('https://www.dia.es/compra-online/productos/c/WEB.000.000.00000?page='+str(items)+'&disp=').text
    soup = bs(urlopen,'html.parser')
    
    ProductInfo = soup.find_all("span", {"class": "details"}) # .text will give us the text underlying that HTML element
    for td in ProductInfo:
        inner_text = td.text
        strings = inner_text.split("\r\n\t\t\t\t")
        productsinfo.append(str(inner_text).strip())
       
    ProductLink = soup.find_all("a",{"class": "productMainLink"})
    for link in ProductLink:
        productslinks.append("www.dia.es"+link.get('href'))
         
    ProductPrice = soup.findAll("p", {"class": "price"})  # .text will give us the text underlying that HTML element
    for td in ProductPrice:
        inner_text = td.text
        #strings = inner_text.split("\r\n\t\t\t\t")
        buggy_name = str(inner_text).rstrip(inner_text[-1])
        productsprice.append(str(buggy_name).strip())  
    
    ProductPricePerKg = soup.findAll("p", {"class": "pricePerKilogram"})# .text will give us the text underlying that HTML element
    for td in ProductPricePerKg:
        inner_text = td.text
        #strings = inner_text.split("\r\n\t\t\t\t")
        productspriceperkg.append(str(inner_text).strip())  
    
products=[productsinfo,productsprice,productspriceperkg]

coma= []
coma.append(",")
table_dict = {'id':coma[0],'product_name': productsinfo, 'link':productslinks,'price':productsprice,'price_per_kg': productspriceperkg}
df = pd.DataFrame(table_dict)

df.to_csv('dia_products.csv',index=False)
