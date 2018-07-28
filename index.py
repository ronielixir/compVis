import numpy as numpy
import cv2

frame_empty = cv2.imread("frame-empty.jpeg")

# cv2.imshow('Image', frame_empty)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture('peopleCount.mp4')

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
