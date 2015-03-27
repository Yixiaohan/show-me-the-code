#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

if len(sys.argv) != 3:
	print "Usage: %s <image> <number>" %(os.path.basename(sys.argv[0]))
	sys.exit(0)	

if int(sys.argv[2]) > 99:
	sys.argv[2] = "99+"

im = Image.open(sys.argv[1])

font_size = im.size[0] if im.size[0] < im.size[1] else im.size[1]
font_size = font_size / 4
font_path = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
font = ImageFont.truetype(font_path, font_size)

draw = ImageDraw.Draw(im)
position = (im.size[0] - font.getsize(sys.argv[2])[0], 0)
draw.text(position, sys.argv[2], font=font, fill='#FF0000')

im.save("output.png")

