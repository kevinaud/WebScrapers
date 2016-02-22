import requests
from bs4 import BeautifulSoup

class Page:

	def __init__(self, url):
		self.url = url
		rawHtml = requests.get(self.url)
		self.html = BeautifulSoup(rawHtml.content, "html.parser")

	def getHtml(self):
		return self.html
