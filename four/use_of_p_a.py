import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread("fire.jpg",0)
plt.subplot(141)
plt.imshow(img,cmap="gray")
plt.title('image_raw')

f=np.fft.fft2(img)
fshift=np.fft.fftshift(f)

shift_img=np.fft.ifftshift(fshift)

only_a_img=np.fft.ifft2(np.abs(shift_img))
plt.subplot(142)
plt.imshow(abs(only_a_img),cmap="gray")
plt.title('only_a_img')

only_p_img=np.fft.ifft2(np.angle(shift_img))
plt.subplot(143)
plt.imshow(abs(only_p_img),cmap="gray")
plt.title('only_p_img')

p=np.abs(shift_img)
angle=np.angle(shift_img)
real=p*np.cos(angle)
imag=p*np.sin(angle)

s=np.zeros(shift_img.shape,dtype=complex)
s.real=real
s.imag=imag

image_back=np.fft.ifft2(s)
plt.subplot(144)
plt.imshow(np.abs(image_back),cmap="gray")
plt.title("image_back")

plt.show()
