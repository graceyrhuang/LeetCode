import re
from collections import defaultdict

def checkMensionStatistics(messages):
	counter = defaultdict(int)

	isId = lambda x : (x[:2] == 'id' and x[2:].isdigit())

	def findId(idInfo):
		if isId(idInfo):		# only one id
			counter[idInfo] += 1 

		elif ',' in idInfo: # more than one id
			ids = idInfo.split(',')
			# print(ids)
			for Id in ids:
				if isId(Id):
					counter[Id] += 1
				else:
					break


	for message in messages:
		idInfos = message.split('@')
		for idInfo in idInfos:
			if idInfo[:2] == 'id':
				# idInfo = '@' + idInfo
				findId(idInfo)

	keys = sorted(counter.keys())

	return [f'{key} : {counter[key]}' for key in keys]

mess = ["hey, @id345,id563,id657, are you gonne ,id345, @id345"]
print(checkMensionStatistics(mess))