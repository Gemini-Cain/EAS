#@Date 2014/09/16
#@Author Xin Du
#coding: utf-8

__metaclass__ = type

import socket
import os
import shutil
import log
import time
import multiprocessing

class Server(multiprocessing.Process):
	"""服务端"""
	def __init__(self, server_name, ip, port, return_message, timeout):
		multiprocessing.Process.__init__(self, name = server_name) 
		self.ip = ip
		self.port = port
		self.return_message = return_message
		self.timeout = timeout
		self.log = None
	
	def StartServer(self):
		try:
			sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			sock.bind((self.ip, self.port))
			sock.listen(10) 			
		except socket.error, msg:
			error_message = 'Create socket failed:' + msg
			self.log.log_error(error_message)

		while True:	
			connection,address = sock.accept()
			try:	
				connection.settimeout(5)
				buff = connection.recv(1024)
				self.log.log_info('[<--]' + buff)
				if len(buff) > 0:					
					time.sleep(self.timeout)
					print '[<--]' + buff
					self.log.log_info('[-->]' + self.return_message)
					connection.send(self.return_message)
					print '[-->]' + self.return_message
			except socket.timeout, msg:
				connection.close()
				error_message = 'Time out:' + str(msg)
				self.log.log_error(error_message)
			#self.log.log_info('Close connection')
			#connection.close()

	def run(self):
		path = './/log//Server//'
		self.log = log.Log(path, self.name)
		self.StartServer()

	def terminate(self):
		self.log.close()
		super().terminate()
 		
def test():
 	return_message = 'FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836';
	Server('success_service', '127.0.0.1', 8588, return_message, 1).start()

if __name__ == '__main__':
	test()