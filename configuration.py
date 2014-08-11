#@Date 2014/04/02
#@Author Xin Du
#coding: utf-8

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
		except Exception, e:
			print self.file_name + "无法解析".decode("utf-8")
			print e
			raise e

	def GetCompileUnits(self):
		if self.root != None:
			return self.root.findall("COMPILEUNIT")
		else:
			return []

	def GetCompileUnitsName(self, compile):
		name = compile.get("NAME")
		if name != None:
			print "UNITNAME :" + name
			return name
		else:
			print "UNITNAME参数未配置！".decode("utf-8")

	def GetCompileCodePath(self, compile):
		code_path = compile.find("CODEPATH")
		if code_path != None:
			print "CODEPATH :" + code_path.text
			return code_path.text
		else:
			print "CODEPATH参数未配置！".decode("utf-8")
		
	def GetCompileFileType(self, compile):
		file_type = compile.find("FILETYPE")
		if file_type != None:
			print "FILETYPE :" + file_type.text
			return file_type.text
		else:
			print "FILETYPE参数未配置！".decode("utf-8")

	def GetCompileOutputPath(self, compile):
		output_path = compile.find("OUTPUTPATH")
		if output_path != None:
			print "OUTPUTPATH :" + output_path.text
			return output_path.text
		else:
			print "OUTPUTPATH参数未配置！".decode("utf-8")

	def GetCompileOutputName(self, compile):
		output_name = compile.find("OUTPUTNAME")
		if output_name != None:
			print "OUTPUTNAME :" + output_name.text
			return output_name.text
		else:
			print "OUTPUTNAME参数未配置！".decode("utf-8")

	def GetCompileOutputIP(self, compile):
		output_ip = compile.find("OUTPUTIP")
		if output_ip != None:
			print "OUTPUTIP :" + output_ip.text
			return output_ip.text
		else:
			print "OUTPUTIP参数未配置！".decode("utf-8")

	def GetCompileUsername(self, compile):
		username = compile.find("USERNAME")
		if username != None:
			print "USERNAME :" + username.text
			return username.text
		else:
			print "USERNAME参数未配置！".decode("utf-8")

	def GetCompileAppPath(self, compile):
		app_path = compile.find("APPPATH")
		if app_path != None:
			print "APPPATH :" + app_path.text
			return app_path.text
		else:
			print "APPPATH参数未配置！".decode("utf-8")

	def GetCompilePackagePath(self, compile):
		package_path = compile.find("PACKAGEPATH")
		if package_path != None:
			print "PACKAGEPATH :" + package_path.text
			return package_path.text
		else:
			print "PACKAGEPATH参数未配置！".decode("utf-8")

def test():
	try:
		config = Configuration("./configuration.xml")
	except Exception:
		config = None

	if config != None:
		for unit in config.GetCompileUnits():
			unit_name = config.GetCompileUnitsName(unit)
			code_path = config.GetCompileCodePath(unit)
			file_type = config.GetCompileFileType(unit)
			output_path = config.GetCompileOutputPath(unit)
			output_name = config.GetCompileOutputName(unit)
			output_ip = config.GetCompileOutputIP(unit)
			username = config.GetCompileUsername(unit)
			app_path = config.GetCompileAppPath(unit)
			package_path = config.GetCompilePackagePath(unit)

if __name__ == '__main__':
	test()