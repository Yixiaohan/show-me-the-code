from PIL import Image
import os
path='.//photos//'
name_list=os.listdir(path)
for name in name_list:
    print(path+name)
print(name_list)
print(os.getcwd())