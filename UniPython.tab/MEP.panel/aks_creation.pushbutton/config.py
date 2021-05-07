
class Configurator():
	"""docstring for Configurator"""

	def __init__(self):
		self._devMode = False 
		self._systemCommon = False
		self._systemPDV = False
		self._FilterByName = False
		self._SystemNameFilter = ""
		self._FilterByNameNotContains = False
		self._SystemNameFilterNotContains = ""

	
	@property
	def devMode(self):
		return self._devMode
	@property
	def systemCommon(self):
		return self._systemCommon
	@property
	def systemPDV(self):
		return self._systemPDV
	@property
	def FilterByName(self):
		return self._FilterByName
	@property
	def SystemNameFilter(self):
		return self._SystemNameFilter
	@property
	def FilterByNameNotContains(self):
		return self._FilterByNameNotContains
	@property
	def SystemNameFilterNotContains(self):
		return self._SystemNameFilterNotContains

	@devMode.setter
	def devMode(self, value):
		self._devMode = value
	@systemCommon.setter
	def systemCommon(self, value):
		self._systemCommon = value
	@systemPDV.setter
	def systemPDV(self, value):
		self._systemPDV = value
	@FilterByName.setter
	def FilterByName(self, value):
		self._FilterByName = value
	@SystemNameFilter.setter
	def SystemNameFilter(self, value):
		self._SystemNameFilter = value
	@FilterByNameNotContains.setter
	def FilterByNameNotContains(self, value):
		self._FilterByNameNotContains = value
	@SystemNameFilterNotContains.setter
	def SystemNameFilterNotContains(self, value):
		self._SystemNameFilterNotContains = value

	def Reset(self):
		self._devMode = False 
		self._systemCommon = False
		self._systemPDV = False
		self._FilterByName = False
		self._SystemNameFilter = ""
		self._FilterByNameNotContains = False
		self._SystemNameFilterNotContains = ""
	
		