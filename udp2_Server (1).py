#udp2.py Server服务器端
#!/usr/bin/env python3
# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1',9999))
print('Wait for connecting...')

while True:
	data,addr = s.recvfrom(1024)		#接收数据，data为接收到的字符串，addr为发送方的地址
	print('Received from %s:%s.' %addr)	#反映地址
	str2 = str(data,encoding = 'utf-8')	#将接收到的数据转换为str类,编码为utf-8
	print('I received a string is : ',str2)	#反映改写前语言
	str3 = str2.upper()			#将字符串中小写字符转大写
	s.sendto(str3.encode('utf-8'),addr)	#通过UDP发送数据，str3.encode('utf-8')为编码后的str3，addr为接收方地址
s.close()
