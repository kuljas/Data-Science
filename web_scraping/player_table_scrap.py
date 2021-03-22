import re
import pandas as pd
import mechanicalsoup

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.nba.com/players"
page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
table = soup.find_all('table', class_="players-list")[0]

table_rows = table.find('tr').find_all('th')
column_names = []
for row in table_rows:
    column_names.append(row.text.strip())

data = {}
for name in column_names:
    data[name]=[]

table_body = table.find('tbody')
for rows in table_body.find_all('tr'):
    i=0
    for c in rows.find_all('td'):
        podatak = c.text.strip()
        data[column_names[i]].append(podatak)
        i=i+1

df = pd.DataFrame(data=data)

print(df)