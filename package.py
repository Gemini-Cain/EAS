#@Date 2014/04/02
#@Author Xin Du
#coding:utf-8

import commands
import os
import shutil

def Package(username, package_path, app_path, app_name):
	copy_file = app_path + app_name
	path = package_path +　username
	if not os.path.exists(path):
		os.makedirs(path)
	shutil.copy(copy_file, path)
	print "Package Success !"

def SendDevelopEnvironment(src_path, app_name, username, ip, dest_path):
	send_file = src_path + '/' + app_name
	status, output = commands.getstatusoutput('scp ' + send_file + ' ' + username + '@' + ip + ':' + dest_path)
	if status != 0:
		print "Send Error !"
	else:
		print "Send Success !"

def Tar(src_path , tar_name, dest_path):
	status, output = commands.getstatusoutput('tar -zcvf ' + dest_path + '/' + tar_name + ' ' + src_path)
	if status != 0:
		print "Tar Error !"
	else:
		print "Tar Success !"

def test():
	eas_username = 'bppf_eas'
	bis_username = 'bppf_bis'
	ip = '192.168.87.4'
	package_path = "./test/"
	app_path = '/u1'
	output_path = './'
	output_name = 'test.txt'
	tar_name = 'test.tar.gz'
	dest_path = ''

	Package(eas_username, package_path, output_path, output_name)
	Package(bis_username, package_path, output_path, output_name)
	#SendDevelopEnvironment(output_path, output_name, eas_username, ip, app_path)
	#SendDevelopEnvironment(output_path, output_name, bis_username, ip, app_path)
	Tar(package_path , tar_name, dest_path)

if __name__ == '__main__':
	test()