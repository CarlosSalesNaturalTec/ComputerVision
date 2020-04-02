# =====================================================================================
# Captura Imagem 
# =====================================================================================

# Importação da Biblioteca OpenCV
import cv2

nome_arquivo = "minha_foto.png"         #nome do arquivo a ser gravado
camera_port = 0                         #número da porta do dispositivo (webcam)
camera = cv2.VideoCapture(camera_port)  #metodo para captura de video

while (camera.isOpened()):
    ret, frame = camera.read()
    if ret == True:
        cv2.imshow('Captura de Foto. Pressione "S" para SALVAR foto',frame)  #exibe em janela, imagem sendo capturada
        if cv2.waitKey(1) & 0xFF == ord('s'):       #aguarda pressionamento de tecla 'S' para salvar foto
            cv2.imwrite(nome_arquivo, frame)        #salva foto
            break
    else:
        break

camera.release()                #Libera dispositivo
cv2.destroyAllWindows           #Fecha Janela