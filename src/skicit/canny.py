
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import feature, io
from skimage.color import rgb2gray



sample_file = 'sample.JPG'
im = io.imread(sample_file)
im = im[:,:,:]
im = rgb2gray(im)

#red_edges = feature.canny(im[:, :, 0])
s1 = 1.5
s2 = 0.9
edges1 = feature.canny(im, sigma=s1)
edges2 = feature.canny(im, sigma=s2)

# display results
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(80, 30),sharex=True, sharey=True)

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
