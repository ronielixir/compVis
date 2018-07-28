"""
Test cam properties.
"""
import cv2 as cv

CAP = cv.VideoCapture(0)

print('Width: ', CAP.get(cv.CAP_PROP_FRAME_WIDTH))
print('Height: ', CAP.get(cv.CAP_PROP_FRAME_HEIGHT))
