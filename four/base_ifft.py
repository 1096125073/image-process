import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread("fire.jpg",0)
plt.subplot(131)
plt.imshow(img,cmap="gray")
plt.title('image_raw')

f=np.fft.fft2(img)
fshift=np.fft.fftshift(f)

shift_img=np.fft.ifftshift(fshift)
i_img=np.fft.ifft2(shift_img)

plt.subplot(132)
plt.imshow(abs(i_img),cmap="gray")
plt.title('inverse image')
print(img-i_img)
plt.show()
