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
import threading
import thread

class Server(multiprocessing.Process):
	"""服务端"""
	def __init__(self, server_name, ip, port, return_message, timeout):
		multiprocessing.Process.__init__(self, name = server_name) 
		print '************************'
		print self.name
		print '************************'
		#print super(Server, self).pid
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
			connection,address = sock.accept()				
			connection.settimeout(5)
		except socket.error, msg:
			error_message = 'Create socket failed:' + msg
			self.log.log_error(error_message)
		while True:		
			try:		
				buff = connection.recv(10240)
				self.log.log_info('[<--]' + buff)
				if len(buff) > 0:
					self.log.log_info('[-->]' + self.return_message)
					time.sleep(self.timeout)
					connection.send(self.return_message)
			except socket.timeout, msg:
				error_message = 'Time out:' + str(msg)
				self.log.log_error(error_message)

		self.log.log_info('Close connection')
		connection.close()	

	def run(self):
		path = './/log//Server//'
		self.log = log.Log(path, self.name)
		self.StartServer()
 		
def test():
 	return_message = 'FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836';
	Server('success_service', '127.0.0.1', 8588, return_message, 1).start()

if __name__ == '__main__':
	test()