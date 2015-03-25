#@Date 2014/09/16
#@Author Xin Du
#coding: utf-8

import socket
import os
import shutil
import log
import time

class Server:
	"""服务端"""
	def __init__(self, ip, port, message, timeout):
		self.ip = ip
		self.port = port
		self.message = message
		self.timeout = timeout
		path = './/log//Server//'
		self.log = log.Log(path, 'Server')
	
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
				buff = connection.recv(10240)
				self.log.log_info('[<--]' + buff)
				if len(buff):
					self.log.log_info('[-->]' + self.message)
					time.sleep(self.timeout)
					connection.send(self.message)
			except socket.timeout, msg:
				error_message = 'Time out:' + msg
				self.log.log_error(error_message)
			connection.close()	
 		
def test():
 	request_message = 'FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836';
	Server('127.0.0.1', 8588, request_message, 1).StartServer()

if __name__ == '__main__':
	test()