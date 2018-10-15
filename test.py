#coding=utf-8
import requests
import json
import base64
import os
import wav2pcm
import sys
baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
grant_type = "client_credentials"
#API Key
client_id = "aMTBj0VxArQlLtNcbALiG7QV"
#Secret Key
client_secret = "ybr2YatdUy5XEZp8mvYkwQH1ML1YY1eo"

#拼url
url ="%sgrant_type=%s&client_id=%s&client_secret=%s"%(baidu_server,grant_type,client_id,client_secret)
print(url)
#获取token
res = requests.post(url)
print(res.text)
token = json.loads(res.text)["access_token"]
print(token)
#24.b891f76f5d48c0b9587f72e43b726817.2592000.1524124117.282335-10958516
#设置格式
RATE = "16000"
FORMAT = "pcm"
CUID="raspberry"
DEV_PID="1536"


a=sys.argv[1]
#以字节格式读取文件之后进行编码
with open(a, "rb") as f:
    speech = base64.b64encode(f.read()).decode('utf8')
size = os.path.getsize(a)
headers = { 'Content-Type' : 'application/json'}
url = "https://vop.baidu.com/server_api"
data={

        "format":FORMAT,
        "rate":RATE,
        "dev_pid":DEV_PID,
        "speech":speech,
        "cuid":CUID,
        "len":size,
        "channel":1,
        "token":token,
    }

req = requests.post(url,json.dumps(data),headers)
result = json.loads(req.text)
print(result["result"][0])
