#@Date 2014/04/02
#@Author Xin Du
#coding:utf-8

import configution
import util
import checker
import package
import compile
import commands
import os

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
			checker = Checker(code_path, types, output_path, output_name)
			checker.GetAllFiles()
			checker.ShowFiles()
			checker.GenerateOldFilesCksum()
			checker.ShowOldFilesCksum()
			checker.GenerateNewFilesCksum()
			checker.ShowNewFilesCksum()
			checker.CompareFilesCksum()
			result = checker.IsFilesChange()
			print '[Result] : ' + str(result)
			checker.GenerateOldOutputCksum()
			checker.ShowOldOutputCksum()
			checker.GenerateNewOutputCksum()
			checker.ShowNewOutputCksum()
			checker.CompareOutputCksum()
			result = checker.IsOutputChange()
			print '[Result] : ' + str(result)
