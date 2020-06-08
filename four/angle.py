import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from four.utils import conver2img

img=cv.imread('block.jpg',0)
plt.subplot(131)
plt.imshow(img,cmap="gray")
plt.title("image_raw")

f=np.fft.fft2(img)
fshift=np.fft.fftshift(f)

angle_f=np.angle(f)
angle_fshift=np.angle(fshift)

img_angle_f=conver2img(angle_f)
img_angle_fshift=conver2img(angle_fshift)

plt.subplot(132)
plt.imshow(img_angle_f,cmap="gray")
plt.title("img_angle_f")
plt.subplot(133)
plt.imshow(img_angle_fshift,cmap="gray")
plt.title("img_angle_fshift")
plt.show()