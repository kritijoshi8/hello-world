# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:40:57 2018

@author: Dell
"""

import requests


data = {
        "Phone_Number":"1234567",
        "Name":"jannat",
        "College_Name":"SKIT",
        "Branch":"IT"
        }

send_url= "https://api.mlab.com/api/1/databases/mydatabase/collections/student?apiKey=Xhbte_NFryGyiASxZQEGDet7aXrWNexx"
send_req= requests.post(send_url,json = data)
print send_req.text

