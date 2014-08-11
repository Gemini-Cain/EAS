#@Date 2014/04/02
#@Author Xin Du
#coding:utf-8

from StringIO import StringIO
import sys

def PrintList(list_name, list):
	print '[' + list_name + ' Start]'
	print '||' + '-' * 40 + 'Name' + '-' * 40 + '||'
	for item in list:
		print '||%-84s||' %item
	print '||' + '-' * 84 + '||' 
	print '[' + list_name + ' End]'

def PrintDictionary(dic_name, dic):
	print '[' + dic_name + ' Start]'
	print '||' + '-' * 40 + 'Name' + '-' * 40 + '|' + '-' * 10 + 'Cksum' + '-' * 10 + '||'
	for item in dic.keys():
		print '||%-84s|%-25s||' %(item, str(dic[item]))
	print '||' + '-' * 84 + '|' + '-' * 25 + '||'
	print '[' + dic_name + ' End]'

def SaveToFile(file_name, mode, content):
	file = open(file_name, mode)
	file.writelines(content)
	file.close()

def test():
	print 'test'

if __name__ == '__main__':
	test()