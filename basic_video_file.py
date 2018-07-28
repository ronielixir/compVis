"""
Basic video from file.
"""

import cv2

CAP = cv2.VideoCapture('./vid-learn/scitunnel.mp4')

while CAP.isOpened():
    RET, FRAME = CAP.read()

    GRAY = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Frame from file', GRAY)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

CAP.release()
cv2.destroyAllWindows()
