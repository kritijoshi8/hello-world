# -*- coding: utf-8 -*-
"""
Created on Wed May 30 23:01:06 2018

@author: Dell
"""

import requests
import re
from pymongo import MongoClient 

client = MongoClient('localhost',27017)

number=raw_input("enter the number")
message=raw_input("enter the message") 

if re.match(r'^[0-9+]\d{12}$',number):
    send_url= "https://api.mlab.com/api/1/databases/mydatabase/collections/student?apiKey=Xhbte_NFryGyiASxZQEGDet7aXrWNexx"
    send_url2="https://smsapi.engineeringtgr.com/send/?Mobile=9982920322&Password=khatu12345&Key=joshi4vXAmniNxhJodLHU&Message="+message+"&To="+number
    data={
          "Number" : number,
          "Message" : message
          }
    send_req=requests.post(send_url,json=data)
    send_req1=requests.post(send_url2)
    print send_req.text
    print send_req1.text
else:
    print "the mobile number is not valid"