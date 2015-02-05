from component import component

class say_command(component):
	tags=["say", "tell", "ask"]
	regexp=r"(say|tell|ask)s? ['\"](?P<what>.+)['\"]"
	
	say_what=""
	
	def __init__(self, string):
		import re
		p=re.compile(self.regexp, re.IGNORECASE)
		string=string.strip()
		string=string.lower()
		
		m = p.search(string)
		if(m==None):
			return
		self.say_what=m.group('what').replace(' ','_')
	
	def __repr__(self):
		return "say(%s)"%self.say_what
		
		
class wait_command(component):
	tags=["wait"]
	regexp=r"waits? .* (?P<number>\d{1,3}) (?P<units>second|minute|ms|sec|min|millisecond)s?"
	
	ms=0
	
	def __init__(self, string):
		import re
		p=re.compile(self.regexp, re.IGNORECASE)
		string=string.strip()
		string=string.lower()
		
		m = p.search(string)
		if(m==None):
			return
		number=m.group('number')
		units=m.group('units')
		
		number_ms=0
		if units in ["second","sec"]:
			number_ms=int(number)*1000
		elif units in ["minute","min"]:
			number_ms=int(number)*60000
		#Assuming it's in milliseconds
		else:
			number_ms=int(number)
		
		self.ms=number_ms
	
	def __repr__(self):
		return "wait(%d)"%self.ms