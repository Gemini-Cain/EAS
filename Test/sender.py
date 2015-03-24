#@Date 2014/09/16
#@Author Xin Du
#coding: utf-8

__metaclass__ = type

import sys
import socket
import threading
import thread
import os
import shutil
import log

class Sender(threading.Thread):
	"""请求客户端"""
	def __init__(self, ip, port, count, message):
		threading.Thread.__init__(self) 
		self.ip = ip
		self.port = port
		self.count = count
		self.message = message
		log_path = './/log//Client//'
		self.log = log.Log(log_path, self.getName())
	
	def Call(self, message, i):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error, msg:
			error_message = 'Create socket failed:' + msg
			self.log.log_error(error_message)

		try:
			s.connect((self.ip , self.port))
		except socket.error, msg:
			error_message = 'Connect failed:' + msg
			self.log.log_error(error_message)

		try :

			self.log.log_info('[-->]' + message)
			s.sendall(message.decode('utf-8'))
		except socket.error, msg:
			error_message = 'Send failed:' + msg
			self.log.log_error(error_message)

		#接收数据
		ret_message = ''
		while True:
			try:
				buff = s.recv(1024)
				if not len(buff):
					break
				else:
					ret_message += buff
			except socket.error, msg:
				error_message = 'Received error:' + msg
				self.log.log_error(error_message)
		self.log.log_info('[<--]' + ret_message)
		s.close()

		return ret_message

 	def run(self):
 		for i in xrange(self.count):
 			ret = self.Call(self.message, i)
 			print ret
 		
def test():
 	request_message = 'FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836';
	for i in xrange(9):
		Sender('127.0.0.1', 8588, 10, request_message).start()

if __name__ == '__main__':
	test()