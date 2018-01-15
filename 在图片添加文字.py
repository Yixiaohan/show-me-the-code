from PIL import Image, ImageDraw, ImageFont

im1=Image.open("e:/1.jpg")
#设置字体
font_size=ImageFont.truetype('arial.ttf',size=50)

#初始化一个类
draw=ImageDraw.Draw(im1)

#第一个参数是位置，(0,0)从左上开始,第二个参数是写入的字符，第三个是设置颜色，font是设置的字体
draw.text((500, 10), "4",fill=(255,0,0),font=font_size)


im1.show()