#@Date 2014/04/02
#@Author Xin Du
#coding:utf-8

__metaclass__ = type
import commands
import configuration
import checker

class Compiler:
	"""compile"""
	def __init__(self, path):
		self.path = path

	def compile(self):
		os.chdir(self.path)
		status, output = commands.getstatusoutput('make')
		if status != 0 || output.find("错误") != -1
			print "Compile Error !"

	def Package(self, output):
		pass

	def SendDevelopEnvironment(self, username, password, ip):

		status, output = commands.getstatusoutput('scp ' + output + ' ' + username + '@' + ip + ':' + path)
		if status != 0:
			print "Send Error !"
		else:
			print "Send Success !"



		
def test():
	try:
		config = Configuration("C:\\Users\\bestpay\\Desktop\\configuration.xml")
	except Exception:
		config = None

	if config != None:
		for unit in config.GetCompileUnits():
			path = config.GetCompilePath(unit)

			config.GetCompileFileType(unit)
			config.GetCompileOutput(unit)

test()