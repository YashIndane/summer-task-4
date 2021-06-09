# 🔅 Task 4.3
# 📌 Take 2 image and combine it to form single image. For example collage
import cv2
import numpy

photo_1=cv2.imread('smile.png')
photo_2=cv2.imread('ang.png')

final = numpy.hstack((photo_2 , photo_1))
cv2.imshow("myphoto",final)
cv2.waitKey()
cv2.destroyAllWindows()