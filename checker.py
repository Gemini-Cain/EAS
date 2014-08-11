#@Date 2014/04/02
#@Author Xin Du
#coding:utf-8

__metaclass__ = type
import os
import commands
import util
from StringIO import StringIO
import sys

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
		util.PrintList('CODE FILE', self.file_list)

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
		util.PrintDictionary('OLD FILES CKSUM', self.old_file_cksum)
		
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
		util.PrintDictionary('NEW FILES CKSUM', self.new_file_cksum)
	
	def GenerateOldOutputCksum(self):
		""""generate old output cksum"""
		for temp in self.output_name.split('|'):
			temp = self.output_path + temp
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
		util.PrintDictionary('OLD OUTPUT CKSUM', self.old_output_cksum)

	def GenerateNewOutputCksum(self):
		""""generate updated output cksum"""
		for temp in self.output_name.split('|'):
			temp = self.output_path + temp
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
		util.PrintDictionary('NEW OUTPUT CKSUM', self.new_output_cksum)
	
	def IsFilesChange(self):
		for file in self.file_list:
			if self.old_file_cksum[file] != self.new_file_cksum[file]:
				return True
		return False

	def IsOutputChange(self):
		for temp in self.output_name.split('|'):
			temp = self.output_path + temp
			if self.old_output_cksum[temp] != self.new_output_cksum[temp]:
				return True
		return False

	def CompareFilesCksum(self):
		buff = StringIO()
		temp = sys.stdout
		sys.stdout = buff
		print '[Cksum Compare Start]'
		print '||' + '-' * 40 + 'Name' + '-' * 40 + '|' + '-' * 10 + 'Old Cksum' + '-' * 10 + '|' + '-' * 10 + 'New Cksum' + '-' * 10 + '|-' + 'Is Change' + '-||'
		for item in self.file_list:
			result = self.old_file_cksum[item] != self.new_file_cksum[item]
			print '||%-84s|%-29s|%-29s|%-11s||' %(item, str(self.old_file_cksum[item]), str(self.new_file_cksum[item]), str(result))
		print '||' + '-' * 84 + '|' + '-' * 29 + '|' + '-' * 29 + '|' + '-' * 11 + '||'
		print '[Cksum Compare End]'

		sys.stdout = temp
		print buff.getvalue()
		file = open('CompareFilesCksum.txt', 'w')
		file.write(buff.getvalue())
		file.close()

	def CompareOutputCksum(self):
		buff = StringIO()
		temp = sys.stdout
		sys.stdout = buff
		print '[Cksum Compare Start]'
		print '||' + '-' * 40 + 'Name' + '-' * 40 + '|' + '-' * 10 + 'Old Cksum' + '-' * 10 + '|' + '-' * 10 + 'New Cksum' + '-' * 10 + '|-' + 'Is Change' + '-||'
		for item in self.output_name.split('|'):
			item = self.output_path + item
			result = self.old_output_cksum[item] != self.new_output_cksum[item]
			print '||%-84s|%-29s|%-29s|%-11s||' %(item, str(self.old_output_cksum[item]), str(self.new_output_cksum[item]), str(result))
		print '||' + '-' * 84 + '|' + '-' * 29 + '|' + '-' * 29 + '|' + '-' * 11 + '||'
		print '[Cksum Compare End]'
		sys.stdout = temp
		print buff.getvalue()
		file = open('CompareOutputCksum.txt', 'w')
		file.write(buff.getvalue())
		file.close()

def test():

	code_path = 'D:\\Code\\DEV\\serv\\S_EBK'
	types = '.cpp|.h|Makefile'
	output_path = '/lib/'
	output_name = 'S_SCS.so'
	checker = Checker(code_path, types, output_path, output_name);
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


if __name__ == '__main__':
	test()