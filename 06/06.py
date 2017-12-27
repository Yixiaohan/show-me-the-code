from PIL import Image
import os



def Re_size(path):
    iPhone5_WIDTH = 1136
    iPhone5_HEIGHT = 640
    new_path=r"\\new\\"
    name_list=os.listdir(path)
    for name in name_list:
        photo=Image.open(path+name)
        w, h = photo.size
        print(name)
        if w>iPhone5_WIDTH:
            w=iPhone5_WIDTH
            h=h*iPhone5_WIDTH//w
        if h>iPhone5_HEIGHT:
            h=iPhone5_HEIGHT
            w=w*iPhone5_HEIGHT//h
        resize_photo=photo.resize((w,h),Image.ANTIALIAS)# ANTIALIAS滤镜缩放
        resize_photo.save(os.getcwd()+new_path+name)
        print(name)




if __name__ == '__main__':
    Re_size(r".//photos//")
