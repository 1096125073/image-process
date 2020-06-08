import numpy as np
import matplotlib.pyplot as plt
from four.utils import gauss_mask
import cv2 as cv

mask=gauss_mask(500,500,10)
print(mask[250,250])
cv.imshow("mask",mask)
cv.waitKey(0)
cv.destroyAllWindows()
