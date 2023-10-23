# Start of Subfile for Webcam or other camera

# Import OpenCV library
import cv2

# Pass the camera port to OpenCV
cap = cv2.VideoCapture(0)

# Create frames (two for redundancy)
ret, frame1 = cap.read()
ret, frame2 = cap.read()

# Loop the Algorithm
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Define Contours
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 90000:
            continue

        # Draw contours
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, 'Status: {}'.format('Movement'), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Alternatively, use the below mentioned function
        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    # Display the Output
    cv2.imshow('Video', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()


    # Add wait-time
    if cv2.waitKey(10) == 27:
        break

# Finish
cv2.destroyAllWindows()
cap.release()

# End of Program
