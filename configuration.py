#@Date 2014/04/02
#@Author Xin Du
#coding:utf-8

__metaclass__ = type 

from xml.etree.ElementTree import ElementTree

class Configuration:
	'''Read Configuration Xml File'''
	def __init__(self, file_name):
		'''initialize file name'''
		self.file_name = file_name
		try:
			tree = ElementTree()
			tree.parse(self.file_name)
			self.root = tree.getroot()
			print tree.getroot()
		except Exception, e:
			print self.file_name + " 无法解析！".decode("utf-8")
			raise e

	def GetCompileUnits(self):
		if self.root != None:
			return self.root.findall("COMPILEUNIT")
		else:
			return []

	def GetCompilePath(self, compile):
		path = compile.find("PATH").text
		print "PATH :" + path
		return path
		
	def GetCompileFileType(self, compile):
		file_type = compile.find("FILETYPE").text
		print "FILETYPE :" + file_type
		return file_type

	def GetCompileOutputPath(self, compile):
		output = compile.find("OUTPUTPATH").text
		print "OUTPUTPATH :" + output
		return output

	def GetCompileOutputName(self, compile):
		output = compile.find("OUTPUTNAME").text
		print "OUTPUTNAME :" + output
		return output

	def GetCompileUsername(self, compile):
		output = compile.find("USERNAME").text
		print "USERNAME :" + output
		return output

	def GetCompilePassword(self, compile):
		output = compile.find("PASSWORD").text
		print "PASSWORD :" + output
		return output

def test():
	try:
		config = Configuration("C:\\Users\\bestpay\\Desktop\\configuration.xml")
	except Exception:
		config = None

	if config != None:
		for unit in config.GetCompileUnits():
			config.GetCompilePath(unit)
			config.GetCompileFileType(unit)
			config.GetCompileOutput(unit)
			config.GetCompileOutputPath(unit)
			config.GetCompileOutputName(unit)
			config.GetCompileUsername(unit)
			config.GetCompilePassword(unit)

test()