﻿#@Date 2014/09/16
#@Author Xin Du
#coding: utf-8

from multiprocessing import Process  
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
		request_message = 'FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836';
		server.Server('127.0.0.1', 8588, request_message, 1).StartServer()
		
	def StopServer(self):
		pass
 		
def test():
	pid = ''
	command = raw_input("Setting Server:start server or stop server\n")
	if command == "start server":
		console = Console()
		process = Process(target = console.StartServer(), args=())
		pid = process.pid
		process.start()
		process.join()

	command = raw_input("Setting Server:start server or stop server\n")
	if command == "stop server":
		os.kill(pid)

if __name__ == '__main__':
	test()