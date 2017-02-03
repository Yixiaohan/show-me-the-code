from PIL import Image, ImageDraw, ImageFont
from random import randint


def add_num(img):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    color = "#123456"
    width, height = img.size
    draw.text((width-40,0), str(randint(0,99)), font=font, fill=color)
    img.save("result.jpg",'jpeg')

if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image)