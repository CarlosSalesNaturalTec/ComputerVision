#=====================================================================================
# Detecção de faces (rostos) em imagem
#=====================================================================================

# Importação da Biblioteca OpenCV
import cv2

# Importa Classificador "CascadeClassifier"
# necessário que o arquivo haarcascade_frontalface_default.xml esteja na pasta do projeto. baixar do github/opencv
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('image1.jpg')                          #faz a leitura da imagem
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)            #converte imagem para escala de cinzas
faces = face_cascade.detectMultiScale(gray, 1.1, 4)     #detecta face

for (x,y,w,h) in faces:                                 #desenha um retângulo em volta de cada face existente na imagem
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),3)

cv2.imshow('Face detection example',img)                #exibe a imagem em uma janela
cv2.waitKey(0)                                          #aguarda que seja pressionada qualquer tecla
cv2.destroyAllWindows                                   #fecha janela
