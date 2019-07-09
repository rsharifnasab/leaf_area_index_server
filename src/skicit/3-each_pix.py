
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from scipy.stats import variation
from skimage import feature, io
from skimage.color import rgb2gray


def is_grey(im,x,y):
    GREY_LIMIT = 0.12
    rgb = im[x][y]
    aver = sum(rgb) / 3
    varians = ( rgb[0] - aver )**2 + ( rgb[1] - aver )**2 + ( rgb[2] - aver )**2
    cv = varians**0.5 / aver
    print("cv is " + str(cv))
    return cv < GREY_LIMIT



def is_green(im,x,y):
    GREEN_LIMIT = 0.8
    rgb = im[x][y]
    aver = sum(rgb) / 3
    return  rgb[1] > GREEN_LIMIT * aver


def is_red(im,x,y):
    RED_LIMIT = 0.8
    rgb = im[x][y]
    aver = sum(rgb) / 3
    print(rgb)
    return  rgb[2] > RED_LIMIT  * aver


def specify_all_pixel(im):

    COLOR_LIMIT = 0.8

    ans = np.zeros(im.shape[:])
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):

            to_add = 0
            #if is_grey(im, x, y): to_add  = 1
            ans[x][y][0] = to_add

            to_add = 0
            if is_green(im, x, y): to_add  = 1
            ans[x][y][1] = to_add

            to_add = 0
            if is_red(im, x, y): to_add  = 1
            ans[x][y][2] = to_add


    return ans

sample_file = 'sample.JPG'
im = io.imread(sample_file)
im = specify_all_pixel(im)
#im = im[:,:,0]
#im = rgb2gray(im)

#red_edges = feature.canny(im[:, :, 0])

# display results
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(80, 30),sharex=True, sharey=True)

ax1.imshow(im[:,:,0], cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('shadow', fontsize=20)


ax2.imshow(im[:,:,1], cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('green', fontsize=20)



ax3.imshow(im[:,:,2] , cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('red', fontsize=20)


fig.tight_layout()

plt.show()
