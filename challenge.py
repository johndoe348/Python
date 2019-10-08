from bs4 import BeautifulSoup
import requests
import re

### challenge 4
# url = "http://pythonchallenge.com/pc/def/linkedlist.php?nothing=8022"

# text = requests.get(url).text

# while 'and the next nothing is' in text:
    
    
#     url = str("http://pythonchallenge.com/pc/def/linkedlist.php?nothing="+ ''.join(re.findall('and the next nothing is ([0-9]+)', text)))
#     print(url)
#     text = requests.get(url).text
#     print(text)

### challenge 5

url = 'http://pythonchallenge.com/pc/def/peak.html'
text = requests.get(url).text



