import requests, pandas as pd
from bs4 import BeautifulSoup
URL='https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches'
html=requests.get(URL,timeout=30,headers={'User-Agent':'Mozilla/5.0'}).text
soup=BeautifulSoup(html,'html.parser')
tables=pd.read_html(str(soup))
# Select the launch-history table(s), normalize columns, and export.
for i,t in enumerate(tables):
    if any('Flight No.' in str(c) or 'Date' == str(c) for c in t.columns):
        t.to_csv(f'../data/wiki_launch_table_{i}.csv',index=False)
