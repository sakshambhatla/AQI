from bs4 import BeautifulSoup
from IPython.display import HTML
import urllib, re
r = urllib.urlopen('http://airnow.gov/index.cfm?action=airnow.local_city&cityid=114').read()
soup = BeautifulSoup(r, "html.parser")
#print type(soup)
#print soup.prettify()[41900:42800]
#letters = soup.find_all("table", class_="AQData")
#regExp = re.compile('AIQ')
#letters = soup.find_all("td", attrs={'class' : 'AQDataSectionTitle'}, text=regExp)
#Find the Air Quality Forecast table to the right.
letters = soup.find_all("table", class_="AQData")
#print letters[2]
#Narrow down to the Table's summary AQI (Today's High and Tomorrow's High)
temp2 = letters[2].find_all("tr")
#print temp2[2]
#Get table showing Today's AQI
temp3 = temp2[2].find("table")
#print temp3
myText= temp3.getText().encode('utf-8').strip()
print myText
#letters[3] has
#print letters


#print str(ans[7])
#matchObj = re.match( '.*([0-9][0-9]).*', str(ans[7]), re.I)
#print matchObj[1]
#print letters[2].renderContents()
#regExp = str(letters[2].getText())
#print regExp.split()
#print [int(s) for s in regExp.split() if s.isdigit()]
#matchObj = re.match( '.*Ozone.*([0-9][0-9]).*', str(regExp), re.M|re.I)
#print type(letters)
#print letters[2]
#HTML('<iframe src=http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts width=700 height=500></iframe>')
#matchObj = re.match( '.*Ozone.*([0-9][0-9]).*', letters[2].getText(), re.M|re.I)
#print "regex is - ", matchObj.group(1)
