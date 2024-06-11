import os
import re

import PIL.Image
import cv2
from PIL import Image
import numpy as np
def reSize():

    for i in os.listdir(os.getcwd()):

        if i.endswith('.png'):
            image = Image.open(i)
            new_size = (2000, 1500)
            resized_image = image.resize(new_size, PIL.Image.LANCZOS)
            resized_image.save(i, optimize=True, quality=500)

            """
            image = Image.open(i)
            new_size = (1200, 900)
            resized_image = image.resize(new_size, PIL.Image.ANTIALIAS)
            resized_image.save(i, optimize=True, quality=500)

        


            image = Image.open(i)
            new_size = (1200, 900)
            resized_image = image.resize(new_size, PIL.Image.ANTIALIAS)
            resized_image.save(i, optimize=True, quality=500)
            
            basewidth = 1080
            img = Image.open(i)
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
            img.save(i)    
            
            img = cv2.imread(i)
            new_ratio = 20000.0 / img.shape[1]
            new_dim = (20000, int(img.shape[0] * new_ratio))
            new_image = cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA)
            cv2.imwrite(i, new_image)
            cv2.waitKey(0)
            
            new_image = Image.open(os.path.join(os.getcwd(), i))
            new_image.thumbnail((900, 1200))
            new_image.save(i)
            """

reSize()