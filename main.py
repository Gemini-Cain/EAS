#@Date 2014/04/02
#@Author Xin Du
#coding:utf-8

import configution
import util
import checker
import package
import compile

def main():
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