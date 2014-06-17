#@Date 2014/04/02
#@Author Xin Du
#coding:utf-8

import commands
import os

def Compile(code_path):
	os.chdir(code_path)
	status, output = commands.getstatusoutput('make')
	if status != 0 or output.find("错误")!= -1:
		print "Compile Error !"


def test():
	code_path = '../serv/S_EBK/'
	Compile(code_path)

if __name__ == '__main__':
	test()
