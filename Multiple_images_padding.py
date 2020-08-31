
#multiple images padding which are present in a folder

from PIL import Image
import re
import os
path = r'D:\Study\Uzair Khan\new_images' #path to folder

for file_name in os.listdir(path):
    try:
        old_im = Image.open(os.path.join(path,file_name))
        old_size = old_im.size

        new_size = (500, 500) #new image size after padding
        new_im = Image.new("RGB", new_size)   #padding images with black colour!
        new_im.paste(old_im, ((new_size[0]-old_size[0])/2, (new_size[1]-old_size[1])/2))

        new_im.save(os.path.join(path,file_name))

    except Exception as e:
        print "/error",e
