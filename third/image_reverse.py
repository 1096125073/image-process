import cv2
import copy
img=cv2.imread("mei.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
rows=img.shape[0]
cols=img.shape[1]
reversed_image=gray.copy()
for i in range(rows):
    for j in range(cols):
        reversed_image[i][j]=255-gray[i][j]
cv2.imshow("reversed_image",reversed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()