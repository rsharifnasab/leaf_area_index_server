from PIL import Image

def load(address):
    MAX_DIMENS = 512 , 512
    image = Image.open(address)
    image.thumbnail(MAX_DIMENS, Image.ANTIALIAS)
    return image

def distinc_colors(image):

    COLOR_LIMIT = 1.1

    im = image
    R, G, B = im.convert('RGB').split()
    r = R.load()
    g = G.load()
    b = B.load()
    w, h = im.size

    for i in range(w):
        for j in range(h):
            aver = ( r[i,j] + g[i, j] + b[i, j] ) / 3

            if r[i,j] < aver * COLOR_LIMIT or r[i,j] < g[i,j] + b[i,j] : r[i,j] = 0 # red is too low
            if g[i,j] < aver * COLOR_LIMIT or g[i,j] < r[i,j] + b[i,j] : g[i,j] = 0 # green is too low
            b[i,j] = 0 # delete blue

    #im = Image.merge('RGB', (R, G, B))
    #im.show()
    return r,g

def pixel_counter(red,green,im_size):
    w,h =  im_size
    red_pixels = 0
    green_pixels = 0
    for i in range(w):
        for j in range(h):
            if red[i,j]  > 0 : red_pixels +=1
            if green[i,j]  > 0 : green_pixels +=1
    return red_pixels,green_pixels

def leaf_area_calculate(address):
    image = load(address)
    red , green = distinc_colors(image)
    red_pix , green_pix = pixel_counter(red,green,image.size)
    ans = green_pix / red_pix
    return ans
