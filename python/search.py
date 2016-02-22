from abc import ABCMeta, abstractmethod, abstractproperty

class SearchParam:

	def __init__(self, key, value="", whitespace="%2C+"):
		self._key=key
		self._value=value
		self._whitespace=whitespace

	@property
	def key(self):
		return self._key
	
	@key.setter
	def key(self, value):
		key = value

	@property
	def value(self):
		return self._value
	
	@value.setter
	def value(self, newValue):
		self.value = newValue

	@property
	def whitespace(self):
		return self._whitespace

	@whitespace.setter
	def whitespace(self, value):
		self.whitespace = value

	@property
	def urlForm(self):
		return self.key + "=" + self.value.replace(" ", self.whitespace)
	
	def isSet(self):
		return self.value != ""

class JobSearch:
	__metaclass__ = ABCMeta
	
	@abstractproperty
	def baseUrl(self):
		pass
	
	@abstractproperty
	def paramConnector(self):
		pass

	@abstractproperty
	def paramList(self):
		pass

	@abstractmethod
	def getUrl(self): pass

class BasicJobSearch(JobSearch):

	def __init__(self):
		self._baseUrl = "http://www.indeed.com/jobs?"
		self._paramConnector = "&"
		self._paramList={'what':SearchParam("q"), 'where':SearchParam("l")}

	@property
	def baseUrl(self):
		return self._baseUrl
	
	@property
	def paramConnector(self):
		return self._paramConnector

	@property
	def paramList(self):
		return self._paramList
	
	@paramList.setter
	def paramList(self, paramDict):
		for param, userValue in paramDict.iteritems():
			if param in self.paramList:
				self.paramList[param].value = userValue 
			else:
				raise ValueError("Error: BasicJobSearch does not have a '" + param + "' parameter")
	
	def printUrl(self):
		print self.getUrl()
	
	def getUrl(self):
		url = self.baseUrl	
		count = 1	
		for name, param in self.paramList.iteritems():
			url += param.urlForm

			if count != len(self.paramList):
				url += self.paramConnector
			count += 1

		return url

















