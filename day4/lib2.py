# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:09:08 2018

@author: Dell
"""

from PIL import Image

#Saving the file in different format
img_filename=Image.open("chip.jpg")
img_filename.show()

from PIL import ImageFilter
img_filename.filter(ImageFilter.CONTOUR).show()

img_filename.mode