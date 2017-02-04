#Assume that the maximum resolution is 600 X 800


from PIL import Image

im = Image.open("./yueyuanzhiye-015.jpg")
print(im.size)


x = im.size[0]
y = im.size[1]


times = max((x/600), (y/800))
print(times)
if(times <= 1):
    pass
else:
    size = int(x/times), int(y/times)
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save("after_edit.png", "PNG")



