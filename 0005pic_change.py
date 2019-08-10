from PIL import Image
import os


def size_change(filepath):
    for each in os.listdir(filepath):
        with Image.open(filepath+'\\'+each) as image:
            ResizedImage = image.resize((1280, 2272), Image.ANTIALIAS)
            ResizedImage.show()

cwd=os.getcwd()+'\\pic'
size_change(cwd)