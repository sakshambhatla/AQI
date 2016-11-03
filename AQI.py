from bs4 import BeautifulSoup
from IPython.display import HTML
import urllib, re
import string

r = urllib.urlopen('http://airnow.gov/index.cfm?action=airnow.local_city&cityid=114').read()
soup = BeautifulSoup(r, "html.parser")

'''
Parse the AirGov website
Return AQI as list
aqiList[0] - AQI value
aqiList[1] - AQI text
aqiList[2] - Additional info
'''
def parseAirGov():
    try:
        #Find the Air Quality Forecast table to the right.
        rightTable = soup.find_all("table", class_="AQData")
        #Narrow down to the Table's summary AQI (Today's High and Tomorrow's High)
        subTable = rightTable[2].find_all("tr")
        #Get table showing Today's AQI
        todayTable = subTable[2].find("table")
        myText= todayTable.getText().encode('utf-8').strip()
    except AttributeError as e:
        print "Error parsing airgov.now. Website layout may have changed.\n" , e
    else:
        #Cleanup text
        aqiList = [s for s in string.split(myText, '\n') if s.strip()]
        del aqiList[0]
        regObj=re.match(r'.*(\d{2,3}).*', aqiList[0])
        aqiList[0] = regObj.group(1)
        return aqiList

myList = parseAirGov()
print myList
