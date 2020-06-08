import numpy as np
import matplotlib.pyplot as plt

def conver2img(img):
    img_min=np.min(img)
    print(img_min)
    img_max=np.max(img)
    print(img_max)
    normal_img=(img-img_min)/(img_max-img_min)
    out_img=(255*normal_img).astype(np.int)
    print(out_img)
    return out_img


def display(num,img,title):
    plt.subplot(num)
    plt.imshow(img,cmap='gray')
    plt.title(title)


def getCenter(img,r):
    center_x,center_y=img.shape[0]/2,img.shape[1]/2
    coords_x=[]
    coords_y=[]
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if np.sqrt((center_x-i)**2+(center_y-j)**2)<r:
                coords_x.append(i)
                coords_y.append(j)
    return coords_x,coords_y


def abs_log(img):
    abs_img=np.abs(img)
    abs_log_img=np.log(abs_img+1)
    return abs_log_img


def gauss_mask(rows,clos,theta):
    mask=np.zeros((rows,clos),dtype=np.float)
    center_row,center_clo=rows/2,clos/2
    for i in range(rows):
        for j in range(clos):
            d=(i-center_row)**2+(j-center_clo)**2
            mask[i,j]=np.exp(-d/(2*theta**2))
    return mask