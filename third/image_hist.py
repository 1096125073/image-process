import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("fire.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
rows=img.shape[0]
cols=img.shape[1]
plt.hist(img.ravel(),256)
plt.show()
colors=['r','g','b']
for i in range(len(colors)):
    hist=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,colors[i])
plt.show()


r,g,b=cv2.split(img)
hist_r=cv2.equalizeHist(r)
hist_g=cv2.equalizeHist(g)
hist_b=cv2.equalizeHist(b)
img_hist=cv2.merge([hist_r,hist_g,hist_b])

clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
clahe_img=clahe.apply(gray)
cv2.imshow("image_raw",gray)
cv2.imshow("clahe_img",clahe_img)
cv2.imshow("hist_image",img_hist)
cv2.waitKey(0)
cv2.destroyAllWindows()