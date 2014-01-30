#!/home/poclement/Prog/Perso/RezConso/venv/bin/python
from bs4 import BeautifulSoup
import urllib2
import base64 
from datetime import date
import math
BASE_URL = "http://www2.cooptel.qc.ca/services/temps/?mois={0}&cmd=Visualiser".format(date.today().month)


req = urllib2.Request(BASE_URL)

base64string = base64.encodestring('%s:%s' % ('ets-res2-665','ets665' ))[:-1]
req.add_header("Authorization", "Basic %s" % base64string)


try:
    handle = urllib2.urlopen(req)
except IOError, e:
    # here we shouldn't fail if the username/password is right
    print "It looks like the username or password is wrong."
    sys.exit(1)
thepage = handle.read()

soup = BeautifulSoup(thepage, "lxml")

data_use = float(soup.find_all("tr")[-3].find_all("td")[-1].text)/1024
data_available = float(soup.find_all("tr")[-1].find_all("td")[-1].text)/1024


print int(math.floor(data_use))
