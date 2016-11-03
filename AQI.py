from bs4 import BeautifulSoup
from IPython.display import HTML
import urllib, re
r = urllib.urlopen('http://airnow.gov/index.cfm?action=airnow.local_city&cityid=114').read()
soup = BeautifulSoup(r, "html.parser")

#Find the Air Quality Forecast table to the right.
letters = soup.find_all("table", class_="AQData")
#Narrow down to the Table's summary AQI (Today's High and Tomorrow's High)
temp2 = letters[2].find_all("tr")
#Get table showing Today's AQI
temp3 = temp2[2].find("table")
myText= temp3.getText().encode('utf-8').strip()
print myText
