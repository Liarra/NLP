class component(object):
	tags=[]
	regexp=""
	
	def __init__(self, name):
		self.name=name;
	
	def __repr__(self):
		return self.name
		
	def parse_from_string(self, string):
		pass
	

class button_press(component):
	tags=["when", "once","as soon as", "press","button"]
	regexp=r"(when|once|as soon as) .* (press|type) ['\"]?(?P<button>.)['\"]?[ ,.]?"
	
	button=''
	
	def __init__(self, string):
		import re
		p=re.compile(self.regexp, re.IGNORECASE)
		string=string.strip()
		string=string.lower()
		
		m = p.search(string)
		if(m==None):
			return
		button=m.group('button')
		
		self.button=button
	
	def __repr__(self):
		return "key[%s]->"%self.button
		
class button_input_component(component):
	pass