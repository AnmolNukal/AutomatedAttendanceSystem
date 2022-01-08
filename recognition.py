import cv2
import numpy as np
import time
import sys

start = time.time()
period = 8
face_cas = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')

# replace 0 with any video file

cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("C:/Users/anmol/OneDrive/Desktop/BE Project/trainer.yml")
flag = 0
id = 0
filename = 'filename'
dict = {
    'item1': 1
}

font = cv2.FONT_HERSHEY_SIMPLEX
f = open("myfile.txt", "w")

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray, 1.3, 7)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        id, conf = recognizer.predict(roi_gray)
        if (conf < 50):
            if (id == 25):
                id = 'JOHN'
                print("John Doe")
            if (id == 57):
                id = 'Anmol'
                print("Anmol")
                f.write("Anmol Present")
                break
            if (id == 6):
                id = 'Anita'
                print("Anita")
            if (id == 10):
                id = 'Test'
                print("Test Doe")
                break

        else:
            id = 'Unknown, can not recognize'
            flag = flag + 1
            break

        cv2.putText(img, str(id) + " " + str(conf),
                    (x, y - 10), font, 0.55, (120, 255, 120), 1)
        # cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255));
    cv2.imshow('frame', img)
    # cv2.imshow('gray',gray);
    if flag == 10:
        print("Transaction Blocked")
        break
    if time.time() > start + period:
        break
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
