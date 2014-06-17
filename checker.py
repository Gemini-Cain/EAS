#@Date 2014/04/02
#@Author Xin Du
#coding:utf-8

__metaclass__ = type
import os
import commands
import configuration
import util

class Checker:
	"""check the difference between old and new files"""
	def __init__(self, path, types, output_path, output_name):
		self.path = path
		self.types = types
		self.output_path = output_path
		self.output_name = output_name
		self.file_list = []
		self.old_file_cksum = {}
		self.new_file_cksum = {}
		self.old_output_cksum = {}
		self.new_output_cksum = {}


	def GetAllFiles(self):
		""""get all files in the path"""
		dir_list = []
		dir_list.append(self.path)  
		for dir in dir_list: 
			files = os.listdir(dir)
			for file in files:
				full_name = dir + "\\\\" + file
				if(os.path.isdir(full_name)):  
					if(file[0] == '.'):	# 排除隐藏文件夹
						pass  
					else:	# 添加非隐藏文件夹  
						dir_list.append(full_name)  
				if(os.path.isfile(full_name)):
					for type in self.types.split('|'):
						if file.find(type) != -1:
							# 添加文件  
							self.file_list.append(full_name)
							#print "Add file " + full_name

	def ShowFiles(self):
		""""show all files in the path"""
		PrintList('CODE FILE', self.file_list)

	def GenerateOldFilesCksum(self):
		""""generate old files cksum"""
		if len(self.file_list) > 0:
			for file in self.file_list:
				status, output = commands.getstatusoutput('cksum ' + file)
				if status == 0:
					pos = output.find(temp)
					if pos != -1:
						output = output[:pos - 1]
					self.old_file_cksum[file] = output
				else:
					self.old_file_cksum[file] = None
		else:
			print "无文件存在！".decode("utf-8")

	def ShowOldFilesCksum(self):
		""""show all files cksum in the path"""
		PrintDictionary('OLD FILES CKSUM', self.old_file_cksum)
		
	def GenerateNewFilesCksum(self):
		""""generate updated files cksum"""
		if len(self.file_list) > 0:
			for file in self.file_list:
				status, output = commands.getstatusoutput('cksum ' + file)
				if status == 0:
					pos = output.find(temp)
					if pos != -1:
						output = output[:pos - 1]
					self.new_file_cksum[file] = output
				else:
					self.new_file_cksum[file] = None
		else:
			print "无文件存在！".decode("utf-8")

	def ShowNewFilesCksum(self):
		""""show all files cksum in the path"""
		PrintDictionary('NEW FILES CKSUM', self.new_file_cksum)
	
	def GenerateOldOutputCksum(self):
		""""generate old output cksum"""
		for temp in self.output_name.split('|'):
			temp = output_path + temp
			status, output = commands.getstatusoutput('cksum ' + temp)
			if status == 0:	
				pos = output.find(temp)
				if pos != -1:
					output = output[:pos - 1]			
				self.old_output_cksum[temp] = output
			else:
				self.old_output_cksum[temp] = None

	def ShowOldOutputCksum(self):
		""""show all files cksum in the path"""
		PrintDictionary('OLD OUTPUT CKSUM', self.old_output_cksum)

	def GenerateNewOutputCksum(self):
		""""generate updated output cksum"""
		for temp in self.output_name.split('|'):
			temp = output_path + temp
			status, output = commands.getstatusoutput('cksum ' + temp)
			if status == 0:
				pos = output.find(temp)
				if pos != -1:
					output = output[:pos - 1]
				self.new_output_cksum[temp] = output
			else:
				self.new_output_cksum[temp] = None

	def ShowNewOutputCksum(self):
		""""show all files cksum in the path"""
		PrintDictionary('NEW OUTPUT CKSUM', self.new_output_cksum)
	
	def IsFilesChange(self):
		for file in file_list:
			if self.old_file_cksum[file] != self.new_file_cksum[file]:
				return True
		return False

	def IsOutputChange(self):
		for temp in self.output_name.split('|'):
			if self.old_output_cksum[temp] != self.new_output_cksum[temp]:
				return True
		return False

	def CompareCksum(self):
		print '[Cksum Compare Start]'
		print '||' + '-' * 40 + 'Name' + '-' * 40 + '|' + '-' * 10 + 'Old Cksum' + '-' * 10 + '|' + '-' * 10 + 'New Cksum' + '-' * 10 + '|-' + 'Is Change' + '-||'
		for item in self.file_list:
			result = self.old_file_cksum[item] != self.new_file_cksum[item]
			print '||%-84s|%-29s|%-29s|%-11s||' %(item, str(self.old_file_cksum[item]), str(self.new_file_cksum[item]), str(result))
		print '||' + '-' * 84 + '|' + '-' * 29 + '|' + '-' * 29 + '|' + '-' * 11 + '||'
		print '[Cksum Compare End]'

def test():
	try:
		config = configuration.Configuration("./configuration.xml")
	except Exception:
		print "error!!!"
		config = None

	if config != None:
			code_path = 'D:\\Code\\DEV\\serv\\S_EBK'
			types = '.cpp|.h|Makefile'
			output_path = '/lib/'
			output_name = 'S_SCS.so'
			checker = Checker(code_path, types, output_path, output_name);
			checker.GetAllFiles(code_path, types)
			PrintList('File List', file_list)
			old_file_cksum = checker.GenerateOldFilesCksum(file_list)
			PrintDictionary('Old File Cksum', old_file_cksum)
			new_file_cksum = checker.GenerateNewFilesCksum(file_list)
			PrintDictionary('New File Cksum', new_file_cksum)
			checker.CompareCksum(file_list, old_file_cksum, new_file_cksum)
			result = checker.IsFilesChange(file_list, old_file_cksum, new_file_cksum)
			print '[Result] : ' + str(result)
			old_output_cksum = checker.GenerateOldOutputCksum(output_name)
			PrintDictionary('Old Output Cksum', old_output_cksum)
			new_output_cksum = checker.GenerateNewOutputCksum(output_name)
			PrintDictionary('New Output Cksum', new_output_cksum)
			result = checker.IsOutputChange(output_name, old_output_cksum, new_output_cksum)
			print '[Result] : ' + str(result)


if __name__ == '__main__':
	test()