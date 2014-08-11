#@Date 2014/04/02
#@Author Xin Du
#coding:utf-8

from StringIO import StringIO
import sys
buff =StringIO()

temp = sys.stdout                               #保存标准I/O流
sys.stdout = buff  
for i in range(1000):
	print '||' + '-' * 40 + 'Name' + '-' * 40 + '|'
sys.stdout =temp                                 #恢复标准I/O流
print buff.getvalue()

file = open('test.txt', 'w')
file.write(buff.getvalue())
file.close()