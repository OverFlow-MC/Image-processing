import os
import numpy as np
import matplotlib.pyplot as plt
def rotation(x):
    os.chdir("D:/Informatique/TP11")
    T=plt.imread("Couchersoleil.jpg")
    m,n,p=np.shape(T)
    T2=np.zeros([m,n,3],dtype='uint8')
    for i in range(n):
        T2[:,n-i-1,:]=T[i,:,:]
    plt.imshow(T2)
    plt.show()
