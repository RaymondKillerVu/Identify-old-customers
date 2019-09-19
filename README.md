# Identify-old-customers
API with face verify and recognize

cách sử dụng API:

RECOGINZE IMAGE:
PUBLISH: TOPIC "APIGetPost"
DATA IN STRING:
 {
   "source": "MainApp",
   "func": "recognize",
   "data": {
     "base64image": "string of path to image"
   }
 }
=> RETURN
SUBCRISE: TOPIC 'MainApp'
{
  'source': 'APIGetPost',
  'func': 'recognize', 
  'data': [{
    'box': [xmin, ymin, xmax, ymax],
    'name': 'user name/Unknown',
    'mess': 'some error or message',
    'company': 'name of user device',
    'score': float number,
    'ID': 'User's ID/Unknown'
  }, {
    'box': [xmin, ymin, xmax, ymax],
    'name': 'user name/Unknown',
    'mess': 'some error or message',
    'company': 'name of user device',
    'score': float number,
    'ID': 'User's ID/Unknown'
  }, {
    'box': [xmin, ymin, xmax, ymax],
    'name': 'user name/Unknown',
    'mess': 'some error or message',
    'company': 'name of user device',
    'score': float number,
    'ID': 'User's ID/Unknown'
  }...
  ]
}

*************************************************************
REGISTER NEW USER BY VIDEO:
PUBLISH: TOPIC "APIGetPost"
DATA IN STRING:
{
  "source": "MainApp",
  "func": "register",
  "data": {
    "username": "name of new user",
    "ID": "id of new user",
    "base64video": "link to path of video to register",
    "base54image": "link to path of image to register"
    "isportrait" : false
    "overwrite": true    
  }
}
**NOTE: isportrait is only affects videos, false for pc or laptop
        if overwrite is true and there is an user matched user_id, user information will be overwrite.
=> RETURN
SUBCRISE: TOPIC 'MainApp'
{
  'source': 'APIGetPost',
  'func': 'register',
  'data': {
    'mess': 'some message or error',
    'ID': 'return id if register successfull'
  }
}
**NOTE: some type of mess:  "user is added but no training" => can not train
                            "user is not math with video" => image and video is not 1 people
                            "can not verify image with user" => can not verify to train
                            "can not register,maybe video to large" => register fails
                            "user is added and ready to use" => all successfull, ID will return

*************************************************************
DELETE AN USER:
PUBLISH: TOPIC "APIGetPost"
DATA IN STRING:
 {
   "source": "MainApp",
   "func": "deleteuser",
   "data": {
     "ID": "ID of user to delete",
   }
 }
=> RETURN
SUBCRISE: TOPIC 'MainApp'
{
  'source': 'APIGetPost',
  'func': 'deleteuser',
  'data': {
    'mess': 'some error or message',
    'ID': 'return id of user deleted'
  }
}

*************************************************************
VERIFY IMAGE:
PUBLISH: TOPIC "APIGetPost"
DATA IN STRING:
 {
   "source": "MainApp",
   "func": "verify",
   "data": {
     "ID": "ID of this user",
     "base64image": "string of path to image"
   }
 }
=> RETURN
SUBCRISE: TOPIC 'MainApp'
{
  'source': 'APIGetPost',
  'data': {
    'box': [xmin, ymin, xmax, ymax],
    'name': 'user name',
    'mess': 'some error or message',
    'company': 'name of user device',
    'score': float number,
    'ID': 'id of user'
  },
  'func': 'verify'
}

*************************************************************
GET ALL USER:
PUBLISH: TOPIC "APIGetPost"
DATA IN STRING:
{
  'source': 'MainApp',
  'func': 'getalluser',
}
=> RETURN
SUBCRISE: TOPIC 'MainApp'
{
  'source': 'APIGetPost',
  'func': 'getalluser',
  'data': [{
      'name': 'LamVo',
      'mess': '',
      'pid': '',
      'address': '',
      'ID': '1234',
      'total_faces': 14
    },
    {
      'name': 'killer',
      'mess': '',
      'pid': '',
      'address': '',
      'ID': '321654',
      'total_faces': 5
    },
    {
      'name': 'killer',
      'mess': '',
      'pid': '',
      'address': '',
      'ID': 'raymond',
      'total_faces': 506
    }
  ]
}
