#@Date 2014/09/16
#@Author Xin Du
#coding: utf-8

import sys
import socket
import thread

class Request:
	"""docstring for ClassName"""
	def __init__(self, ip, port):
		self.ip = ip
		self.prot = port
		
	def Call(self, message):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error, msg:
			print 'Create socket failed:' + msg

		try:
			s.connect((ip , port))
		except socket.error, msg:
			print 'Connect failed:' + msg

		try :
			s.sendall(message)
		except socket.error, msg:
			print 'Send failed:' + msg
		#Now receive data
		ret_message = s.recv(102400)
		return ret_message
 	
 	def ConcurrentCall(thread_count, round, message):
 		for i in xrange(thread_count):
 			thread.start_new_thread(self.Call, (message))
def test():
	req = Request('192.168.87.4', '8588')
	req.ConcurrentCall(10, 10, 'FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836')

if __name__ == '__main__':
	test()