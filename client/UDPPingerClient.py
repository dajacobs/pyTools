#!/usr/bin/env python

# Module imports
import socket
import time

# Socket variables
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 12000)
sock.settimeout(1)

# Try block for pinger
try:
	for i in range(1, 11):
		start = time.time()
		message = 'Ping #' +str(i)+ " " +time.ctime(start)
		# Try block for send/receive message
		try: 
			sent = sock.sendto(message, server_addr)
			print 'Sent ' +message
			data, server = sock.recvfrom(4096)
			print 'Received ' +data
			end = time.time()
			diff = end - start
			print 'RTT ' +str(diff)+ 'seconds\n'
		except socket.timeout:
			print '#' +str(i)+ 'Time out\n'
finally:
	sock.close()				