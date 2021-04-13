import pandas as pd
df = pd.read_csv('carrefour_products.csv')
df.drop_duplicates(inplace=True)
df.to_csv('carrefour_products2.csv',index=False)