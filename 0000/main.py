#coding = utf-8
from PIL import Image, ImageDraw, ImageFont


def draw(pic, number, color, font):
	img = Image.open(pic)
	x, y = img.size
	print x, y
	fontSize = y / 4
	print fontSize
	print len(str(number))
	x -= fontSize*len(str(number))/1.5 # 1.5 seems suitable....
	print x, y

	drawImg = ImageDraw.Draw(img)
	drawFont = ImageFont.truetype(font, fontSize)
	drawImg.text((x, 0), str(number), color, font = drawFont)
	del drawImg
	img.save("./result.png")
	img.show()

if __name__ == '__main__':
	font = "/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf"
	pic = "./a.png"
	color = "red"
	number = "99+"
	draw(pic, number, color, font)
	