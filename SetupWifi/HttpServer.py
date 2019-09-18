#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import os
import cgi
import sys
import datetime
import threading
import picamera
#import time

import time
import urllib2 
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

PORT_NUMBER = 8080
Flag = False


Buffer = ""

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	#Handler for the GET requests
	def do_GET(self):
		global Flag
		global Buffer
		if self.path == "/":
			self.path = "/index.html"
			
		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				#f = open(curdir + sep + self.path) 
				f = open("/home/pi/maychamcong/SetupWifi" + self.path)
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				#self.wfile.write("Successfull!")
				
				f.close()
			return
		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)
			Flag = False	
		
		
	#Handler for the POST requests
	def do_POST(self):
		if self.path=="/send":
			form = cgi.FieldStorage(
				fp=self.rfile, 
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})

			print "Your name is: %s" % form["your_name"].value
			self.send_response(200)
			self.end_headers()
			self.wfile.write("Thanks %s !" % form["your_name"].value)
			return


try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER

	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()


#class HTTPServerThread (threading.Thread):
#	def __init__(self, threadID, name):
#		threading.Thread.__init__(self)
#		self.threadID = threadID
#		self.name = name
#	def run(self):
#		try:
#			server = HTTPServer(('', PORT_NUMBER), myHandler)
#			print 'Starting ' + self.name + "onport:", PORT_NUMBER
#			server.serve_forever()
#
#		except KeyboardInterrupt:
#			print 'server.socket.close()'
#			server.socket.close()

#HTTPServerThread1 = HTTPServerThread(1, "Get HTTP Server")

