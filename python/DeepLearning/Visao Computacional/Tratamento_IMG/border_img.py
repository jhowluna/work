import numpy as np
from zipfile import ZipFile
import json
import cv2


arq = cv2.imread('download.jpg')

cv2.imshow('image',arq)


arq = arq[:,:,2]

# altura = len(arq)-1
# largura = len(arq[0])-1

# #arq = [[arq[c][l] if (arq[c][l].all() == arq[c+1][l].all() or arq[c][l].all() == arq[c][l+1].all()) else [0,0,255] for l in range(largura)] for c in range(altura)]

# for l in range(largura):
#     for c in range(altura):
        
#         if  arq[c][l].all = arq[c+1][l+1].all :
#             arq[c][l] = arq[c][l]
#         else:
#             arq[c][l] = [0,0,255]
            

arq = np.uint8(arq)


cv2.imshow('image',arq)
cv2.waitKey(0)
cv2.imwrite('teste1.jpg',arq)
