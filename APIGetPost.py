#!/usr/bin/python
# -*- coding: utf8 -*-
########################################################################
#API face detect setup
########################################################################
import json
import requests
import base64
from datetime import datetime
from ftplib import FTP
import time
import os

import threading
from MqttClient import MQTTClient

Mqtt = MQTTClient()
Mqtt.MqttPathPublish = "your path to publish"
Mqtt.MqttPathSubcribe = "APIGetPost"


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

#login infomation
# urlLogin = "http://new-thd.ddns.net:4000/v1/auth"
urlLogin = "https://api.deepkafe.com/faceid/v1/auth"
typeHeaderLogin = {'Content-Type': 'application/json'}
userData = {"username": "creta",  "password": "creta"}

#API Upload
# urlDac = "http://new-thd.ddns.net:4000/v1/dac"
urlDac = "https://api.deepkafe.com/faceid/v1/dac"

#Get access data
# urlGetAccess = "http://new-thd.ddns.net:4000/v1/fetch"
urlGetAccess = "https://api.deepkafe.com/faceid/v1/fetch"
dataGetAccess = {"start_time": "01/01/1992 1:1:1", "end_time": "06/03/2019 1:1:1"}

#Verification API
# urlVerify = "http://new-thd.ddns.net:4000/v1/verify"
urlVerify = "https://api.deepkafe.com/faceid/v1/verify"
dataVerify = {'image': '',  'verify_id' : ''}
urlVerifyFtp = "https://api.deepkafe.com/faceid/v1/ftp-verify-notice"
dataVerifyFtp = {"ftp_host": "", "ftp_user": "", "ftp_pass": "", "verify_data": [1]}

#Get all user API
# urlGetUsers = "http://new-thd.ddns.net:4000/v1/get_users"
urlGetUsers = "https://api.deepkafe.com/faceid/v1/get_users"

#Register User API
# urlRegister = "http://new-thd.ddns.net:4000/v1/register"
urlRegister = "https://api.deepkafe.com/faceid/v1/register"
dataRegister = {"user_name": "",  "user_id" : "",  "face_images" : [], "videos": [1], "isPortrait": False , "overwrite": True}

#Retrain API
# urlRetrain = "http://new-thd.ddns.net:4000/v1/retrain"
urlRetrain = "https://api.deepkafe.com/faceid/v1/retrain"

#Delete User API
# urlDeleteUser = "http://new-thd.ddns.net:4000/v1/delete_user"
urlDeleteUser = "https://api.deepkafe.com/faceid/v1/delete_user"
dataDeleteUser = {"user_id" : ""}

#Recognize by FTP API
urlRecognize = "https://api.deepkafe.com/faceid/v1/ftp-recognize-notice"
dataRecognize = {"ftp_host": "", "ftp_user": "", "ftp_pass": "", "recognize_data": [""]}

typeHeaderApi = {'Content-Type': 'application/json', 'Authorization':''}

#Retrain clound API
# urlRetrainClound = "http://new-thd.ddns.net:4000/v1/cloud-recognize-retrain"
urlRetrainClound = "https://api.deepkafe.com/faceid/v1/cloud-recognize-retrain"


def getToken():
    responseDecodedJson = requests.post(urlLogin, data=json.dumps(userData), headers=typeHeaderLogin)
    #print responseDecodedJson
    responseJson = responseDecodedJson.json()
    if responseJson["message"] == "SUCCESS":
        return responseJson["data"]["authToken"].encode("ascii","replace")
    else:
        return "False"

def getAccess(_startTime, _endTime):
    dataGetAccess["start_time"] = _startTime
    dataGetAccess["end_time"] = _endTime

    typeHeaderApi['Authorization'] = 'Bearer ' + getToken()
    responseDecodedJson = requests.post(urlGetAccess, data=json.dumps(dataGetAccess), headers=typeHeaderApi)
    responseJson = responseDecodedJson.json()
    return responseJson

def verifyFace(_base64Image, _id):
    dataVerify['image'] = _base64Image
    dataVerify['verify_id'] = _id
    _token = getToken()
    if _token == "False":
        return "False"
    typeHeaderApi['Authorization'] = 'Bearer ' + _token
    responseDecodedJson = requests.post(urlVerify, data=json.dumps(dataVerify), headers=typeHeaderApi)
    responseJson = responseDecodedJson.json()
    return responseJson

def verifyFaceFtp(_ftpHost, _ftpUser, _ftpPass, _imageFtp, _ID):
    dataVerifyFtp['ftp_host'] = _ftpHost
    dataVerifyFtp['ftp_user'] = _ftpUser
    dataVerifyFtp['ftp_pass'] =_ftpPass
    dataVerifyFtp['verify_data'][0] = [_imageFtp,_ID]
    _token = getToken()
    if _token == "False":
        return "False"
    typeHeaderApi['Authorization'] = 'Bearer ' + _token
    responseDecodedJson = requests.post(urlVerifyFtp, data=json.dumps(dataVerifyFtp), headers=typeHeaderApi)
    responseJson = responseDecodedJson.json()
    return responseJson

def getAllUsers():
    typeHeaderApi['Authorization'] = 'Bearer ' + getToken()
    responseDecodedJson = requests.get(urlGetUsers, headers=typeHeaderApi)
    responseJson = responseDecodedJson.json()
    return responseJson

def registerUser(_username, _userId, _videosbase64, _isPortrait, _overwrite):
    _token = getToken()
    if _token == "False":
        return "False"
    typeHeaderApi['Authorization'] = 'Bearer ' + _token
    dataRegister["user_name"] = _username
    dataRegister["user_id"] = _userId
    #dataRegister["face_images"][0] = _faceImage
    dataRegister["videos"][0] = _videosbase64
    dataRegister["isPortrait"] = _isPortrait
    dataRegister["overwrite"] = _overwrite
    #print dataRegister
    responseDecodedJson = requests.post(urlRegister, data=json.dumps(dataRegister), headers=typeHeaderApi)
    #print responseDecodedJson
    responseJson = responseDecodedJson.json()
    return responseJson

def deleteUser(_userId):
    typeHeaderApi['Authorization'] = 'Bearer ' + getToken()
    dataDeleteUser["user_id"] = _userId
    responseDecodedJson = requests.post(urlDeleteUser, data=json.dumps(dataDeleteUser), headers=typeHeaderApi)
    responseJson = responseDecodedJson.json()
    return responseJson

def recognizeFaceFtp(_ftpHost, _ftpUser, _ftpPass, _imageFtp):
    dataRecognize["ftp_host"] = _ftpHost
    dataRecognize["ftp_user"] = _ftpUser
    dataRecognize["ftp_pass"] =_ftpPass
    dataRecognize["recognize_data"][0] = _imageFtp
    _token = getToken()
    if _token == "False":
        return "False"
    typeHeaderApi['Authorization'] = 'Bearer ' + _token
    #print dataRecognize
    responseDecodedJson = requests.post(urlRecognize, data=json.dumps(dataRecognize), headers=typeHeaderApi)
    responseJson = responseDecodedJson.json()
    return responseJson

def reTrain():
    _token = getToken()
    if _token == "False":
        return "False"
    typeHeaderApi['Authorization'] = 'Bearer ' + _token
    responseDecodedJson = requests.get(urlRetrain, headers=typeHeaderApi)
    responseJson = responseDecodedJson.json()
    return responseJson

def reTrainClound():
    _token = getToken()
    if _token == "False":
        return "False"
    typeHeaderApi['Authorization'] = 'Bearer ' + _token
    responseDecodedJson = requests.get(urlRetrainClound, headers=typeHeaderApi)
    responseJson = responseDecodedJson.json()
    return responseJson
    

########################################################################
def saveImageFtp(_host,_user,_pass,_path,_image):
    FtpImage = "Image_" + datetime.now().strftime("%b-%d-%Y_%H_%M_%S")+".jpg"
    if not os.path.isfile(_image):
        print "Image path from Mqtt is not exist"
        return False
    fp = open(_image, 'rb')
    ftp.connect(_host)
    ftp.login(_user,_pass)
    ftp.cwd(_path)
    ftp.storbinary('STOR %s' % FtpImage, fp)
    fp.close()
    ftp.quit()
    return (_path + "/" + FtpImage)

flag_1 = False
flag_2 = False
_dataWriteMainApp = {"source":"APIGetPost","func":"screen","data":{"company":"","name":"","ID":"","mess":""}}
_dataWriteAudioPlay = {"source":"APIGetPost","func":"play","data":""}
_dataWriteGPIO = {"source":"APIGetPost","func":"blinkLed","data":0}


print "APIGetPost"
ImageBase64 = ""
IDCardNumber = ""
ftp = FTP()
ftp.set_debuglevel(2)
ftpHost = "new-thd.ddns.net"
ftpUser = "ltkftp"
ftpPass = "aNdIcKerbanDeNUmBEtIcYoFUraTHe"
ftpPath = "/files/save/in"

while True:
    _waitData = Mqtt.getData()
    if (_waitData != None): 
        if (_waitData.find('source') != -1) & (_waitData.find('func') != -1):
            waitData = json.loads(_waitData)
            if (waitData["source"] == "MainApp") & (waitData["func"] == "recognize"):
                _ImageBase64 = waitData["data"]["base64image"]
                IDCardNumber = waitData["data"]["ID"]
                if IDCardNumber == "0250879771":
                    FlagType = "recognize"
                    _ImageBase64 = waitData["data"]["base64image"]
                    IDCardNumber = waitData["data"]["ID"]
                    # FtpImage = "Image_" + datetime.now().strftime("%b-%d-%Y_%H_%M_%S")+".jpg"
                    # fp = open(_ImageBase64, 'rb')
                    # ftp.connect(ftpHost)
                    # ftp.login(ftpUser,ftpPass)
                    # ftp.cwd(ftpPath)
                    # ftp.storbinary('STOR %s' % FtpImage, fp)
                    # fp.close()
                    # ftp.quit()
                    FtpImage = saveImageFtp(ftpHost,ftpUser,ftpPass,ftpPath,_ImageBase64)
                    #print "start"
                    if FtpImage == False:
                        continue
                    _timeStart = time.time()
                    _respont = recognizeFaceFtp(ftpHost,ftpUser,ftpPass,FtpImage)
                    _timeStop = time.time()
                    if os.path.isfile('/home/pi/maychamcong/log.txt'):
                        data = open('/home/pi/maychamcong/log.txt', 'a')
                        print _timeStop-_timeStart
                        now = datetime.now()
                        data.write("RecognizeFace " + str(now.strftime("%m/%d/%Y, %H:%M:%S:\n")))
                        data.write(str('total run-time of API in second: %fs\n\n' % (_timeStop-_timeStart)))
                        data.close()
                    else:
                        print "file log.txt is not exist"
                    print _respont
                    if (_respont["message"] == "SUCCESS"):
                        if (len( _respont["data"]["result"][0]["recognition"]) != 0):
                            #print _respont["data"]["result"][0]["recognition"][0]["score"]
                            _score = _respont["data"]["result"][0]["recognition"][0]["score"]
                            if _score == -1:
                                _dataWriteMainApp["data"]["mess"] = u"chào bạn! mời bạn đến quầy đăng ký thông tin"
                                _dataWriteAudioPlay["data"] = u"chào bạn mời bạn đến quầy đăng ký thông tin"
                                _dataWriteGPIO["data"] = 2
                            else:
                                _dataWriteMainApp["data"]["mess"] = _respont["data"]["result"][0]["message"] + "score = " + str("%.2f" % (_score*100)) + "%"
                                _dataWriteAudioPlay["data"] =  u"xin chào " + _respont["data"]["result"][0]["recognition"][0]["name"] + u" mời bạn vào"
                                _dataWriteGPIO["data"] = 5
                            _dataWriteMainApp["data"]["name"] = _respont["data"]["result"][0]["recognition"][0]["name"]
                            _dataWriteMainApp["data"]["company"] = userData["username"]
                            _dataWriteMainApp["data"]["ID"] = _respont["data"]["result"][0]["recognition"][0]["user_id"]
                            Mqtt.MqttPathPublish = "MainApp"
                            Mqtt.mqttPublish(json.dumps(_dataWriteMainApp))
                            #_dataWriteAudioPlay["data"] = "moibanvao"
                            Mqtt.MqttPathPublish = "AudioPlay"
                            Mqtt.mqttPublish(json.dumps(_dataWriteAudioPlay))
                            Mqtt.MqttPathPublish = "GPIO"
                            Mqtt.mqttPublish(json.dumps(_dataWriteGPIO))

                        else:
                        #elif (len( _respont["data"]["result"][0]["recognition"]) == 0):
                            _dataWriteMainApp["data"]["mess"] = _respont["data"]["result"][0]["message"] + u"camera chưa thấy mặt bạn"
                            _dataWriteMainApp["data"]["name"] = ""
                            _dataWriteMainApp["data"]["company"] = ""
                            _dataWriteMainApp["data"]["ID"] = ""
                            Mqtt.MqttPathPublish = "MainApp"
                            Mqtt.mqttPublish(json.dumps(_dataWriteMainApp))
                            _dataWriteAudioPlay["data"] = u"camera chưa thấy mặt bạn"
                            Mqtt.MqttPathPublish = "AudioPlay"
                            Mqtt.mqttPublish(json.dumps(_dataWriteAudioPlay))
                            _dataWriteGPIO["data"] = 3
                            Mqtt.MqttPathPublish = "GPIO"
                            Mqtt.mqttPublish(json.dumps(_dataWriteGPIO))

                    else:
                        _dataWriteMainApp["data"]["mess"] = u"server đang gặp lỗi!"
                        _dataWriteMainApp["data"]["name"] = ""
                        _dataWriteMainApp["data"]["company"] = ""
                        _dataWriteMainApp["data"]["ID"] = ""
                        Mqtt.MqttPathPublish = "MainApp"
                        Mqtt.mqttPublish(json.dumps(_dataWriteMainApp))
                        _dataWriteAudioPlay["data"] = u"server đang gặp lỗi"
                        Mqtt.MqttPathPublish = "AudioPlay"
                        Mqtt.mqttPublish(json.dumps(_dataWriteAudioPlay))
                        _dataWriteGPIO["data"] = 1
                        Mqtt.MqttPathPublish = "GPIO"
                        Mqtt.mqttPublish(json.dumps(_dataWriteGPIO))

                else:
                    FlagType = "verify"
                    #with open(_ImageBase64) as image_file:
                    #    ImageBase64 = base64.b64encode(image_file.read())
                    _ImageBase64 = waitData["data"]["base64image"]
                    IDCardNumber = waitData["data"]["ID"]
                    # FtpImage = "Image_" + datetime.now().strftime("%b-%d-%Y_%H_%M_%S")+".jpg"
                    # fp = open(_ImageBase64, 'rb')
                    # ftp.connect(ftpHost)
                    # ftp.login(ftpUser,ftpPass)
                    # ftp.cwd(ftpPath)
                    # ftp.storbinary('STOR %s' % FtpImage, fp)
                    # fp.close()
                    # ftp.quit()
                    FtpImage = saveImageFtp(ftpHost,ftpUser,ftpPass,ftpPath,_ImageBase64)
                    #print "start"
                    if FtpImage == False:
                        continue
                    _timeStart = time.time()
                    #print "start request"
                    #__respont =  verifyFace(ImageBase64,IDCardNumber)
                    __respont = verifyFaceFtp(ftpHost,ftpUser,ftpPass,FtpImage,IDCardNumber)
                    _timeStop = time.time()
                    if os.path.isfile('/home/pi/maychamcong/log.txt'):
                        data = open('/home/pi/maychamcong/log.txt', 'a')
                        print _timeStop-_timeStart
                        now = datetime.now()
                        data.write("RecognizeFace " + str(now.strftime("%m/%d/%Y, %H:%M:%S:\n")))
                        data.write(str('total run-time of API in second: %fs\n\n' % (_timeStop-_timeStart)))
                        data.close()
                    else:
                        print "file log.txt is not exist"
                    print __respont
                    if __respont["message"] == "SUCCESS":
                        #print __respont
                        if __respont["data"]["result"][0]["message"] == "Matched":
                        #if __respont["data"]["message"] == "Matched":
            #		    	print IDCardNumber
                            _dataWriteGPIO["data"] = 5
                            #_dataWriteMainApp["data"]["mess"] = "Moi Ban Vao!"
                            #_dataWriteMainApp["data"]["name"] = __respont["data"]["user_data"]["user_name"]
                            _dataWriteMainApp["data"]["mess"] = "score: " + str("%.2f" % (__respont["data"]["result"][0]["score"]*100)) + u"% => Mời bạn vào!"
                            _dataWriteMainApp["data"]["name"] = __respont["data"]["result"][0]["user_data"]["user_name"]
                            _dataWriteMainApp["data"]["company"] = userData["username"]
                            _dataWriteMainApp["data"]["ID"] = IDCardNumber
                            _dataWriteAudioPlay["data"] = u"xin chào " + __respont["data"]["result"][0]["user_data"]["user_name"] + u" mời bạn vào"
                        elif __respont["data"]["result"][0]["message"] == "Not matched":
                        #if __respont["data"]["message"] == "Not matched":
                            _dataWriteGPIO["data"] = 4
                            _dataWriteMainApp["data"]["mess"] = "score: " + str("%.2f" % (__respont["data"]["result"][0]["score"]*100)) + u"% => Bạn cầm nhầm thẻ rồi!"
                            _dataWriteMainApp["data"]["name"] = ""
                            _dataWriteMainApp["data"]["company"] = ""
                            _dataWriteMainApp["data"]["ID"] = IDCardNumber
                            _dataWriteAudioPlay["data"] = u"bạn cầm nhầm thẻ rồi"
                        elif __respont["data"]["result"][0]["message"] == "there is no user presented verify id":
                        #if __respont["data"]["message"] == "there is no user presented verify id":
                            _dataWriteGPIO["data"] = 2
                            _dataWriteMainApp["data"]["mess"] = u"thẻ không hợp lệ!"
                            _dataWriteMainApp["data"]["name"] = ""
                            _dataWriteMainApp["data"]["company"] = ""
                            _dataWriteMainApp["data"]["ID"] = IDCardNumber
                            _dataWriteAudioPlay["data"] = u"thẻ không hợp lệ"
                        elif __respont["data"]["result"][0]["message"] == "There is not any face in the image":
                        #if __respont["data"]["message"] == "There is not any face in the image":
                            _dataWriteGPIO["data"] = 3
                            _dataWriteMainApp["data"]["mess"] = u"Camera chưa thấy mặt bạn!"
                            _dataWriteMainApp["data"]["name"] = ""
                            _dataWriteMainApp["data"]["company"] = ""
                            _dataWriteMainApp["data"]["ID"] = IDCardNumber
                            _dataWriteAudioPlay["data"] = u"camera chưa thấy mặt bạn"
                        else:
                            _dataWriteGPIO["data"] = 1
                            _dataWriteMainApp["data"]["mess"] = u"server gặp lỗi!"
                            _dataWriteMainApp["data"]["name"] = ""
                            _dataWriteMainApp["data"]["company"] = ""
                            _dataWriteMainApp["data"]["ID"] = IDCardNumber
                            # Mqtt.MqttPathPublish = "MainApp"
                            # Mqtt.mqttPublish(json.dumps(_dataWriteMainApp))
                            _dataWriteAudioPlay["data"] = u"server đang gặp lỗi rồi"
                            # Mqtt.MqttPathPublish = "AudioPlay"
                            # Mqtt.mqttPublish(json.dumps(_dataWriteAudioPlay))

                        Mqtt.MqttPathPublish = "MainApp"
                        Mqtt.mqttPublish(json.dumps(_dataWriteMainApp))
                        Mqtt.MqttPathPublish = "GPIO"
                        Mqtt.mqttPublish(json.dumps(_dataWriteGPIO))
                        Mqtt.MqttPathPublish = "AudioPlay"
                        Mqtt.mqttPublish(json.dumps(_dataWriteAudioPlay))
                    else:
                        _dataWriteMainApp["data"]["mess"] = u"server đang gặp lỗi!"
                        _dataWriteMainApp["data"]["name"] = ""
                        _dataWriteMainApp["data"]["company"] = ""
                        _dataWriteMainApp["data"]["ID"] = IDCardNumber
                        Mqtt.MqttPathPublish = "MainApp"
                        Mqtt.mqttPublish(json.dumps(_dataWriteMainApp))
                        _dataWriteAudioPlay["data"] = u"server đang gặp lỗi rồi"
                        Mqtt.MqttPathPublish = "AudioPlay"
                        Mqtt.mqttPublish(json.dumps(_dataWriteAudioPlay))
                        _dataWriteGPIO["data"] = 1
                        Mqtt.MqttPathPublish = "GPIO"
                        Mqtt.mqttPublish(json.dumps(_dataWriteGPIO))
                print "done"

            elif (waitData["source"] == "MainApp") & (waitData["func"] == "register"):
                _ID = waitData["data"]["ID"]
                _userName = waitData["data"]["username"]
                _VideoBase64 = waitData["data"]["base64video"]
                _ImageBase64 = waitData["data"]["base64image"]
                print "start register"
                if not os.path.isfile(_VideoBase64):
                    print "Image path from Mqtt is not exist"
                    continue
                videoFile = open(_VideoBase64,"rb")
                VideoBase64 = base64.b64encode(videoFile.read())
                videoFile.close()
                #print VideoBase64
                _respont = registerUser(_userName,_ID,VideoBase64,False,True)
                print _respont
                if _respont["message"] == "SUCCESS":
                    FtpImage = saveImageFtp(ftpHost,ftpUser,ftpPass,ftpPath,_ImageBase64)
                    if FtpImage == False:
                        continue
                    _timeStart = time.time()
                    __respont = verifyFaceFtp(ftpHost,ftpUser,ftpPass,FtpImage,_ID)
                    _timeStop = time.time()
                    if os.path.isfile('/home/pi/maychamcong/log.txt'):
                        data = open('/home/pi/maychamcong/log.txt', 'a')
                        print _timeStop-_timeStart
                        now = datetime.now()
                        data.write("verify " + str(now.strftime("%m/%d/%Y, %H:%M:%S:\n")))
                        data.write(str('total run-time of API in second: %fs\n\n' % (_timeStop-_timeStart)))
                        data.close()
                    else:
                        print "file log.txt is not exist"
                    if __respont["message"] == "SUCCESS":
                        #print __respont
                        if __respont["data"]["result"][0]["message"] == "Matched":
                            print "start train"
                            _respontRetraint = reTrainClound()
                            if _respontRetraint["message"] == "SUCCESS":
                                print "train success clound"
                            else:
                                print _respontRetraint
                        else:
                            print "image and video is not 1 people"
                    else:
                        print "can't verify image"
                else:
                    print _respont
            else:
                continue
        else:
            continue
    else:
        continue

