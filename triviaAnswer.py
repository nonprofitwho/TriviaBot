from bs4 import BeautifulSoup
import requests
import os
import sys
import time
import json
import urllib
import pycurl

sys.stdout.write(time.strftime("%H:%M:%S") + ' Running Quesiton output code: \n')
response = requests.get('http://finalscoremaryland.com/')
soup = BeautifulSoup(response.content, "lxml")
line = soup.find("div", {"id" : "victory_says"}).p.contents[0].encode('ascii', 'ignore')
question = line.split('A:')[0].strip()

if(len(line.split('A:')) > 1):
	answer = line.split('A:')[1].strip()
	
data = urllib.quote_plus(question + ' A: ' + answer)

c = pycurl.Curl()
c.setopt(pycurl.URL, 'https://api.groupme.com/v3/bots/post?bot_id=&text=' + data + '"')
c.setopt(pycurl.POST, 1)
c.perform()
c.close()
print data
