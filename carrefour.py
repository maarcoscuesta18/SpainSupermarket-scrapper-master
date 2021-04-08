from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
eanCodeLists = []
for i in range(24835):
    eanCodeLists.append(str(i))

productsinfo=[]
productsprice=[]
productspriceperkg=[]
productslinks=[]

for i in range(len(eanCodeLists)):
    urlopen = requests.get('https://www.carrefour.es/supermercado/c?No='+str(eanCodeLists[i])+'').text
    soup = bs(urlopen,'html.parser')
    
    ProductInfo = soup.find("p", {"class": "title-product"}).text # .text will give us the text underlying that HTML element
    productsinfo.append(str(ProductInfo).strip())
    
    ProductLink = soup.find("a",{"class": "js-gap-product-click-super"})['href']
    productslinks.append("www.carrefour.es"+ProductLink.strip())
         
    ProductPrice = soup.find("span", {"class": "price"}).text  # .text will give us the text underlying that HTML element
    buggy_name = str(ProductPrice).rstrip(ProductPrice[-1])
    inner_text = float(buggy_name.replace(',','.'))
    productsprice.append(float(str(inner_text).strip()))
    
    ProductPricePerKg = soup.find("p", {"class": "format-price"}).text# .text will give us the text underlying that HTML element
    productspriceperkg.append(str(ProductPricePerKg).strip())  

productsinfoResult=[]
for item in productsinfo:
    if item not in productsinfoResult:
        productsinfoResult.append(item)

productspriceResult=[]
for item in productsprice:
    if item not in productspriceResult:
        productspriceResult.append(item)

productslinkResult=[]       
for item in productslinks:
    if item not in productslinkResult:
        productslinkResult.append(item)

productsPricePerKgResult=[]
for item in productspriceperkg:
    if item not in productsPricePerKgResult:
        productsPricePerKgResult.append(item)
        
table_dict = {'id':'','product_name': productsinfoResult, 'link':productslinkResult,'price':productspriceResult,'price_per_kg': productsPricePerKgResult}
df = pd.DataFrame(table_dict)

df.to_csv('carrefour_products.csv',index=False)
