"""
Basic image operation.
"""

import cv2

# Load image COLOR 1 GRAYSCALE 0 UNCHANGE -1
IMG = cv2.imread('./img-learn/gundam.png', 0)

# Display
cv2.imshow('Gundam In Action', IMG)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Write
cv2.imwrite('./img-learn/gundam-gray.jpg', IMG)
