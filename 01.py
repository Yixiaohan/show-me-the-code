# -*- coding: UTF-8 -*-
from PIL import Image
from PIL import ImageDraw,ImageFont




im=Image.open("./qq.png")
name="4"
print(im.format,im.size,im.mode)
ps=ImageDraw.Draw(im)
box=im.size
ps.ink= 255 + 0 * 256 + 0 * 256 * 256
ps.text((im.size[0]-35,5),name,font=ImageFont.truetype("C:\Windows\Fonts\simfang.ttf",50))

im.show()
im.save("./qq1.png")

