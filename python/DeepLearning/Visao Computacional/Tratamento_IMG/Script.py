import cv2
import zipfile
import json

image = cv2.imread('download.jpg')

width = len(image)
height = len(image[0])  
lista = {}


for i in range(width):
    for a in range(height):
        #print (f'altura: {a} largura: {i} {arrimg[a][i]}' )
        #json_data = f'{a} {i} {arrimg[i][a]}'
        json_data = {f'{a}_{i}' :f'{image[i][a]}'}
        lista.update(json_data)

with open ("jhonatan.txt","w" ) as escritor:
    json.dump(lista,escritor)
escritor.close()

zipar = zipfile.ZipFile('Jhonatan.zip', 'w')
zipar.write('jhonatan.txt', compress_type=zipfile.ZIP_DEFLATED)