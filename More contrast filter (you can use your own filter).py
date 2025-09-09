import os
import numpy as np
import matplotlib.pyplot as plt
os.chdir("D:/Informatique/TP11")
T=plt.imread("Couchersoleil.jpg")
n,m,p=np.shape(T)
T2=np.zeros([n,m,p],dtype='uint8')
F=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
niv=0
for i in range(1,n-1):
    for j in range(1,m-1):
        for k in range(p):
            niv=int(np.sum(F*T[i-1:i+2,j-1:j+2,k]))
            if niv>255:
                niv=255
            elif niv<0:
                niv=0
            T2[i,j,k]=niv
plt.imshow(T2)
plt.show()