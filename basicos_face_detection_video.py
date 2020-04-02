#=====================================================================================
# Detecção de faces (rostos) em vídeos em tempo real
#=====================================================================================

# Importação da Biblioteca OpenCV
import cv2

# Importa Classificador "CascadeClassifier"
# necessário que o arquivo haarcascade_frontalface_default.xml esteja na pasta do projeto. baixar do github/opencv
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Abre dispositivo de vídeo (webcam)
camera = cv2.VideoCapture(0)

while camera.isOpened():
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)          #converte imagem para escala de cinzas
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)     #detecta faces
    
    for (x,y,w,h) in faces:                                 #desenha um retângulo em volta de cada face
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),3)
    
    cv2.imshow('Video com Face Detection',frame)            #exibe vídeo

    if cv2.waitKey(1) & 0xFF == ord('s'):                   #aguarda que seja pressionada tecla "S" para fechar janela
        break

camera.release()                                            #libera dispositivo
cv2.destroyAllWindows                                       #fecha janela