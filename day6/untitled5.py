# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:33:20 2018

@author: Dell
"""

from twython import Twython

APP_KEY = 'mjd9CMYbS3Wg7b1yb9YooDVw8'  # Customer Key here
APP_SECRET = 'rmcoIiPMJ02oAFReZpAcJJUOxyT578CSNYKAFlMm2Q6vhvxAZr'  # Customer secret here
OAUTH_TOKEN = '997359327752085505-cYQzTueD4DrAU79S31qU78em3GWhkAU'  # Access Token here
OAUTH_TOKEN_SECRET = 'Y8IEEOIKYH62bWtQVL9jJuLUyOc48dgvk6Jxx4uor2mbf'  # Access Token Secret here

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter.update_status(status="Hello from Python! :D")