# coding=utf-8
import os
import glob
from PIL import Image
import os

def change_resolution(path, resolution):
    png_paths = glob.glob(path + r'/*.png')
    jpg_paths = glob.glob(path + r'/*.jpg')
    num = 0
    print(png_paths)
    new_path = path + '/changed'
    if not os.path.isdir(new_path):
        print("mkdir!")
        os.mkdir(new_path)
    for png in png_paths:
        num += 1
        file = Image.open(png)
        file.thumbnail(resolution)
        filename = png.strip(path+'/')
        file.save(new_path+'/changed_'+filename+'.png')
    for jpg in jpg_paths:
        num += 1
        file = Image.open(jpg)
        file.thumbnail(resolution)
        filename = jpg.strip(path+'/')
        file.save(new_path+'/changed_'+filename+'.jpg')


if __name__ == "__main__":
    relative_path = './SavedPictures'
    ip_resolution = (1136, 640)
    change_resolution(relative_path, ip_resolution)