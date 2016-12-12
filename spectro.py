from math import *
import numpy as np
import astropy.io.fits as fits
import matplotlib.pyplot as plt
import os

H=fits.open('new_median_epscyg.fit')

hdat = H[0].data[407:476,0:1000]
h1d = np.sum(hdat, axis=0)
y = np.arange(len(h1d))
w = - 0.210*y + 574.1
"""
plt.figure()
plt.plot(y,h1d)
plt.show()
"""
div = []

x = np.arange(0, len(w))
z = np.polyfit(y, h1d, 3)
p = np.poly1d(z)
for i in range(len(h1d)):
    div.append(p(i))

new = h1d/div
"""
print new

plt.plot(y, h1d, x, p(x))
plt.show()
"""
D=fits.open('new_master_alphaOph.FIT')

ddat = D[0].data[407:476,0:1000]
h2d = np.sum(ddat, axis=0)
yd = np.arange(len(h2d))
"""
plt.figure()
plt.plot(yd,h2d)
plt.show()
"""
h2d = np.sum(ddat, axis=0)/new
h3d = np.sum(ddat, axis=0)
yd = np.arange(len(h2d))
wd = - 0.210*yd + 574.1


plt.figure()
plt.plot(wd,h2d)
#plt.plot(wd,h3d)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Intensity")
plt.show()
