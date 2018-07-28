"""
Basic video streaming operation.
"""

import cv2

# Capture video from camera
CAP = cv2.VideoCapture(0)

while True:
    # Capture frame by frame
    RET, FRAME = CAP.read()

    # Frame operation
    GRAY = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)

    # Display
    cv2.imshow('From Frame', GRAY)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture
CAP.release()
cv2.destroyAllWindows()
