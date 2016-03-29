#Filename:10.py
# url:http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140767171357714f87a053a824ffd811d98a83b58ec13000

import PIL
import random
import Image, ImageFilter, ImageDraw, ImageFont

def rndChar():
	return chr(random.randint(65, 90))

def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 40
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('Arial.ttf', 36)
draw = ImageDraw.Draw(image)

for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndColor())

for t in range(4):
	draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
