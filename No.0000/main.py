from PIL import Image, ImageDraw, ImageFont

def editPhoto(filename, number):
    img = Image.open(filename)
    print(number)
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-60, 0), number, font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')


editPhoto('0.jpg', '4')





