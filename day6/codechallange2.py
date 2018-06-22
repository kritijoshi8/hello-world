# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:03:54 2018

@author: Dell
"""
import oauth2
import time
import urllib2
import json
url1 = "https://api.twitter.com/1.1/search/tweets.json"  

params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }

consumer = oauth2.Consumer(key="mjd9CMYbS3Wg7b1yb9YooDVw8", secret="rmcoIiPMJ02oAFReZpAcJJUOxyT578CSNYKAFlMm2Q6vhvxAZr")

token = oauth2.Token(key="997359327752085505-cYQzTueD4DrAU79S31qU78em3GWhkAU",
                     secret="Y8IEEOIKYH62bWtQVL9jJuLUyOc48dgvk6Jxx4uor2mbf")

params["oauth_consumer_key"] = consumer.key  

params["oauth_token"] = token.key

params["q"]= "jaipur"
req = oauth2.Request(method="GET", url=url1, parameters=params)
signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
req.sign_request(signature_method, consumer, token)
url = req.to_url()
response = urllib2.Request(url)
data = json.load(urllib2.urlopen(response)) 


filename = params["q"]      
f = open(filename + "_File.txt", "w")  
json.dump(data["statuses"], f)
f.close()
