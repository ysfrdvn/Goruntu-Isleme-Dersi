def get_distance(v,w=[1/3,1/3,1/3]): #default deger !!!!
    a,b,c = v[0],v[1],v[2]
    w1,w2,w3 = w[0],w[1],w[2]
    d = ((a**2)*w1+
    (b**2)*w2+
    (c**2)*w3)**.5
    return d#((a*w1)**2+(b*w2)**2+(c*w3)**2)**(0.5)
my_RGB=[1,2,3]
gray_level = get_distance(my_RGB)
print(gray_level)

my_RGB=[10,20,3]
gray_level = get_distance(my_RGB,[.6,.3,.1])
print(gray_level)


def convert_rgb_to_gray_level(im_1):#renkliyi grilevela cevirme
    m=im_1.shape[0]
    n=im_1.shape[1]
    im_2 = np.zeros((m,n)) # boyutu belirttik yeni resmin
    for i in range(m):
        for j in range(n):
            im_2[i,j] = get_distance(im_1[i,j,:])
    return im_2

def convert_gray_level_to_BW(im_gray_level): #grileveli siyah beyaz yapma
    m=im_gray_level.shape[0]
    n=im_gray_level.shape[1]
    im_bw = np.zeros((m,n)) # boyutu belirttik yeni resmin
    for i in range(m):
        for j in range(n):
            if im_gray_level[i,j]>120:
                im_bw[i,j] =1
            else:
                im_bw[i,j]=0
    return im_bw

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('image_1.jpg')

import os
cwd = os.getcwd()
cwd

%matplotlib inline
plt.imshow(img)

img2 = convert_rgb_to_gray_level(img) #resmi degistirdik yeni resme atadık
plt.imshow(img2,cmap='gray') #artık gri level oldu

img.shape,img2.shape #img 3 boyutlu img2 ise 2 boyutlu
img3 = convert_gray_level_to_BW(img2)

plt.imshow(img3,cmap='gray')

plt.subplot(1,3,1),plt.imshow(img)
plt.subplot(1,3,2),plt.imshow(img2,cmap='gray') #hepsinin 1 arada yazılan hali !!!
plt.subplot(1,3,3),plt.imshow(img3,cmap='gray')
