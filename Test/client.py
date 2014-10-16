#@Date 2014/09/16
#@Author Xin Du
#coding: utf-8

import sys
import socket
import threading
import thread
import os

class Client(threading.Thread):
	"""请求客户端"""
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

		#接收数据
		ret_message = None
		try:
			ret_message = s.recv(102400)
			#print "Call:%s\n" %ret_message
		except socket.error, msg:
			print "Received error:%s" %msg
		s.close()

		ret_message = '[' + self.getName() + ':' + str(i) + ']' + ret_message + '\n'
		#print ret_message
		return ret_message

 	def run(self):
 		file = open('./' + self.getName() + '.log', 'w')
 		for i in xrange(self.count):
 			ret = self.Call(self.message, i)
 			#print ret
 			file.write(ret)
 		file.close()
 		
def test():
	for i in xrange(50):
		Client('192.168.87.4', 8588, 10, 'FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836').start()
		

if __name__ == '__main__':
	test()