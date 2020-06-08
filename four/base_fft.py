import cv2
import matplotlib.pyplot as plt
from four.utils import *


img=cv2.imread("block.jpg",0)
plt.subplot(131)
plt.imshow(img,cmap="gray")
plt.title("raw_image")

f=np.fft.fft2(img)
abs_f=np.abs(f)
log_abs_f=np.log(abs_f+1.0)
plt.subplot(132)
plt.imshow(conver2img(log_abs_f),cmap="gray")
plt.title("f")

fshift=np.fft.fftshift(f)
abs_fshift=np.abs(fshift)
log_abs_shift=np.log(abs_fshift+1.0)
plt.subplot(133)
plt.imshow(conver2img(log_abs_shift),cmap="gray")
plt.title("fshift")
plt.show()
