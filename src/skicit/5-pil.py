

# 0 : b  ,  1 : g  ,  2 : r

sample_file = 'sample.JPG'
sample_file = 'leaf2.JPG'

from PIL import Image
import os

# Separate RGB arrays
im = Image.open(sample_file)
R, G, B = im.convert('RGB').split()
r = R.load()
g = G.load()
b = B.load()
w, h = im.size
COLOR_LIMIT = 1.1

# Convert non-black pixels to white
for i in range(w):
    for j in range(h):
        aver = ( r[i,j] + g[i, j] + b[i, j] ) / 3

        if r[i,j] < aver * COLOR_LIMIT or r[i,j] < g[i,j] + b[i,j] : r[i,j] = 0 # red is too low
        if g[i,j] < aver * COLOR_LIMIT or g[i,j] < r[i,j] + b[i,j] : g[i,j] = 0 # green is too low
        b[i,j] = 0 # delete blue

# Merge just the R channel as all channels
im = Image.merge('RGB', (R, G, B))
im.show()
