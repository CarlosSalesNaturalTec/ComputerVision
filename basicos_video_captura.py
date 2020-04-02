# =====================================================================================
# Captura de Video
# =====================================================================================

# Importação da Biblioteca OpenCV
import cv2

camera_port = 0                             #número da porta do dispositivo (webcam)
camera = cv2.VideoCapture(camera_port)      #metodo para captura de video

# parâmetros do video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('meu_video.avi', fourcc, 20.0, (640,480))

camera_esta_ativa = camera.isOpened()
while (camera_esta_ativa):
    ret, frame = camera.read()
    if ret == True:
        out.write(frame)                         #salva frame / segue gravando video
        cv2.imshow('Meu Video',frame)            #exibe em janela, video sendo capturado/gravado
        if cv2.waitKey(1) & 0xFF == ord('q'):    #aguarda pressionamento de tecla 'q' para interromper
            break
    else:
        break

out.release()                   #libera arquivo (video)
camera.release()                #libera dispositivo
cv2.destroyAllWindows           #fecha janela