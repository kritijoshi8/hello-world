# -*- coding: utf-8 -*-
"""
Created on Wed May 16 13:38:45 2018

@author: Dell
"""

from PIL import Image
img=Image.open("sample.jpg").convert("L").rotate(270)
w,h = img.size
hw,hh = w/2,h/2
dim = (hw-80, hh-102,hw+80,hh+102)
img = img.crop(dim)
img.thumbnail((75,75))
img.show()
img.save("my_img.jpg")


