"""
Basic video saving from stream.
"""

import cv2

CAP = cv2.VideoCapture(0)

# Define codec and video writer object
FOURCC = cv2.VideoWriter_fourcc(*'DIVX')
OUT = cv2.VideoWriter('output.avi', FOURCC, 20.0, (1280, 720))

while CAP.isOpened():
    RET, FRAME = CAP.read()
    if RET is True:
        # FRAME = cv2.flip(FRAME, 0)

        # write frames
        OUT.write(FRAME)
        cv2.imshow('Frame from camera', FRAME)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything
CAP.release()
OUT.release()
cv2.destroyAllWindows()
