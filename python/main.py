from search import BasicJobSearch
from page import Page

mySearch = BasicJobSearch()

myParams = {'what':"computer programmer",'where':"Waco TX"}
mySearch.paramList = myParams

resultsPage = Page(mySearch.getUrl())
resultsPage = resultsPage.getHtml()

get_jobs = resultsPage.find_all("a", {"data-tn-element": "jobTitle"})

for job in get_jobs:
	print job.text
