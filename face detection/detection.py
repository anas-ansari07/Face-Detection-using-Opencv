import cv2

#haarcascade files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

#input the image
img = cv2.imread(r"C:/Users/DDKG/Downloads/project.jpg")

#converting into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detecting face and smile                  #scalingFactor,neighbour
faces= face_cascade.detectMultiScale(gray, 1.3, 4)
smiles= smile_cascade.detectMultiScale(gray,1.8, 20)

#making rectangle           #x&y-upperleftcorner w&h-lowerrightcorner
for(x, y, w, h) in faces: 
    cv2.rectangle(img, (x,y), ((x+w), (y+h)), (255, 0, 0), 3)
    
for(sx, sy, sw, sh) in smiles:
    cv2.rectangle(img, (sx,sy), ((sx+sw), (sy+sh)), (0, 0, 255), 2)    

#showing output
cv2.imshow('img', img)
cv2.waitKey()
    
    
        