#@Date 2014/09/16
#@Author Xin Du
#coding: utf-8

__metaclass__ = type

import log
import sender
import multiprocessing

class Job(multiprocessing.Process):
	"""请求客户端"""
	def __init__(self, name, ip, port, message, thread, count):
		multiprocessing.Process.__init__(self, name = name)
		self.name = name
		self.ip = ip
		self.port = port
		self.thread = thread
		self.count = count
		self.message = message
		self.threads = []
		for i in xrange(self.thread):
			self.threads.append(sender.Sender(self.ip, self.port, self.count ,self.message))
		#log_path = './/log//Client//'
		#self.log = log.Log(log_path, name)
 		
	def run(self):
		print '*****************'
		for item in self.threads:
			print '***'
			item.start()

	def showState(self):
		print '||' + '-' * 95 + '||'
		for item in self.threads:
			if item.isAlive():
				print '||%-15s|%-15s|%-15s|%-15s|%-15s|%-15s||' %(self.name, item.getName(), self.ip, self.port, self.count, 'Running')
			else:
				print '||%-15s|%-15s|%-15s|%-15s|%-15s|%-15s||' %(self.name, item.getName(), self.ip, self.port, self.count, 'Stopped')
		print '||' + '-' * 95 + '||'

def test():
 	job = Job('test', '127.0.0.1', 8588, 'FFFF012345678900000118EBK000101001UU00ABCDEFGHIJKLMNOPQRSTUVWXYZ000000000020010200210004600100220018110000001000101836', 10, 10)
 	job.showState()
 	job.start()
 	#job.showState()

if __name__ == '__main__':
	test()