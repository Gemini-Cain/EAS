#@Date 2014/09/16
#@Author Xin Du
#coding: utf-8

import socket
 		
def test():
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.bind(('127.0.0.1',8588))
	sock.listen(10) 
	while True:
		connection,address = sock.accept()
		print "client ip is "
		print address
		try:
			connection.settimeout(5)
			buf = connection.recv(10240)
			if not len(buf):
				connection.send('FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836')
		except socket.timeout:
			print 'time out'
		connection.close()		

if __name__ == '__main__':
	test()