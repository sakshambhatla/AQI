from bs4 import BeautifulSoup
from IPython.display import HTML
import urllib, re
import string

class parseAirGov:
    def __init__(self):
        r = urllib.urlopen('http://airnow.gov/index.cfm?action=airnow.local_city&cityid=114').read()
        self.soup = BeautifulSoup(r, "html.parser")

    def getToday(self):
        '''
        Parse the AirGov website
        Return AQI as list of [AQI value, AQI text, Additional info]
        '''
        try:
            #Find the Air Quality Forecast table to the right.
            rightTable = self.soup.find_all("table", class_="AQData")
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

obj1 = parseAirGov()
myList = obj1.getToday()
print myList
