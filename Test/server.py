#@Date 2014/09/16
#@Author Xin Du
#coding: utf-8

import socket
import os
import shutil

class Server:
	"""服务端"""
	def __init__(self, ip, port, message):
		self.ip = ip
		self.port = port
		self.message = message
	
	def StartServer(self):
		try:
			sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			sock.bind((self.ip, self.port))
			sock.listen(10) 
		except socket.error, msg:
			print '[Error] Create socket failed:%s' %msg
		
		while True:
			connection,address = sock.accept()
			try:
				connection.settimeout(5)
				buf = connection.recv(10240)
				print buf
				if len(buf):
					connection.send('FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836')
			except socket.timeout:
				print 'time out'
			connection.close()		
 		
def test():
	path = '.\\log\\'
	if os.path.exists(path):
		shutil.rmtree(path)  
 	os.mkdir(path)
 	request_message = 'FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836';
	Server('127.0.0.1', 8588, request_message).StartServer()

if __name__ == '__main__':
	test()