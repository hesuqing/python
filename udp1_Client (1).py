#upd1.py  Client 客户机端
#!/usr/bin/env python3
# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(('127.0.0.1',9999))
print('I am connecting the Server!')

for fwt in ['aBch','f服务d','h7Tq','.']:
	s.sendto(fwt.encode('utf-8'),('127.0.0.1',9999))
	str1,addr = s.recvfrom(1024)
	str2 = str(str1,encoding = 'utf-8')
	print('The original string is : ',fwt,'\tthe processed string is :',str2)
s.close()
