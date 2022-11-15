#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os 
import cv2
import numpy as np 
import tensorflow as tf
from tensorflow import keras 
from tensor.keras.models import load_model


# In[ ]:


#esta primera seccion del codigo sera para darle a la computadora
#la herrramienta de acceder a la camara y crear un registro facial
#del usuario frente a la computadora. 

video = cv2.VideoCapture(0)
df= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
nombreID=str(input("Ingrese su nombre: ")).lower()
path= os.path.exists(path)

if isExist:
    print("Este nombre ya esta en uso")
    nombreID= str(input("Ingrese otro nombre:"))
else:
    os.makedirs(path)
while True:
    ret, frame= video.read()
    rostros = df.detectMultiScale(frame, 1.3, 5)
    for x, y, w, h in faces:
        count= count+1
        nombre='./images/'+ nombreID + '/' + str(count) + '.jpg'
        print("Creando imagenes..." + nombre)
        cv2.imwrite(name, frame[y:y+h, x:x+w])
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow("WindowFrame", frame)
    cv2.wait.key(1)
    if count> 200:
        break
video.realese()
cv2.destroyAllWindows()


# In[ ]:


#Esta segunda parte del codigo es para que la computadora pueda
#entrar en el registro que se creo gracias a la anterior parte 
#del codigo.

df= cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
font = cv2.FONT_HERSHEY_COMPLEX


model = load_model('keras_model.h5')

while True:
    sucess, imgOrignal = cap.read()
    rostros = df.detectMultiScale(imgOrignal, 1.3, 5)
    for x, y, w, h in faces:
        crop_img = imgOrignal[y:y+h, x:x+h]
        img = cv2.resize(crop_img, (224, 224))
        img = img.reshape(1, 224, 224, 3)
        prediccion = model.predict(img)
        classIndex = model.predict_classes(img)
        ValorProbable = np.amax(prediccion)
        if classIndex == 0:
            cv2.rectangle(imgOrignal, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.rectangle(imgOrignal, (x, y-40), (x+w, y), (0, 255, 0), -2)
            cv2.putText(imgOrignal, str(get_className(classIndex)),
                        (x, y-10), font, 0.75, (255, 255, 255), 1, cv2.LINE_AA)
        elif classIndex == 1:
            cv2.rectangle(imgOrignal, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.rectangle(imgOrignal, (x, y-40), (x+w, y), (0, 255, 0), -2)
            cv2.putText(imgOrignal, str(get_className(classIndex)),
                        (x, y-10), font, 0.75, (255, 255, 255), 1, cv2.LINE_AA)

        cv2.putText(imgOrignal, str(round(ValorProbable*100, 2)) +
                    "%", (180, 75), font, 0.75, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("Result", imgOrignal)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

