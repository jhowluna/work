import sys
import signal
import cv2

end = False

# --------------------------------------
def signal_handler(signal, frame):
    global end
    end = True

# --------------------------------------
cap = cv2.VideoCapture(0)

# Tenta abrir a webcam, e já falha se não conseguir
if not cap.isOpened():
    print('Não foi possível abrir a web cam.')
    sys.exit(-1)

# Cria o arquivo de video de saída
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

# Captura o sinal de CTRL+C no terminal
signal.signal(signal.SIGINT, signal_handler)
print('Capturando o vídeo da webcam -- pressione Ctrl+C para encerrar...')

# Processa enquanto o usuário não encerrar (com CTRL+C)
while(not end):
    ret, frame = cap.read()
    if ret:
        out.write(frame)
    else:
        print('Oops! A captura falhou.')
        break

print('Captura encerrada.')

# Encerra tudo
cap.release()
out.release()
