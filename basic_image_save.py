import cv2

IMG = cv2.imread('./img-learn/gundam.png', 0)

cv2.imshow('Gundam In Action', IMG)
k = cv2.waitKey(0) & 0xFF  # 64 bit

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait s key
    cv2.imwrite('./img-learn/gundam-grey.jpg', IMG)
    cv2.destroyAllWindows()
