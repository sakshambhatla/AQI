from bs4 import BeautifulSoup
from IPython.display import HTML
import urllib, re
r = urllib.urlopen('http://airnow.gov/index.cfm?action=airnow.local_city&cityid=114').read()
soup = BeautifulSoup(r, "html.parser")
print type(soup)
#print soup.prettify()[41900:42800]
#letters = soup.find_all("table", class_="AQData")
#regExp = re.compile('AIQ')
#letters = soup.find_all("td", attrs={'class' : 'AQDataSectionTitle'}, text=regExp)
letters = soup.find_all("td", class_="AQDataSectionTitle")
temp=letters[2].find_all("td", attrs={'background':None})
print letters
'''ans = temp[7].find_all("td", attrs={'align':'center'})
for line in ans:
    print str(line.getText()).strip()
    #print [int(s) for s in str(line.getText()).strip() if s.is()]
    print "........."'''
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
