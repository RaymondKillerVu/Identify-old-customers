#!/usr/bin/python
# -*- coding: utf8 -*-
########################################################################
#GPIO setup
########################################################################
import json
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

import threading
from MqttClient import MQTTClient

Mqtt = MQTTClient()
Mqtt.MqttPathPublish = "your path to publish"
Mqtt.MqttPathSubcribe = "GPIO"


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

_dataWriteMainApp = {"source":"GPIO","func":"interrupt","data":""}
_dataWriteAudioPlay = {"source":"GPIO","func":"play","data":""}

########################################################################
#GPIO setup
LedWifi = 18
LedStatus = 16
interrupt1 = 22

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# #wifi status:
GPIO.setup(LedWifi, GPIO.OUT, initial=GPIO.LOW) 
#trigger status: 
GPIO.setup(LedStatus, GPIO.OUT, initial=GPIO.LOW) 
#interrup:
GPIO.setup(interrupt1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def interrupt_handler(channel):
    print("start interrupt trigger handler!")
    #if channel == interrupt1:
    _dataWriteMainApp["data"] = "interrupt1"
    Mqtt.MqttPathPublish = "MainApp"
    Mqtt.mqttPublish(json.dumps(_dataWriteMainApp))
    print("stop interrupt trigger handler!")

GPIO.add_event_detect(interrupt1, GPIO.RISING, callback=interrupt_handler, bouncetime=200)

def blinkLed(_number,_time,_timeDelay):
    for _t in range(_time):
        GPIO.output(_number, GPIO.HIGH) # Turn on
        time.sleep(_timeDelay)
        GPIO.output(_number, GPIO.LOW) # Turn off
        time.sleep(_timeDelay)

def led(_number,_lever):
    if _lever == "on":
        GPIO.output(_number, GPIO.HIGH) # Turn on
    elif _lever == "off":
        GPIO.output(_number, GPIO.LOW) # Turn on

########################################################################

print "start GPIO!"
while True:
    _waitData = Mqtt.getData()
    if _waitData != None:
        if (_waitData.find('source') != -1) & (_waitData.find('func') != -1):
            waitData = json.loads(_waitData)
            if waitData["source"] == "APIGetPost":
                if waitData["func"] == "blinkLed":
                    blinkLed(LedStatus,waitData["data"],0.2)
            elif waitData["source"] == "MainApp":
                if waitData["func"] == "blinkLed":
                    blinkLed(LedStatus,waitData["data"],0.2)
            elif waitData["source"] == "WifiStatus":
                if waitData["func"] == "led":
                    led(LedWifi,waitData["data"])
                if waitData["func"] == "blinkLed":
                    blinkLed(LedStatus,waitData["data"],0.2)
