"""
Draw function basic.
"""

import numpy as np
import cv2 as cv

# Create a black image using np array operation
IMG = np.zeros((512, 512, 3), np.uint8)

# [base, start px, finish px, bgr color, thickness]
cv.line(IMG, (0, 0), (511, 511), (255, 0, 0), 5)
cv.rectangle(IMG, (384, 0), (510, 128), (0, 255, 0), 3)

# [coord, r, bgr color, thickness]
cv.circle(IMG, (447, 163), 63, (0, 0, 255), -1)

# https://docs.opencv.org/3.4.0/d6/d6e/group__imgproc__draw.html#ga28b2267d35786f5f890ca167236cbc69
cv.ellipse(IMG, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# Use numpy array as locator
PTS = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
PTS = PTS.reshape((-1, 1, 2))
cv.polylines(IMG, [PTS], True, (0, 255, 255))

FONT = cv.FONT_HERSHEY_SIMPLEX
cv.putText(IMG, 'Phire!!', (10, 500), FONT, 4, (255, 255, 255), 2, cv.LINE_AA)

# Display
cv.imshow('Image black', IMG)
cv.waitKey(0)
cv.destroyAllWindows()
