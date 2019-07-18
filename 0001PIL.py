from PIL import Image, ImageDraw, ImageFont

def imgWriter(filepath,number):
    img=Image.open(filepath)
    fnt_img = ImageDraw.Draw(img)
    imgw,imgh = img.size
    fnt=ImageFont.truetype('C:/Windows/Fonts/AdobeHeitiStd-Regular.otf',size=100)
    fnt_img.ellipse([(imgw-150, 20), (imgw-20, 150)], fill=(255, 0, 0))
    fnt_img.text((imgw - 110, 40), str(number), font=fnt, fill=(255, 255, 255, 128))
    #out = Image.alpha_composite(img,d)
    img.show()


imgWriter('C:/Users/景程/Desktop/2.jpg',7)