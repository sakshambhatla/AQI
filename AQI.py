from bs4 import BeautifulSoup
from IPython.display import HTML
import urllib, re
r = urllib.urlopen('http://airnow.gov/index.cfm?action=airnow.local_city&cityid=114').read()
soup = BeautifulSoup(r, "html.parser")

def parseAirGov():
    #Find the Air Quality Forecast table to the right.
    try:
        rightTable = soup.find_all("table", class_="AQData")
        #Narrow down to the Table's summary AQI (Today's High and Tomorrow's High)
        subTable = rightTable[2].find_all("tr")
        #Get table showing Today's AQI
        todayTable = subTable[0].find("table")
        myText= todayTable.getText().encode('utf-8').strip()
    except AttributeError as e:
        print "Error parsing airgov.now. Website layout may have changed.\n" , e
    else:
        return myText

myText = parseAirGov()
print myText
