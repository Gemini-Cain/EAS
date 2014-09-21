#@Date 2014/09/20
#@Author Xin Du
#coding: utf-8

__metaclass__ = type 

from xml.etree.ElementTree import ElementTree, Element, SubElement

class ConfigurationManager:
	'''manage configuration'''
	def __init__(self, file_name):
		'''initialize xml's root note'''
		self.file_name = file_name
		self.tree = None
		self.root = None

	def ReadXML(self):
		try:
			self.tree = ElementTree()
			self.tree.parse(self.file_name)
			self.root = self.tree.getroot()
		except Exception, e:
			print self.file_name + "无法解析".decode("utf-8")
			print e
			raise e

	def Intent(self, elem, level = 0):
		temp = "\n" + level*"\t"
		if len(elem):
			if not elem.text or not elem.text.strip():
				elem.text = temp + "\t"
			for e in elem:
				self.Intent(e, level + 1)
			if not e.tail or not e.tail.strip():
				e.tail = temp
		if level and (not elem.tail or not elem.tail.strip()):
			elem.tail = temp

	def WriteXML(self):
		if self.root != None:
			self.Intent(self.root)
		if self.tree != None:
			self.tree.write(self.file_name, 'utf-8', True)

	def GetItems(self):
		if self.root != None:
			return self.root.findall("ITEM")
		else:
			print 'Root is None !'
			return []

	def GetItemName(self, item):
		name = item.find("NAME")
		if name != None:
			#print "NAME :" + name.text
			return name.text
		else:
			print "NAME参数未配置！".decode("utf-8")

	def GetItemIP(self, item):
		ip = item.find("IP")
		if ip != None:
			#print "IP :" + ip.text
			return ip.text
		else:
			print "IP参数未配置！".decode("utf-8")

	def GetItemPort(self, item):
		port = item.find("PORT")
		if port != None:
			#print "PORT :" + port.text
			return port.text
		else:
			print "PORT参数未配置！".decode("utf-8")

	def ShowAllItems(self):
		list = []
		for item in self.GetItems():
			print item
			message = '[' + self.GetItemName(item) + '] ' + self.GetItemIP(item) + ':' + self.GetItemPort(item);
			#print message
			list.append(message)
		return list

	def AddItem(self, item):
		#self.root = ElementTree.Element('CONFIGURATION')
		if self.root != None:
			self.root.append(item,)

def test():
	manager = ConfigurationManager('./configuration.xml')
	manager.ReadXML()
	list = manager.ShowAllItems()
	for i in range(len(list)):
		print str(i + 1) + '.' + list[i]
	item1 = Element('ITEM')
	item11 = Element('NAME')
	item11.text = '测试'.decode("utf-8")
	item1.append(item11)
	item12 = Element('IP')
	item12.text = '127.0.0.0'
	item1.append(item12)
	item13 = Element('PORT')
	item13.text = '8588'
	item1.append(item13)
	manager.AddItem(item1)
	manager.WriteXML()
	manager.ReadXML()
	list = manager.ShowAllItems()
	for i in range(len(list)):
		print str(i + 1) + '.' + list[i]		

if __name__ == '__main__':
	test()