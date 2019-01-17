from requests import get
import sys
from bs4 import BeautifulSoup

#URL TWITTER
url = 'https://twitter.com/{0}'.format(sys.argv[1])

response = get(url)

soup = BeautifulSoup(response.text, 'html.parser')

followers= soup.findAll('span','ProfileNav-value')

if followers:
    print(followers[2].string)
else : 
    print('No result for this page')