import cv2 as cv
import numpy as np

img=cv.imread("jiaoyan.png",0)
cv.imshow("image_noise",img)

blur_img=cv.blur(img,(3,3))
cv.imshow("blur_img",blur_img)

median_img=cv.medianBlur(img,3)
cv.imshow("media_img",median_img)

lap_img=cv.Laplacian(median_img,-1,ksize=3)
cv.imshow("lap_img",lap_img)



img1=median_img+cv.medianBlur(lap_img,5)
cv.imshow("img1",img1)

cv.waitKey(0)
cv.destroyAllWindows()