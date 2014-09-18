#@Date 2014/09/16
#@Author Xin Du
#coding: utf-8

import sys
import socket

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'Failed to create socket:' + msg
	sys.exit()
print 'Socket Created'
 
ip = '192.168.87.4';
port = 8588;
s.connect((ip , port))
 
#Send some data to remote server
message = "FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836"
 
try :
    #Set the whole string
	s.sendall(message)
except socket.error:
    #Send failed
	print 'Send failed'
	sys.exit()
 
print 'Message send successfully'
 
#Now receive data
reply = s.recv(102400)
 
print reply