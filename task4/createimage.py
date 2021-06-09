# 🔅 Task 4.1
# 📌 Create image by yourself Using Python Code
import numpy as np
import cv2
photo = np.zeros((600,600,3))
photo.shape
#head
cv2.circle(photo,center=(250,75),radius=75,color=(78,25,0),thickness=-1)
photo[150:170,240:260]=[56,67,45]#neck
photo[170:300,150:350]=[255,0,37]#body

photo[300:450,150:200]=[12,255,0]#right leg
photo[300:450,300:350]=[12,255,0]#left leg
photo[170:180,350:450]=[45,67,255]#right hand
photo[170:180,50:450]=[45,67,255]#left hand
cv2.imshow('img',photo)
cv2.waitKey()
cv2.destroyAllWindows()