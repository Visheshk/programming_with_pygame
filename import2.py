from BeautifulSoup import BeautifulStoneSoup
	soup = BeautifulStoneSoup(xml)
	def getValues(name):
		return [child['value'] for child in soup.find('parent', attrs={'name': name}).findAll('child')]

