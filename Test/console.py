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
		self.server_list = {}
	
	def serverSetting(self):
		server_command = ('start', 'stop', 'list', 'exit')
		server_start_command_opition= {'-n':'', '-i':'', '-p':'', '-m':'', '-t':''}
		while True:
			print '1.Start server command: start -n [server name] -i [ip] -p [port] -m [return_message] -t [timeout]'
			print '2.Stop server command: stop [server name] | [server id]'
			print '3.Scan server command: list'
			print '4.Exit command: exit'
			opition = raw_input('please input command: > ').split()
			if len(opition) <= 0:
				continue
			elif len(opition) == 1:
				if opition[0] == server_command[2]:
					showServer()
					continue
				elif opition[0] == server_command[3]:
					break
				elif opition[0] == server_command[0]:
					startServer('', '', '', '', '')
					continue
				else:
					print '[!]Error Input'
					continue
			elif len(opition) == 2:
				if opition[0] == server_command[1]:
					stopServer(opition[1])
				else:
					print '[!]Error Input'
					continue
			else :
				if opition[0] == server_command[0]:
					if len(opition) % 2 == 0:
						print '[!]Error Input'
						continue
					else:
						for i in xrange(1,len(opition), 2):
							if opition[i] in server_start_command_opition:
								server_start_command_opition[opition[i]] = opition[i + 1]
							else:
								print '[!]Error Parameter Input'

					name = server_start_command_opition['-n']
					ip = server_start_command_opition['-i']
					port = server_start_command_opition['-p']
					return_message = server_start_command_opition['-m']
					timeout = server_start_command_opition['-t']
					sartServer(name, ip, port, return_message, timeout)
					continue										
				else:
					print '[!]Error Input'
					continue
	def startServer(self, name, ip, port, return_message, timeout):
		if name == '':
			name = 'success_service'
		if ip == '':
			ip = '127.0.0.1'
		if port == '':
			port = 8588
		else:
			port = int(port)
		if return_message == '':
			return_message = 'FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836'
		if timeout == '':
			timeout = 0
		else:
			timeout = int(timeout)

		if name in self.server_list.keys():
			print '[!]Server Name Is Exist'
		else:
			server_thread = server.Server(name, ip, port, return_message, timeout)
			self.server_list[name] = server_thread
			server_thread.start()
		
	def stopServer(self, key):
		if key in self.server_list.keys():
			self.server_list[key].terminate()
		else:
			print '[!] Service name is not exist'

	def showServer(self):
		for key in self.server_list.keys():
			if self.server_list[key].is_alive():
				print '[' + key + '] ' + 'Running'
			else:
				 print '[' + key + '] ' + 'Stopped'
		print '\n'

	def clientSetting(self):
		client_command = ('start', 'stop', 'list', 'exit')
		client_start_command_opition= {'-n':'', '-i':'', '-p':'', '-m':'', '-t':''}
		while True:
			print '1.Start client command: start -n [server name] -i [ip] -p [port] -m [return_message] -t [thread] -c [count]'
			print '2.Stop client command: stop [server name]'
			print '3.Scan client command: list'
			print '4.Exit command: exit'
			opition = raw_input('please input command: > ').split()
			if len(opition) <= 0:
				continue
			elif len(opition) == 1:
				if opition[0] == client_command[2]:
					showServer()
					continue
				elif opition[0] == client_command[3]:
					break
				elif opition[0] == client_command[0]:
					startServer('', '', '', '', '')
					continue
				else:
					print '[!]Error Input'
					continue
			elif len(opition) == 2:
				if opition[0] == client_command[1]:
					stopServer(opition[1])
				else:
					print '[!]Error Input'
					continue
			else :
				if opition[0] == client_command[0]:
					if len(opition) % 2 == 0:
						print '[!]Error Input'
						continue
					else:
						for i in xrange(1,len(opition), 2):
							if opition[i] in server_start_command_opition:
								server_start_command_opition[opition[i]] = opition[i + 1]

					name = server_start_command_opition['-n']
					ip = server_start_command_opition['-i']
					port = server_start_command_opition['-p']
					return_message = server_start_command_opition['-m']
					timeout = server_start_command_opition['-t']
					sartServer(name, ip, port, return_message, timeout)
					continue										
				else:
					print '[!]Error Input'
					continue
	
	def startSender(self, name, ip, port, return_message, thread, count):
		if name == '':
			name = 'success_service'
		if ip == '':
			ip = '127.0.0.1'
		if port == '':
			port = 8588
		else:
			port = int(port)
		if return_message == '':
			return_message = 'FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836'
		if thread == '':
			thread = 1
		else:
			timeout = int(thread)
		if count == '':
			count = 1
		else:
			count = int(count)

		if name in self.server_list.keys():
			print '[!]Server Name Is Exist'
		else:
			server_thread = server.Server(name, ip, port, return_message, timeout)
			self.server_list[name] = server_thread
			server_thread.start()
		
	def stopSender(self, key):
		if key in self.server_list.keys():
			self.server_list[key].terminate()
		else:
			print '[!] Service name is not exist'

	def showSender(self):
		for key in self.server_list.keys():
			if self.server_list[key].is_alive():
				print '[' + key + '] ' + 'Running'
			else:
				 print '[' + key + '] ' + 'Stopped'
		print '\n'


			
 		
def test():

	console = Console()
	while True:
		command = raw_input("Setting opition(server, client or exit): > ")
		if command == 'server':
			console.serverSetting()
		elif command == 'client':
			pass
		elif command == 'exit':
			break
		else:
			print '[!]Error Input'
			continue



if __name__ == '__main__':
	test()