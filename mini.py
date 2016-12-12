import sys
import astropy.io.fits as fits
import numpy as np

input = raw_input("Enter fit file: ")
image = fits.open(input)
#image[0].header['comment'] = "File modified by mini.py"
if image[0].data.any() > 65400:
    image[0].data = 0
for i in range(0, image[0].data.shape[0]):
    for j in range(0, image[0].data.shape[1]):
        if image[0].data[i,j] > 65400:
            image[0].data[i,j] = 0
print(np.mean(image[0].data))
newn = "new_" + input
image.writeto(newn)
# this will write new fit with changes made, the next line will save changes to the same file
# image.flush()
image.close()
