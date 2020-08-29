	
#crop multiple images present in a folder


from PIL import Image
import os.path, sys


path = "D:\Study\Uzair Khan\crop" #path to files
dirs = os.listdir(path)

def crop():
    for item in dirs:
        fullpath = os.path.join(path,item)         #corrected
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop((40, 160, 580, 410)) #crop image dimensions
            imCrop.save(f + '.jpg', "BMP", quality=50) #format and quality
            

crop()

