import json

class Controller:

	curObj = 0
	countObj = 0
	json_data = ""
	
	def __init__(self):
		# ------- Json loading -------
		f = open('cgi-bin/data.json')
		json_file = f.read()
		f.close()

		try:
			self.json_data = json.loads(json_file)
		except ValueError:
			self.json_data = ''
			#print ('Json SyntaxError !')

		self.countObj = len(self.json_data)
		#print(countObj)
		
	def jsonStatus(self):
		if self.json_data=="":
			return False;
		else:
			return True;
			
	def getTitle(self, numObj):
		return self.json_data[numObj]['title']
		
	def getName(self, numObj):
		return self.json_data[numObj]['name']

	def getMessage(self, numObj):
		return self.json_data[numObj]['message']
		
	def getCountObj(self):
		return self.countObj
	
	def setTitle(self, numObj, newTitle):
		self.json_data[numObj]['title'] = newTitle
	
	def setName(self, numObj, newName):
		self.json_data[numObj]['name'] = newName
	
	def setMessage(self, numObj, newMessage):
		self.json_data[numObj]['message'] = newMessage
		
	def saveData(self):
		json_str = json.dumps(self.json_data)
		with open('cgi-bin/data.json', 'w') as outfile:
			outfile.write(json_str)
