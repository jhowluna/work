import numpy as np
from zipfile import ZipFile
import json
import base64

#with ZipFile('image.zip', 'r') as zip:
with open('4000x4000.txt','r') as felipe:
   arq =  felipe.read()

img = base64.b64decode(arq)
with open ('imagefelipe.jpg','wb') as f:
    f.write(img)