#import  os
#from PIL import Image

#dir = "C:\Users\pc\study\photo"
#list = os.listdir(dir)
#
#for file in list :
	#if os.path.isfile(file):
		#image = Image.open(file)
		#image.resize((1136,640),Image.BILINEAR)
		#image.save(file,'jpg')
		


import os

from PIL import Image

size = 1136,640
path = "C:\Users\pc\study\photo"

def transfer(image):
	 file, ext = os.path.splitext(image)
	 im = Image.open(image)
	 im.thumbnail(size)
	 im.save(file + ".thumbnail", "JPEG")
	 
def get_image_list(path):
	files = os.listdir(path) 
	return files
	
if __name__ == '__main__':
	files = get_image_list(path)
	for i in files:
		a_path = path + os.sep + i
		transfer(a_path)

	 
