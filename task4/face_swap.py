# 🔅 Task 4.2
# 📌 Take 2 image crop some part of both image and swap it.

import cv2
import numpy

photo_1=cv2.imread('smile.png')
photo_2=cv2.imread('ang.png')

photo_1_=photo_1[180:260,80:240]
cv2.imshow("myphoto",photo_1_)
cv2.waitKey()
cv2.destroyAllWindows()

photo_2_ = photo_2[180:260,80:240]
cv2.imshow("myphoto",photo_2_)
cv2.waitKey()
cv2.destroyAllWindows()

photo_2[180:260,80:240] = photo_1_
cv2.imshow("myphoto",photo_2)
cv2.waitKey()
cv2.destroyAllWindows()

temp_photo = photo_2=cv2.imread('ang.png')
photo_2_ = temp_photo[180:260,80:240]

photo_1[180:260,80:240]  = photo_2_
cv2.imshow("myphoto",photo_1)
cv2.waitKey()
cv2.destroyAllWindows()