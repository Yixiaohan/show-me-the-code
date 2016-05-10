from PIL import Image, ImageDraw, ImageFont

num = str(5)
img = Image.open('shenle.png')
h, l = img.size

font = ImageFont.truetype('/usr/share/fonts/truetype/droid/DroidSans.ttf', 30)
draw = ImageDraw(img)

draw.text((h*0.8, l*0.2), num, font=font, fill(255, 33, 33))

img.save('shenle5.png', 'png')

