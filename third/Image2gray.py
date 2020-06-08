import cv2

img=cv2.imread('mei.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("image",img)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
