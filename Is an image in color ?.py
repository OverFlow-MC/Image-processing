import os
import numpy as np
import matplotlib.pyplot as plt
def test_image(x):
    os.chdir("D:/Informatique/TP11")
    a=plt.imread('PaysageNB.jpg')
    b,c,d=np.shape(a)
    for i in range(b):
        for j in range(c):
            if not(a[i,j,0]==a[i,j,1]==a[i,j,2]):
                return "l'image est en couleur"
    return "l'image est en noir et blanc"