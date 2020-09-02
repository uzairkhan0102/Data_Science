
#resize multiple images in a folder

from PIL import Image
import os, sys
import glob

root_dir = "D:\Study\Uzair Khan\resize" #path to images folder


for filename in glob.iglob(root_dir + '**/*.jpg'):
    print(filename)
    im = Image.open(filename, 'r')
    imResize = im.resize((270,125), Image.ANTIALIAS) #new size of images
    imResize.save(filename , 'JPEG', quality=90) #format and quality

