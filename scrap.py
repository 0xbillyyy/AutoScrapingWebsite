#python2
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

print """

Simple Auto Scraping Website

How to use?
1. Enter the link using http or https
2. Enter the html tags you are looking for (html, body, p, div, a, etc)
3. Enter the html attributes you are looking for (class, id, align, etc.)
4. enter the value of the html attribute you are looking for (mt-6 content, content, paragraph, etc)

Requires the command pip install requests, pip install bs4, pip install useragent

"""

link = raw_input("URL: ")
tag = raw_input("Tag: ")
attribute_name = raw_input("Attribute name: ")
attribute_value = raw_input("Attribute value: ")
ua = UserAgent().random
url = requests.get(link, headers={"User-Agent":ua})
bs = BeautifulSoup(url.text,'html.parser')
find = bs.find_all(tag,{attribute_name: attribute_value})

print("\033[92mResponse code: "+ str(url.status_code)+"\033[39m")
print("\033[36mUser Agent: "+ua)
print("\033[34mResult:")
for text in find:
	print(text.get_text())
print("\033[39m")
