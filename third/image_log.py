import cv2
import numpy as np
img=cv2.imread("mei.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
rows=img.shape[0]
cols=img.shape[1]
log_image=gray.copy()
for i in range(rows):
    for j in range(cols):
        log_image[i][j]=10*np.log(1+gray[i][j])
cv2.imshow("log_image",log_image)
cv2.waitKey(0)
cv2.destroyAllWindows()