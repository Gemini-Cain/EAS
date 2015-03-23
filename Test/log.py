#@Date 2015/03/23
#@Author Xin Du
#coding: utf-8

import os
import time

class Log:
	"""日志"""
	def __init__(self, log_path, log_file_name):
		if not os.path.exists(log_path):
		 	os.mkdir(log_path)
		self.file = open(log_path + log_file_name + '.log', 'a')

	def log_debug(self, message):
		format_message = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ' [Debug] ' +  message + '\n'
		self.file.write(format_message)
	
	def log_info(self, message):
		format_message = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ' [Info] ' +  message + '\n'
		self.file.write(format_message)
	
	def log_error(self, message):
		format_message = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ' [Error] ' + message + '\n'
		self.file.write(format_message)

	def log_warn(self, message):
		format_message = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ' [Warn] ' + message + '\n'
		self.file.write(format_message)
		
def test():
	log1 = Log('.//log//', 'test1')
	log1.log_debug("FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836")
	log1.log_info("FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836")
	log1.log_error("FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836")
	log1.log_warn("FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836")

	log2 = Log('.//log//', 'test2')
	log2.log_debug("FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836")
	log2.log_info("FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836")
	log2.log_error("FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836")
	log2.log_warn("FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836")

if __name__ == '__main__':
	test()
