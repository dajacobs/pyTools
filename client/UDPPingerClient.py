#!/usr/bin/env python

# Module imports
from socket import *
import time

# Socket variables
servName = 'localhost'
servPort = 12000
clientSock = socket(AF_INET, SOCK_DGRAM)
server_addr = (servName, servPort)
clientSock.settimeout(1)

# Try block for pinger
try:
	for i in range(1, 11):
		start = time.time()
		message = 'Ping #' +str(i)+ " " +time.ctime(start)
		# Try block for send/receive message
		try: 
			sent = clientSock.sendto(message, server_addr)
			print 'Sent ' +message
			data, server = clientSock.recvfrom(4096)
			print 'Received ' +data
			end = time.time()
			diff = end - start
			print 'RTT ' +str(diff)+ 'seconds\n'
		except socket.timeout:
			print '#' +str(i)+ 'Time out\n'
finally:
	clientSock.close()				