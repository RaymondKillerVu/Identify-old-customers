<p># Identify-old-customers<br>
API with face verify and recognize</p>

<p>c&aacute;ch s&#7917; d&#7909;ng API:</p>

<p>RECOGINZE IMAGE:<br>
PUBLISH: TOPIC &quot;APIGetPost&quot;<br>
DATA IN STRING:<br>
 {<br>
 &quot;source&quot;: &quot;MainApp&quot;,<br>
 &quot;func&quot;: &quot;recognize&quot;,<br>
 &quot;data&quot;: {<br>
 &quot;base64image&quot;: &quot;string of path to image&quot;<br>
 }<br>
 }<br>
=> RETURN<br>
SUBCRISE: TOPIC 'MainApp'<br>
{<br>
 'source': 'APIGetPost',<br>
 'func': 'recognize', <br>
 'data': [{<br>
 'box': [xmin, ymin, xmax, ymax],<br>
 'name': 'user name/Unknown',<br>
 'mess': 'some error or message',<br>
 'company': 'name of user device',<br>
 'score': float number,<br>
 'ID': 'User's ID/Unknown'<br>
 }, {<br>
 'box': [xmin, ymin, xmax, ymax],<br>
 'name': 'user name/Unknown',<br>
 'mess': 'some error or message',<br>
 'company': 'name of user device',<br>
 'score': float number,<br>
 'ID': 'User's ID/Unknown'<br>
 }, {<br>
 'box': [xmin, ymin, xmax, ymax],<br>
 'name': 'user name/Unknown',<br>
 'mess': 'some error or message',<br>
 'company': 'name of user device',<br>
 'score': float number,<br>
 'ID': 'User's ID/Unknown'<br>
 }...<br>
 ]<br>
}</p>

<p>*************************************************************<br>
REGISTER NEW USER BY VIDEO:<br>
PUBLISH: TOPIC &quot;APIGetPost&quot;<br>
DATA IN STRING:<br>
{<br>
 &quot;source&quot;: &quot;MainApp&quot;,<br>
 &quot;func&quot;: &quot;register&quot;,<br>
 &quot;data&quot;: {<br>
 &quot;username&quot;: &quot;name of new user&quot;,<br>
 &quot;ID&quot;: &quot;id of new user&quot;,<br>
 &quot;base64video&quot;: &quot;link to path of video to register&quot;,<br>
 &quot;base54image&quot;: &quot;link to path of image to register&quot;<br>
 &quot;isportrait&quot; : false<br>
 &quot;overwrite&quot;: true <br>
 }<br>
}<br>
**NOTE: isportrait is only affects videos, false for pc or laptop<br>
 if overwrite is true and there is an user matched user_id, user information will be overwrite.<br>
=> RETURN<br>
SUBCRISE: TOPIC 'MainApp'<br>
{<br>
 'source': 'APIGetPost',<br>
 'func': 'register',<br>
 'data': {<br>
 'mess': 'some message or error',<br>
 'ID': 'return id if register successfull'<br>
 }<br>
}<br>
**NOTE: some type of mess: &quot;user is added but no training&quot; => can not train<br>
 &quot;user is not math with video&quot; => image and video is not 1 people<br>
 &quot;can not verify image with user&quot; => can not verify to train<br>
 &quot;can not register,maybe video to large&quot; => register fails<br>
 &quot;user is added and ready to use&quot; => all successfull, ID will return</p>

<p>*************************************************************<br>
DELETE AN USER:<br>
PUBLISH: TOPIC &quot;APIGetPost&quot;<br>
DATA IN STRING:<br>
 {<br>
 &quot;source&quot;: &quot;MainApp&quot;,<br>
 &quot;func&quot;: &quot;deleteuser&quot;,<br>
 &quot;data&quot;: {<br>
 &quot;ID&quot;: &quot;ID of user to delete&quot;,<br>
 }<br>
 }<br>
=> RETURN<br>
SUBCRISE: TOPIC 'MainApp'<br>
{<br>
 'source': 'APIGetPost',<br>
 'func': 'deleteuser',<br>
 'data': {<br>
 'mess': 'some error or message',<br>
 'ID': 'return id of user deleted'<br>
 }<br>
}</p>

<p>*************************************************************<br>
VERIFY IMAGE:<br>
PUBLISH: TOPIC &quot;APIGetPost&quot;<br>
DATA IN STRING:<br>
 {<br>
 &quot;source&quot;: &quot;MainApp&quot;,<br>
 &quot;func&quot;: &quot;verify&quot;,<br>
 &quot;data&quot;: {<br>
 &quot;ID&quot;: &quot;ID of this user&quot;,<br>
 &quot;base64image&quot;: &quot;string of path to image&quot;<br>
 }<br>
 }<br>
=> RETURN<br>
SUBCRISE: TOPIC 'MainApp'<br>
{<br>
 'source': 'APIGetPost',<br>
 'data': {<br>
 'box': [xmin, ymin, xmax, ymax],<br>
 'name': 'user name',<br>
 'mess': 'some error or message',<br>
 'company': 'name of user device',<br>
 'score': float number,<br>
 'ID': 'id of user'<br>
 },<br>
 'func': 'verify'<br>
}</p>

<p>*************************************************************<br>
GET ALL USER:<br>
PUBLISH: TOPIC &quot;APIGetPost&quot;<br>
DATA IN STRING:<br>
{<br>
 'source': 'MainApp',<br>
 'func': 'getalluser',<br>
}<br>
=> RETURN<br>
SUBCRISE: TOPIC 'MainApp'<br>
{<br>
 'source': 'APIGetPost',<br>
 'func': 'getalluser',<br>
 'data': [{<br>
 'name': 'LamVo',<br>
 'mess': '',<br>
 'pid': '',<br>
 'address': '',<br>
 'ID': '1234',<br>
 'total_faces': 14<br>
 },<br>
 {<br>
 'name': 'killer',<br>
 'mess': '',<br>
 'pid': '',<br>
 'address': '',<br>
 'ID': '321654',<br>
 'total_faces': 5<br>
 },<br>
 {<br>
 'name': 'killer',<br>
 'mess': '',<br>
 'pid': '',<br>
 'address': '',<br>
 'ID': 'raymond',<br>
 'total_faces': 506<br>
 }<br>
 ]<br>
}</p>
