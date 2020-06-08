import cv2 as cv
import numpy as np

img=cv.imread("jiaoyan.png",0)
cv.imshow("image_noise",img)

blur_img=cv.blur(img,(3,3))
cv.imshow("blur_img",blur_img)

median_img=cv.medianBlur(img,3)
cv.imshow("median_img",median_img)

gauss_img=cv.GaussianBlur(img,(3,3),0)
cv.imshow("gauss_img",gauss_img)

kernel=np.ones([3,3],np.float)/9
self_img=cv.filter2D(img,-1,kernel)
cv.imshow("self_img",self_img)

lap_img=cv.Laplacian(img,-1,ksize=3)
cv.imshow("lap_img",lap_img)

img1=img+lap_img*0.1
cv.imshow("img1",img1)

cv.waitKey(0)
cv.destroyAllWindows()