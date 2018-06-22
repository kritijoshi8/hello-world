# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:43:13 2018

@author: Dell
"""
import requests
import json

data = {"Phone_Number":"0123456789",
        "Name": "Kriti",
        "College_Name":"SKIT",
        "Branch":"Information Technology"
        }
data = json.dumps(data)#DUMPS AND LOADS:,dumps converts from data to json format and loads convert from json format to data.
headers = {"Content-Type":"application/json"}

send_req=requests.post("http://13.127.155.43/api_v0.1/sending",data = data,headers=headers)
print (send_req.text)

url="http://13.127.155.43/api_v0.1/receiving"
url+="?Phone_Number=0123456789"
receive_req=requests.get(url)
print receive_req.text