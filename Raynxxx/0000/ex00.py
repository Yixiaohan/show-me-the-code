__author__ = 'rayn'

#problem 0000
#Add a unread number on the face icon

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class UnreadTagFace:
    def __init__(self):
        self.img = None
        self.num = None
    def open(self, image_path):
        self.img = Image.open(image_path)
        return True
    def draw(self, tag_num = 1):
        tag_size = max(self.img.size[0], self.img.size[1]) / 5
        tag_str = str(tag_num) if tag_num < 100 else '99+'
        font = ImageFont.truetype("Arial.ttf", tag_size)
        px = self.img.size[0] - font.getsize(tag_str)[0]
        draw_pen = ImageDraw.Draw(self.img)
        draw_pen.text((px, 0), tag_str, (255, 0, 0), font)
        self.img.save('face' + tag_str + '.jpg')
        return True


solver = UnreadTagFace()
solver.open('face.jpg')
solver.draw(4)








