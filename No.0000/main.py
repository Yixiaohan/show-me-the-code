from PIL import Image, ImageDraw, ImageFont

img = Image.open('0.jpg')
draw = ImageDraw.Draw(img)
myfont = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', size=40)
fillcolor = "#ff0000"
width, height = img.size
draw.text((width-60, 0), '1', font=myfont, fill=fillcolor)
img.save('result.jpg','jpeg')

