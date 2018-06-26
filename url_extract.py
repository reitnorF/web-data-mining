from urlparse import urlparse
import operator

#Input 	: Raw URL
#Output	: Domain Name of URL
def extractDomainURL(url):
	parsed_uri = urlparse(url)
	return '{uri.netloc}'.format(uri=parsed_uri)
	
#Input	: Domain Name of URL
#Output	: True if valid. False if possibly spam node.
def heuristicChecker(url):
	#Remove All bp.blogspot.com
	if ( "bp.blogspot.com" in url):
		return False
	#Remove ad.doubleclick.net ads
	elif ("ad.doubleclick.net" in url):
		return False
	else:
		return True	
	
isL = 0
coldStart = 0
currentDomain = "lol"
setOfLink = set()
nodeDict = dict()
inDegree = dict()

with open('ccc.txt') as f:
	for line in f:
		if (line[0] == 'P'):
			splitted = line.split()
			try:
				#domain = extractDomainURL(splitted[1])
				domain = splitted[1]
				#print ' '
				#print 'P ' + domain
				currentDomain = domain
				setOfLink.clear()
				if (currentDomain not in nodeDict):
					nodeDict[currentDomain] = set()
				coldStart = 1
				if (currentDomain not in inDegree):
					inDegree[currentDomain] = set()
			except:
				pass
			
			
		elif (line[0] == 'L'):
			if (coldStart == 1):
				splitted = line.split()
				try:
					#domain = extractDomainURL(splitted[1])
					domain = splitted[1]
					if (heuristicChecker(domain)):
						if (domain != currentDomain):						
							if ((domain not in setOfLink)):
								setOfLink.add(domain)
								#print 'L ' + domain
								nodeDict[currentDomain] = setOfLink.union(nodeDict[currentDomain])
								if (domain not in inDegree):
									inDegree[domain] = set()
								else:
									inDegree[domain].add(currentDomain)
					isL = 1
				except:
					pass
			

'''
for key,value in nodeDict.iteritems():
	print ' '
	print 'P ' + key
	for n in value:
		print 'L ' + n
'''

inDegreeQty = dict()
	
for key,value in inDegree.iteritems():
	#print ' '
	print 'P ' + key
	inDegreeQty[key] = len(value)
	for n in value:
		print 'L ' + n



#bla = sorted(inDegreeQty.items(), key=lambda x:x[1], reverse=True)

#for key,value in bla:
	#print key +" : "+ str(value)
	#for n in inDegree[key]:
		#print ' ' + n
