#@Date 2014/09/16
#@Author Xin Du
#coding: utf-8
  
import socket
import os
import shutil
import os  
import time
import server

class Console:
	"""控制台"""
	def __init__(self):
		pass
	
	def StartServer(self):
		return_message = 'FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836';
		server.Server('success_service', '127.0.0.1', 8588, return_message, 1).StartServer()
		
	def StopServer(self):
		pass
 		
def test():
	pid = ''
	command = raw_input("Setting opition(server or client):\n")
	if command == "server":
		print 'Start server command: start server -n [server name] -i [ip] -p [port] -m [return_message] -t [timeout]'
		print 'Stop server command: stop server [server name] | [server id]'
		print 'Scan server command: list server'
		opition = raw_input('please input command:').split()
		for item in opition:
			print item
		#console = Console()
		#console.StartServer()

	command = raw_input("Setting Server:start server or stop server\n")
		

if __name__ == '__main__':
	test()