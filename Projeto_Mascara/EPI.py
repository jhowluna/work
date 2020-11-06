import dlib
import cv2
import glob
import os

detectorRelogio = dlib.simple_object_detector("recursos/EPI.svm")
# detectorPontosRelogio = dlib.shape_predictor("recursos/detector_relogios_pontos.dat")

# print(dlib.test_shape_predictor("recursos/teste_relogios_pontos.xml", "recursos/detector_relogios_pontos.dat"))

# def imprimirPontos(imagem, pontos):
#     for p in pontos.parts():
#         cv2.circle(imagem, (p.x, p.y), 2, (0, 255, 0))

for arquivo in glob.glob(os.path.join("teste_EPI", "*.jpeg")):
    imagem = cv2.imread(arquivo)
    objetosDetectados = detectorRelogio(imagem, 2)
    for d in objetosDetectados:
        e, t, d, b = (int(d.left()), int(d.top()), int(d.right()), int(d.bottom()))
        cv2.rectangle(imagem, (e,t), (d, b), (0,0,255), 2)
    cv2.imshow("Detector pontos", imagem)
    cv2.waitKey(0)

cv2.destroyAllWindows()