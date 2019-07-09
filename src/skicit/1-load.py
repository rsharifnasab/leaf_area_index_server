import os
import matplotlib.pyplot as plt
import matplotlib
from skimage import io

matplotlib.rcParams['font.size'] = 18

sample_file = 'sample.JPG'
image = io.imread(sample_file)

plt.figure()
plt.title(sample_file)

plt.imshow(image)

plt.show()
