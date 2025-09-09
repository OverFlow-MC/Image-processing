import os
import numpy as np
import matplotlib.pyplot as plt
def test_image(x):
    os.chdir("D:/...")
    a=plt.imread('YourImage.jpg')
    b,c,d=np.shape(a)
    for i in range(b):
        for j in range(c):
            if not(a[i,j,0]==a[i,j,1]==a[i,j,2]):
                return "The image is in color"

    return "The image is in black and white"
