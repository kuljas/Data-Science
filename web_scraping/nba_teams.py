import re
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://en.wikipedia.org/wiki/National_Basketball_Association"
page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
table = soup.find_all('table', class_="wikitable")[0]


#scrap column names:
table_rows = table.find('tr').find_all('th')
column_names = []
for row in table_rows:
    column_names.append(row.text.strip())

#initialize data:
data = {}
for name in column_names:
    data[name]=[]

#scrape division names:
divisions = table.find_all('th', rowspan="5")
for d in divisions:
    division_name = d.text.strip()
    list_of_divisions = [division_name]
    list_of_divisions=list_of_divisions*5
    data["Division"] = data["Division"] + list_of_divisions

#scrape data from rows:
table_rows2 = table.find_all('tr')
for rows in table_rows2:
    ostalo = rows.find_all('td')
    if len(ostalo)==6:
        i=1
        for c in ostalo:
            podatak = c.text.strip()
            data[column_names[i]].append(podatak)
            i=i+1
        data[column_names[i]].append(podatak)
    if len(ostalo)==7:
        i=1
        for c in ostalo:
            podatak = c.text.strip()
            data[column_names[i]].append(podatak)
            i=i+1

df = pd.DataFrame(data=data)
df.to_csv('nba_teams.csv', index = False)