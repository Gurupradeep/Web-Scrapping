#importing required libraries
import urllib2
from bs4 import BeautifulSoup
import pandas as pd


wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page)

#to get the document structure of a page 
print(soup.prettify())

#getting various elements
print(soup.title)
print(soup.title.string)
print(soup.a)
print(soup.find_all("a"))

#getting all links
all_links = soup.find_all("a")
for link in all_links :
	print link.get("href")

#getting all tables
all_tables = soup.find_all('table')
print(all_tables)

#getting the required tables for capitals and states
capital_table = soup.find_all('table',class_= 'wikitable sortable plainrowheaders')
print(capital_table)
req_rows = capital_table.findAll("tr")
right_table = soup.find('table', {"class" : 'wikitable sortable plainrowheaders'})

#creating lists for storing various attributes
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

#populating lists
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))

#making a dataframe
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
print(df)