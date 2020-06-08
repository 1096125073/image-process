import cv2
import numpy as np
img=cv2.imread("mei.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
rows=img.shape[0]
cols=img.shape[1]
gamma_image=np.power(gray,0.5).astype(np.int8)
cv2.imshow("gamma_image",gamma_image)
cv2.waitKey(0)
cv2.destroyAllWindows()