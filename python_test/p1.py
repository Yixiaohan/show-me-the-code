from PIL import Image,ImageDraw,ImageFont

img = Image.open('qq1.jpg')


pencil = ImageDraw.Draw(img)

#画笔颜色设置成绿色
pencil.ink = 255 + 0*256 + 0*256*256

h,w = img.size

print h,w

#font=ImageFont.load_default() 


#font = ImageFont.truetype(l=none, 100)

font = ImageFont.truetype('C:\Users\pc\study\Debugged.ttf', 100)

pencil.text((1800,1000),'30',font = font)

img.save('qq1.png')







