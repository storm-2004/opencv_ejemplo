""" Este codigo due echo de acuerdo a la documentacion de opencv """

import cv2
from numpy import true_divide

caras_harcascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

bandera= True;

while bandera:
    _, img = cap.read()
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    cara = caras_harcascade.detectMultiScale(gris,1.1,4);
    
    for (x,y,w,h) in cara:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0 ,0) ,2)
    cv2.imshow("img", img)
    k = cv2.waitKey(30)
    if k == 27:
        break
cap.release()
        
     
