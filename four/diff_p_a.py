import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from four.utils import *

img1=cv.imread('fire.jpg',0)
img2=cv.imread("mei.jpg",0)
img2=cv.resize(img2,(656,437))

display(141,img1,'img1')
display(142,img2,'img2')

f1=np.fft.fft2(img1)
f2=np.fft.fft2(img2)

fs1=np.fft.fftshift(f1)
fs2=np.fft.fftshift(f2)

a1=np.abs(fs1)
angle1=np.angle(fs1)
a2=np.abs(fs2)
angle2=np.angle(fs2)

a1_angle2=np.zeros(img1.shape,dtype=complex)
a1_angle2.real=a1*np.cos(angle2)
a1_angle2.imag=a1*np.sin(angle2)

a2_angle1=np.zeros(img1.shape,dtype=complex)
a2_angle1.real=a2*np.cos(angle1)
a2_angle1.imag=a2*np.sin(angle1)

i_fs1=np.fft.ifftshift(a1_angle2)
i_fs2=np.fft.ifftshift(a2_angle1)

i_f1=np.fft.ifft2(i_fs1)
i_f2=np.fft.ifft2(i_fs2)

display(143,np.abs(i_f1),"i_img1")
display(144,np.abs(i_f2),"i_img2")

plt.show()
