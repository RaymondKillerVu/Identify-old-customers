from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

from time import sleep
import serial
import threading
import time
import json
import math
import datetime
import os
import requests

#Web Socket:
SocketDataOld = ""
SocketData = ""
#ResponseFlag = False

class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        global SocketData
        SocketData = self.data

    def handleConnected(self):
        print(self.address, 'connected!')

    def handleClose(self):
        print(self.address, 'closed!')

class SocketThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    #   self.counter = counter
    def run(self):
        #global SocketData
	print "Starting " + self.name + "!\n"
        server = SimpleWebSocketServer('', 8181, SimpleEcho)
        server.serveforever()

threadLock = threading.Lock()
#threads = []

# Create new threads
SocketThread = SocketThread(1, "Socket Comunicate")

# Start new Threads
SocketThread.start()


while True:
    #SocketData = ""    
    SocketDataOld = SocketData
    
    
    if(SocketDataOld.find('WifiSetup') != -1):
        print "client WifiSetup"
        data = json.loads(SocketDataOld)
        f=open("/etc/wpa_supplicant/wpa_supplicant.conf", "a+")
        _str = "\nnetwork={\n        ssid=\"" + data["SSID"] + "\"\n        psk=\"" + data["PASS"] + "\"\n        key_mgmt=" + data["key_mgmt"] + "\n}"
        f.write(_str)
        f.close()    
        os.system('sudo reboot')
        
        
    
    if(SocketDataOld.find('StaticWifi') != -1):
        print "client StaticWifi"
        data = json.loads(SocketDataOld)   
        os.system('sudo rm /etc/dhcpcd.conf')
        f=open("/etc/dhcpcd.conf", "w+")
        _str = "\nSSID " + data["SSID"] + "\ninform " + data["IPWifiStatic"] + "\nstatic routers=" + data["IPWifiRouters"] + "\nstatic domain_name_servers=" + data["DNS"] + "\nstatic domain_search=" + data["DSS"]
        f.write(_str)
        f.close() 
        os.system('sudo chmod 777 /etc/dhcpcd.conf')
        os.system('sudo reboot')
    
    if(SocketDataOld.find('StaticLAN') != -1):
        print "client StaticLAN"
        data = json.loads(SocketDataOld)
        os.system('sudo rm /etc/dhcpcd.conf')
        f=open("/etc/dhcpcd.conf", "w+")
        _str = "interface eth0\ninform " + data["IPLANStatic"] + "\nstatic routers=" + data["IPLANRouters"] + "\nstatic domain_name_servers=" + data["DNS"] + "\nstatic domain_search=" + data["DSS"]
        f.write(_str)
        f.close() 
        os.system('sudo chmod 777 /etc/dhcpcd.conf')
        os.system('sudo reboot')


