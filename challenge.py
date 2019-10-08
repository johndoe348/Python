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

# import pickle

# #url = 'http://pythonchallenge.com/pc/def/peak.html'
# url = 'http://pythonchallenge.com/pc/def/banner.p'

# text = pickle.loads(requests.get(url).content)
# print(text)
# for x in text:
#     print(''.join([k*v for k, v in x]))
#     # this doesn't work because every iteration of a [(' ', 3), ('#', 3)], it prints each tuple in sequence, 
#     # as opposed to adding all the tuples within the list together before printing
#     # for k, v in x:
#     #     print(''.join([k * v])


### challenge 6

url = 'http://pythonchallenge.com/pc/def/channel.html'

text = requests.get(url).content
print(text)





