#!/usr/bin/python
# -*- coding: utf8 -*-
#!/bin/bash

import threading
from MqttClient import MQTTClient

Mqtt = MQTTClient()
Mqtt.MqttPathPublish = "MainApp"
Mqtt.MqttPathSubcribe = "MainApp"



class myThread (threading.Thread):
	def __init__(self, threadID, name):
        	threading.Thread.__init__(self)
            	self.threadID = threadID
            	self.name = name
        def run(self):
            	Mqtt.mqttSubcribe()

queueLock = threading.Lock()
thread = myThread(1, "thread1")
thread.start()

_dataWriteAPIGetPost = {"source":"MainApp","func":"recognize","data":{"ID":"","base64image":""}}


                
                
        
###############################################################
import sys
#import requests 

# import some PyQt5 modules
#from PyQt5.QtWidgets import QApplication
#from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtCore import QThread, pyqtSignal
#from PyQt5.QtGui import QString

from picamera.array import PiRGBArray
from picamera import PiCamera
import urllib2
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs
import cgi
import json
import Tkinter
import subprocess




# import Opencv module
import cv2
#import json


#import
import os.path
from os import path
import json
import requests
#import picamera
import base64
import time
import datetime
import pygame
#import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from evdev import InputDevice, categorize, ecodes

from ui_main_window1 import *

camera = PiCamera()
camera.rotation = 90
camera.resolution = (208,240)
camera.framerate=16
rawCapture= PiRGBArray(camera, size=(208, 240))


#camera.capture(rawCapture, format="bgr")


class MainWindow(QMainWindow):#QWidget
        
        #

        
        
        # class constructor
    def __init__(self):
        #run()

        # call QWidget constructor
        super(MainWindow,self).__init__() # python 3x con python2x()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #bar = self.menuBar()
        #Setting = bar.addMenu('Setting')
        #Status = bar.addMenu('Status')
        self.statusBar().showMessage('Ready')
        self.git_thread = CloneThread()
        #self.git_thread1 = CloneThread1()
        self.git_thread.imageChanged.connect(self.on_imageChanged)
        self.git_thread.start()
        #self.git_thread1.start()
        #self.git_thread1.signalChanged.connect(self.on_signalChanged)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.start(0.1)
        #self.timer.timeout.connect(self.viewCam)
        #self.cap = cv2.VideoCapture(0)
        # start timer
        #self.timer.start(20)
        #self.timer.timeout.connect(self.controlTimer)
        #self.timer.timeout.connect(self.displayimage)
        
        self.timer.timeout.connect(self.detectwifi)
        self.timer.timeout.connect(self.MainApp)
        #set control_bt callback clicked  function
        #self.ui.control_bt.clicked.connect(self.setting)


    # view camera
    def viewCam(self): #hien thi camera
            
            
        #camera = PiCamera()
        #camera.resolution = (640, 480)
        #camera.framerate=24
        #rawCapture= PiRGBArray(camera, size=(640, 480))
        #camera.start_preview()
        #camera.capture("/home/pi/killer/imageGet/image.jpg")
        #camera.stop_preview()

        camera.capture(rawCapture, format="bgr", use_video_port=True)

        #rawCapture.truncate(0)
            # read image in BGR format
        image=self.rawCapture.array
        #ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
        self.rawCapture.truncate(0)




    # start/stop timer
    def controlTimer(self): #hien thi data
        camera.capture("/home/pi/killer/imageGet/image.jpg")
	#req = requests.get('http://localhost:8088')
        #var c = url.searchParams.get("c");
        #contents = urllib2.urlopen("http://localhost:8088/foo/bar").read()
        #r = requests.get("http://localhost:8088/foo/bar",params="foo")

        #json_response = json.loads(r.content) #python 2.7
        #json_response = req.json() #python 3.6
        #long="long"
        #print(str(req))
        data = open('/home/pi/qt5/data.txt', 'r+')
        data1 = data.read()
	data.close()
        #print(data1)
        data_string= json.loads(data1)
        

        
        # if timer is stopped
        #if not self.timer.isActive():
            # create video capture
         #   self.cap = cv2.VideoCapture(0)
            # start timer
          #  self.timer.start(20)
            # update control_bt text
           # self.ui.control_bt.setText("Stop")
        # if timer is started
        #else:
            # stop timer
         #   self.timer.stop()
            # release video capture
          #  self.cap.release()
            # update control_bt text
           # self.ui.control_bt.setText("Start")

        self.ui.label_8.setText(data_string['congty'])
        self.ui.label_9.setText(data_string['ten'])
        self.ui.label_7.setText(data_string['id'])
        self.ui.label_6.setText(data_string['thongbao'])

    
        
        
    def displayimage(self,_imagePath): #hien thi image
        #label = QLabel(self)
        pixmap = QPixmap(_imagePath)
        self.ui.image_label1.setPixmap(pixmap)
        self.ui.image_label1.resize(104,140)

    def detectwifi(self):
        ps = subprocess.Popen(['iwgetid'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        try:

            output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout)
            self.ui.label_10.setText("<font color= green>WIFI")
        except subprocess.CalledProcessError:
            self.ui.label_10.setText("<font color= red>WIFI")
    def on_imageChanged(self, image):
        
        pixmap = QtGui.QPixmap.fromImage(image)
        self.ui.image_label.setPixmap(pixmap)
    #def on_signalChanged(self, signal):
     #   if (signal == '1'):
      #      self.ui.label_10.setText("<font color= green>WIFI")          
      #  else:
       #     self.ui.label_10.setText("<font color= red>WIFI")        
        
        
    
                
    
    def MainApp(self):
        
                
        _waitData = Mqtt.getData()
        #IDCardNumber = ""
	if _waitData != None:
                
	    self.statusBar().showMessage('Processing...')
            print "client get: ", _waitData
            waitData = json.loads(_waitData)
            if waitData["source"] == "KeyBoard":
                IDCardNumber = waitData["data"]
                _imageBase64 = "/home/pi/maychamcong/MainApp/image/image.jpg"
                print("start")
                camera.capture(_imageBase64)
                print("stop")
                pixmap = QPixmap(_imageBase64)
                self.ui.image_label1.setPixmap(pixmap.scaled(104, 140, QtCore.Qt.KeepAspectRatio))


                #with open("/home/pi/maychamcong/MainApp/image/image.jpg") as image_file:
                #    encoded_string = base64.b64encode(image_file.read())
                _dataWriteAPIGetPost["data"]["base64image"] = _imageBase64
                _dataWriteAPIGetPost["data"]["ID"] = IDCardNumber
                Mqtt.MqttPathPublish = "APIGetPost"
                #print "start"
                Mqtt.mqttPublish(json.dumps(_dataWriteAPIGetPost))
                #print "stop"
            if waitData["source"] == "APIGetPost":
                #displayimage("/home/pi/maychamcong/MainApp/image/image.jpg")
                pixmap = QPixmap("/home/pi/maychamcong/MainApp/image/image.jpg")
                self.ui.image_label1.setPixmap(pixmap.scaled(104, 140, QtCore.Qt.KeepAspectRatio))
                #self.ui.image_label1.resize(104,140)
                self.ui.label_9.setText(waitData["data"]["company"])
                self.ui.label_8.setText(waitData["data"]["name"])
                self.ui.label_7.setText(waitData["data"]["ID"])
                _mess = waitData["data"]["mess"]
                if len(_mess) > 15:
                    i = 0
                    k = 0
                    for _space in _mess:
                        i = i + 1
                        if _space == " ":
                            if i > 15:
                                break
                            k = i
                    self.ui.label_6.setText(_mess[0:k])
                    self.ui.label_12.setText(_mess[k:len(_mess)])
                else:
                    self.ui.label_6.setText(_mess)
                    self.ui.label_12.setText("")
                self.statusBar().showMessage('Done!')
                #self.ui.plainTextEdit.setPlainText("the khong hop le the khong hop le")
class CloneThread(QThread):#QWidge
    
    imageChanged = QtCore.pyqtSignal(QtGui.QImage)    
    def __init__(self):
                    
        QThread.__init__(self)
    def run(self):
         
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
          
          #camera.capture(rawCapture, format="bgr", use_video_port=True)

          #rawCapture.truncate(0)
            # read image in BGR format
          image=rawCapture.array
          #ret, image = self.cap.read()
          # convert image to RGB format
          image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
          # get image infos
          height, width, channel = image.shape
          step = channel * width
          # create QImage from image
          qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
          self.imageChanged.emit(qImg)
          # show image in img_label
          #self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
          rawCapture.truncate(0)
#class CloneThread1(QThread):#QWidge
    
 #   signalChanged = QtCore.pyqtSignal(QtGui.QString)    
  #  def __init__(self):
                    
   #     QThread.__init__(self)
    #def run(self):
     #   ps = subprocess.Popen(['iwgetid'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

      #  try:

       #     output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout)
        #    k = '1'
         #   self.signalChanged.emit(k)
        #except subprocess.CalledProcessError:
            
         #   k = '0'
          #  self.signalChanged.emit(k)
                
         
       
          

          
        
                
            
            
            

         
            

    
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    

    # create and show mainWindow
    mainWindow = MainWindow()
    #mainWindow.show()
    mainWindow .showFullScreen()
    

    
    #run()

    sys.exit(app.exec_())
