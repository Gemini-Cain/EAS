#@Date 2014/04/02
#@Author Xin Du
#coding:utf-8

__metaclass__ = type
import configuration
import checker

class Compiler:
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
def Compiler():
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