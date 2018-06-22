# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:31:19 2018

@author: Dell
"""

import facebook as fb

# Facebook Graphic Explorer API user Access Token
access_token = "EAACEdEose0cBABJcJZBS0P5T1PbOfO7OoNSNptsMuY20lGQNKUI9f2T2ZBRHTl4u8YDwnMy393ZALnbD7RQTA68mIO84b7MBdaNaAX3LS4i22exvko7F9voeT8Fx3GdZCTmwZCD9WztrZCSvA3Bz5lmJDCogijPaHIfSowilFZA3jGr46I5ED8wCmpuAIQrb5oZCVZCiwcDXchAZDZD"

# Message to post as status on Facebook
status = "<at forsk>"

# Authenticating
graph = fb.GraphAPI(access_token)

# Posting Status on your wall
post_id = graph.put_wall_post(status)
graph.put_photo(image=open("RFID-chip.jpg","rb"))