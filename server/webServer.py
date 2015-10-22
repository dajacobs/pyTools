#!/usr/bin/env python

# Import modules
from socket import *
# Socket/Port variables
serverSocket = socket(AF_INET, SOCK_STREAM)
TCP_PORT     = 8000
BUFFER_SIZE  = 1024

# Bind TCP set and set socket to listen
serverSocket.bind('', TCP_PORT)
serverSocket.listen(1)

# Conditional loop for connection
while True:
	print 'Ready to server...'
	connectionSocket, addr = serverSocket.accept()
	print 'Connection address: ', addr

	# Try block for HTTP request/response/error message
	try:
		message = connectionSocket.recv(BUFFER_SIZE)
		file    = message.split()[1]
		f       = open(file[1:])
		out     = f.read()

		# HTTP header/file content sent to client
		connectionSocket.send('HTTP/1.0 200 OK\r\n')
		for i in range(0, len(out)):
			connectionSocket.send(out[i])
		connectionSocket.close()	
	except IOError:
		# 404 Not Found Error Message
		err = '''<html> <head> <title> 404 </title> </head> <body><h1>404 Not Found</h1> <h3> Error Message </h3> </body></html>'''
		connectionSocket.send('HTTP/1.0 200 OK\r\n'%len(err))
		for i in err:
			connectionSocket.send(i)
	serverSocket.close()						  		