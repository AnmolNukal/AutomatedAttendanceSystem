# Last edited : 25/12/2021

import os
import cv2


def checkPath(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


face_id = input('Enter your roll no ')

camera = cv2.VideoCapture("video.mp4")


face_detector = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')


count = 0

checkPath("C:/Users/anmol/OneDrive/Desktop/BE Project/dataSet/")


while (True):

    _, image_frame = camera.read()

    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        count += 1

        cv2.imwrite("datasets/User." + str(face_id) + '.' +
                    str(count) + ".jpg", gray[y:y + h, x:x + w])

        cv2.imshow('frame', image_frame)

    #
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    elif count >= 50:
        print("Successfully Captured")
        break

camera.release()
cv2.destroyAllWindows()
