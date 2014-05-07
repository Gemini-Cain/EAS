#@Date 2014/04/02
#@Author Xin Du
#coding:utf-8

__metaclass__ = type
import os
import commands

class Checker:
	"""check the difference between old and new files"""
	def __init__(self):
		self.files = []
		self.old_cksum = {}
		self.new_cksum = {}

	def GetAllFiles(self, types, path):
		""""get all files in the path"""
		self.files.clear()
		dir_list = []
		dir_list.append(path)  
		for dir in dir_list: 
			files = os.listdir(path)
			for file in files:
				full_name = dir + '/' + file
				if(os.path.isdir(full_name)):  
					if(file[0] == '.'):	# 排除隐藏文件夹
						pass  
					else:	# 添加非隐藏文件夹  
						dir_list.append(full_name)  
				if(os.path.isfile(full_name)):
					for type in types.split('|'):
						if file.find(type) != -1:
							# 添加文件  
							self.files.append(f)
		return file_list

	def GenerateOldCksum(self):
		""""generate old files cksum"""
		if len(self.files) > 0:
			for file in self.files:
				status, output = commands.getstatusoutput('cksum ' + file)
				if status == 0:
					old_cksum[file] = output

	def GenerateNewCksum(self):
		""""generate updated files cksum"""
		if len(self.files) > 0:
			for file in self.files:
				status, output = commands.getstatusoutput('cksum ' + file)
				if status == 0:
					files[file] = output
		
	def IsChange(self):
		for file in self.files:
			if self.old_cksum[file] == self.new_cksum[file]:
				return true
			else:
				return false