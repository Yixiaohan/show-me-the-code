#-*-coding: utf-8-*-
class change_DPI:

    def __init__(self):
        self.path = None

    def setPath(self, path):
        self.path = path

    def change_DPI(self):
        import os
        files = os.listdir(self.path)
        is_exist = False
        for f in files:
            if f.endswith(('.jpg', '.png')):
                is_exist = True
                path_name = os.path.join(self.path, f)
                # 更改f对应文件的分辨率
                from PIL import Image
                im = Image.open(path_name)
                x_iphone5 = 1136
                y_iphone5 = 640
                (x, y) = im.size
                print('origin img size:')
                print(im.size)
                if x > x_iphone5 or y > y_iphone5:
                    if x > x_iphone5:
                        x_resize = x_iphone5
                        y_resize = int(y * (x_resize / x))
                        f_resize = im.resize((x_resize, y_resize))
                        f_resize.save(f)
                        continue
                    if y > x_iphone:
                        y_resize = y_iphone5
                        x_resize = x * (y_resize / y)
                        f_resize = im.resize(
                            (x_resize, y_resize), Image.ANTIALIAS)
                        f_resize.save(f)
                        continue

        if is_exist == False:
            print('no photo')


if __name__ == '__main__':
    test = change_DPI()
    test.setPath('.')
    test.change_DPI()
