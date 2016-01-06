from PIL import Image, ImageDraw
from PIL import ImageFont
import random

# 设置字体
font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 20)

#打开文件
im = Image.open("avatar.jpg")

#使用PIl的ImageDraw
draw = ImageDraw.Draw(im)
text = str(random.randint(1, 20))
point = (180, 10)
draw.text(point, text, font=font, fill="red")

#保存
im.save("avatar2.jpg")
