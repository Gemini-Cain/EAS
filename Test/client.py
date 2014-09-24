#@Date 2014/09/16
#@Author Xin Du
#coding: utf-8

import sys
import socket
import threading
import thread
import os

class Request(threading.Thread):
	"""docstring for ClassName"""
	def __init__(self, ip, port, count, message):
		threading.Thread.__init__(self) 
		self.ip = ip
		self.port = port
		self.count = count
		self.message = message
	
	def Call(self, message, i):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error, msg:
			print 'Create socket failed:%s' %msg

		try:
			s.connect((self.ip , self.port))
		except socket.error, msg:
			print 'Connect failed:%s' %msg

		try :
			s.sendall(message.decode('utf-8'))
		except socket.error, msg:
			print 'Send failed:%s' %msg
		#Now receive data
		ret_message = ''
		while 1:
			try:
				ret_message = s.recv(2048)
			except socket.error, msg:
				print "Received error:%s" %msg
			if not len(ret_message):
				break
		s.close()

		ret_message = '[' + self.getName() + ':' + str(i) + ']' + ret_message + '\n'
		return ret_message

 	def run(self):
 		file = open('./' + self.getName() + '.log', 'w')
 		for i in xrange(self.count):
 			ret = self.Call(self.message, i)
 			file.write(ret)
 		file.close()
 		
def test():
	for i in xrange(20):
		Request('127.0.0.1', 8588, 5, 'FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836').start()
		

if __name__ == '__main__':
	test()