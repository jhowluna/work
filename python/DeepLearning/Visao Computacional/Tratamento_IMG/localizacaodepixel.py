import numpy as np
from zipfile import ZipFile
import json
import cv2

arq = cv2.imread('images.png',0)


altura = len(arq)-1
largura = len(arq[0])-1

arq = [[arq[c][l] if (arq[c][l] == (arq[c+1][l]) or arq[c][l] == (arq[c][l+1])) else 255 for l in range(largura)] for c in range(altura)]

arq = np.uint8(arq)


cv2.cvtColor(arq , cv2.COLOR_GRAY2RGB)
cv2.imshow('image',arq , )
cv2.waitKey(0)
cv2.imwrite('teste1.jpg',arq)
