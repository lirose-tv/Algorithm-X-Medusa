import requests
import time
import json

from types import SimpleNamespace

server = "http://ip:port/api/xSign"
**Contact for api :** [https://t.me/lirose_tv](https://t.me/lirose_tv)
  
## telegram: @lirose_tv

currentTime = time.time()
x_khronos = str(currentTime).split(".")[0]
_rticket = str(int(x_khronos) * 1000).split(".")[0]

url = f"douyin.com, api*.tiktokv.com, api*.fqnovel.com ..."

   
responseGorgon = requests.request("POST", server, data = {
	'token': 'token',
	'url': url,
	'cookies': '1',
	'stub': '1'
}).text

res = json.loads(responseGorgon, object_hook = lambda d: SimpleNamespace(**d))

x_gorgon = res.x_gorgon
x_Ladon = res.x_Ladon
x_Argus = res.x_Argus
x_Medusa = res.x_Medusa
x_Helios = res.x_Helios

print(res)

headers = {
	"X-Gorgon": x_gorgon,
	"X-Argus": x_Argus,
	"X-Ladon": x_Ladon,
	"X-Khronos": x_khronos,
  "X-Medusa": x_Medusa,
  "X-Helios": x_Helios,
	"multi_login": "1",
	"sdk-version": "2",
	"passport-sdk-version": "19",
	"Accept-Encoding": "gzip",
	"X-SS-REQ-TICKET": _rticket,
	"User-Agent": "TikTok 25.4.0 rv:254012 (iPhone; iOS 12.5.5; en_US) Cronet",
	"Host": "",
	"Connection": "Keep-Alive",
	"x-tt-token": ""
}

response = requests.get(url, headers = headers)

print(response.text)
