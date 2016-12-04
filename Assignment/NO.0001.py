#!/usr/bin/env python
# -*- coding:utf-8 -*-


print 'NO.001 头像加数字'

import Image, ImageDraw, ImageFont, random

#导入图片
im = Image.open('portrait2.jpeg')

w, h = im.size

print 'width = %d \nheight = %d' % (w, h)
print '------------------>'

#创建draw对象
draw = ImageDraw.Draw(im)

#创建font对象
font = ImageFont.truetype(
'/usr/share/fonts/truetype/freefont/FreeSansOblique.ttf', size = 36)

#字体颜色 、内容
def col():
	return (255, 0, 0)

text = str(random.randint(0, 9))

#写字
draw.text((165, 5), text , font = font, fill = col())

#save
im.save('tagportrait.jpg', 'jpeg')
