#@Date 2014/09/16
#@Author Xin Du
#coding: utf-8

import socket
import os
import shutil

class Console:
	"""控制台"""
	def __init__(self):
		pass
	
	def StartServer(self):
		pass
		
	def StopServer(self):
		pass
 		
def test():
	command = raw_input("Setting Server:start server or stop server")
	if command == "start server":
		server = Server('127.0.0.1', 8588, request_message)
		server.StartServer()

	command = raw_input("Client :start server or stop server")


if __name__ == '__main__':
	test()