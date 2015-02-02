import sys
import Image
import ImageFont, ImageDraw, ImageOps

class Image_num_taged:
    def open_Img(self, path):
        self.img = Image.open(path)
        return True

    def __init__(self):
        self.fnt = None
        self.img = None

    def set_Font(self, font_Path, font_Size):
        self.fnt = ImageFont.truetype(font_Path, font_Size,
                                      encoding = 'symb')
        return True

    def posi_Set(self):
        (self.width, self.height) = self.img.size
        self.num_posi = self.width - 1.5 * self.font_size
        return True

    def num_Taged(self, str):
        Image_num_taged.posi_Set(self)
        img_Taged = ImageDraw.Draw(self.img)
        img_Taged.text(self.num_posi, str, (255, 0, 0), self.fnt)
        del img_Taged
        self.img.save(self.path)


im = Image_num_taged()
im.open_Img('squirrel.jpg')
im.set_Font('Arabic.ttf', 20)
im.num_Taged('4')


# im = Image.open("squirrel.jpg")
# (width, height) = im.size
# posi = width - 10
#
# # fontsize = 20
# # fontpath = 'C:\Windows\Fonts\Arial\Adobe Arabic.ttf'
# # font = ImageFont.truetype(fontpath, fontsize, encoding = 'symb')
# font = ImageFont.load_default()
#
#
# im1 = ImageDraw.Draw(im)
# im1.text(( posi, 0), "4", (255, 0, 0), font)
#
# del im1
#
# im.save("squirrel2.png")
