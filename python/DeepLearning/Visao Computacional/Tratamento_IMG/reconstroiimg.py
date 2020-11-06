import numpy as np
from zipfile import ZipFile
import json
import cv2

class openimg():
    def __init__(self,imagemzip,imagem):
        with ZipFile(imagemzip, 'r') as zip:
            arq = open(imagem,'r')
            arq = arq.read()
            arq = json.loads(arq)

        for heigth in arq.keys():
            heigth = heigth.split('_')
            heigth = heigth[0]
            heigth = int(heigth)+1
            

        for width in arq.keys():
            width = width.split('_')
            width = width[1]
            width = int(width)+1
            
        #rq[f'{l}_{c}'] if [arq[f'{l}_{c}'] == [arq[f'{l}_{c}']+1 else([arq[f'{l}_{c}'] = [255,0,0]) for l in range(heigth)]for c in range(width)]
        
        arq = [[arq[f'{l}_{c}'] for l in range(heigth)]for c in range(width)]
        arq = np.uint8(arq)
        #arq = [arq[f'{l}_{c}'] if(arq[f'{l+1}_{c}']==arq[f'{l}_{c}']) else(np.uint8([255,0,0])) for l in range(width) for c in range(heigth)]

        cv2.cvtColor(arq,cv2.COLOR_BGR2RGB)
        cv2.imshow('image',arq)
        cv2.waitKey(0)
        cv2.imwrite('teste.jpg',arq)

openimg('jhonatan.zip','jhonatan.txt')

