#!/usr/bin/python
# -*- coding: utf8 -*-
########################################################################
#IdCardReader setup
########################################################################
import json
import os
import time
import urllib2 

import threading
from MqttClient import MQTTClient

Mqtt = MQTTClient()
Mqtt.MqttPathPublish = "your path to publish"
Mqtt.MqttPathSubcribe = "WifiStatus"


class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        Mqtt.mqttSubcribe()

# queueLock = threading.Lock()
# thread = myThread(1, "thread1")
# thread.start()

#########################################################################
flag_1 = False
_dataWriteMainApp = {"source":"WifiStatus","func":"wifistatus","data":""}
_dataWriteGPIO = {"source":"WifiStatus","func":"led","data":""}

print "Wifi Status!"

while True:
    try:
        urllib2.urlopen("http://www.google.com").close()
    except urllib2.URLError:
        #print "Not Connected"
        _dataWriteGPIO["func"] = "blinkLed"
        _dataWriteGPIO["data"] = 2
        _dataWriteMainApp["func"] = "wifistatus"
        _dataWriteMainApp["data"] = "off"
        Mqtt.MqttPathPublish = "MainApp"
        Mqtt.mqttPublish(json.dumps(_dataWriteMainApp))
        Mqtt.MqttPathPublish = "GPIO"
        Mqtt.mqttPublish(json.dumps(_dataWriteGPIO))
        time.sleep(2)
    else:
        #print "Connected"
        _dataWriteGPIO["func"] = "led"
        _dataWriteGPIO["data"] = "on"
        _dataWriteMainApp["func"] = "wifistatus"
        _dataWriteMainApp["data"] = "on"
        Mqtt.MqttPathPublish = "MainApp"
        Mqtt.mqttPublish(json.dumps(_dataWriteMainApp))
        Mqtt.MqttPathPublish = "GPIO"
        Mqtt.mqttPublish(json.dumps(_dataWriteGPIO))
        time.sleep(5)


	
