import sys
import dlib
import cv2

pula_quadros = 10
captura = cv2.VideoCapture(0)
contadorQuadros = 0
detector = dlib.simple_object_detector("recursos/Pessoas.svm")
detectorPontos = dlib.shape_predictor("recursos/Pessoas.dat")
font = cv2.FONT_HERSHEY_SIMPLEX
# fontScale
fontScale = 0.7

# Blue color in BGR
color = (0, 255, 0)

# Line thickness of 2 px
thickness = 2

def imprimirPontos(imagem, pontos):
    for p in pontos.parts():
        cv2.circle(imagem, (p.x, p.y), 3, (0, 0, 0))
    for i in range(6):
        points = pontos.parts()
        a = points[i]
        try:
            b = points[i+1]
        except:
            b = points[0]

        cv2.line(imagem,(a.x,a.y),(b.x,b.y),color,thickness)



while captura.isOpened():
    conectado, frame = captura.read()
    contadorQuadros += 1
    if contadorQuadros % pula_quadros == 0:
        objetosDetectados = detector(frame, 1)
        for o in objetosDetectados:
            e, t, d, f = (int(o.left()), int(o.top()), int(o.right()), int(o.bottom()))
            #cv2.rectangle(frame, (e, t), (d, f), (0, 255, 0), 2)
            cv2.putText(frame, 'Mascara Identificada', (e,t-5), font, fontScale, color, thickness, cv2.LINE_AA)
            pontos = detectorPontos(frame, o)
            imprimirPontos(frame, pontos)
        cv2.imshow("Preditor de Objetos", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

captura.release()
cv2.destroyAllWindows()
sys.exit(0)
