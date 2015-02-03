from PIL import Image
from PIL import ImageFont, ImageDraw


class Image_num_taged:
    def open_Img(self, path):
        self.img = Image.open(path)
        return True

    def __init__(self):
        self.fnt = None
        self.img = None

    def set_Font(self, font_Path, font_Size):
        self.fnt = ImageFont.truetype(font_Path, font_Size,
                                      encoding = 'unic')
        (self.width, self.height) = self.img.size
        self.num_posi = (self.width - font_Size, 0.5*font_Size)
        return True

    def num_Taged(self, str):
        img_Taged = ImageDraw.Draw(self.img)
        img_Taged.text(self.num_posi, str, (255, 0, 0), self.fnt)
        del img_Taged
        self.img.save('image_taged.png')


im = Image_num_taged()
im.open_Img('squirrel.jpg')
im.set_Font('Arial.ttf', 40)
im.num_Taged('4')