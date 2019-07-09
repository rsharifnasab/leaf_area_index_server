
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

from skimage import feature


# Generate noisy image of a square
im = np.zeros((128, 128))
im[32:-32, 32:-32] = 1

im = ndi.rotate(im, 15, mode='constant')
im = ndi.gaussian_filter(im, 4)
im += 0.2 * np.random.random(im.shape)


im 
# Compute the Canny filter for two values of sigma
#feature.canny : Edge filter an image using the Canny algorithm.
#https://en.wikipedia.org/wiki/Canny_edge_detector
s1=1.5
s2=10
edges1 = feature.canny(im, sigma=s1)
edges2 = feature.canny(im, sigma=s2)

# display results
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),sharex=True, sharey=True)

#plt.show()

ax1.imshow(im, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('noisy image', fontsize=20)


ax2.imshow(edges1, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Canny filter, s='+str(s1), fontsize=20)


ax3.imshow(edges2, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('Canny filter, s='+str(s2), fontsize=20)


fig.tight_layout()


plt.show()
