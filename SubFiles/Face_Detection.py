# Start of Program

# Import OpenCV library 
import cv2

face_cascade = cv2.CascadeClassifier('TestFiles/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 15)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow('Image', img)

    if cv2.waitKey(40) == 27:
        break

cap.destroyAllWindows()
cap.release()
