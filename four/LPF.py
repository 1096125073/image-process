import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from four.utils import *

img1=cv.imread('jiaoyan.png',0)
display(141,img1,'img1')

f1=np.fft.fft2(img1)
fs1=np.fft.fftshift(f1)
angle1=np.angle(fs1)

mask=np.zeros(img1.shape,np.int8)
coord_x,coord_y=getCenter(img1,50)
mask[coord_x,coord_y]=1

fs1=np.abs(fs1*mask)
log_img=abs_log(fs1)
display(142,conver2img(log_img),'LPF')

i_fs1=np.zeros(img1.shape,dtype=complex)
i_fs1.real=fs1*np.cos(angle1)
i_fs1.imag=fs1*np.sin(angle1)

i_f=np.fft.ifftshift(i_fs1)
i_img=np.fft.ifft2(i_f)
display(143,np.abs(i_img),"i_img")
cv.imwrite('HPF.jpg',np.abs(i_img))
plt.show()
