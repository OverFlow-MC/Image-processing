import os
import numpy as np
import matplotlib.pyplot as plt
def couleurs(x):
    os.chdir("D:/...")
    a=plt.imread('YourImage.jpg')
    b,c,d=np.shape(a)
    x=np.zeros([b,c,3],dtype="uint8")
    y=np.zeros([b,c,3],dtype="uint8")
    z=np.zeros([b,c,3],dtype="uint8")
    x[:,:,0]=a[:,:,0]
    y[:,:,1]=a[:,:,1]
    z[:,:,2]=a[:,:,2]
    plt.imshow(x)
    plt.figure()
    plt.show()
    plt.imshow(y)
    plt.figure()
    plt.show()
    plt.imshow(z)
    plt.figure()



