import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.yellowpages.com/search?search_terms=pizza&geo_location_terms=Waco%2C+TX")

soup = BeautifulSoup(html.content, "html.parser")

links = soup.find_all("a")

for link in links:
	"""print "<a href='%s'>%s</a>" %(link.get("href"), link.text)"""

g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
	print item.contents[0].text
	print item.contents[1].text
