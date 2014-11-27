from PIL import Image, ImageDraw, ImageFont

class Image_unread_message:
	def open(self,path):
		self.im=Image.open(path)
		return True
	def __init__(self):
		self.fnt=None
		self.im=None

	def setFont(self,font_path,size):
		self.fnt=ImageFont.truetype(font_path,size)
		return True
	def draw_text(self,position,str,colour,fnt):
		draw=ImageDraw.Draw(self.im)
		draw.text(position,str,fill=colour,font=fnt)
		self.im.show()
		self.im.save(str+'num'+'.jpg')
		return True


test=Image_unread_message()
test.open('test.jpg')
test.setFont('ahronbd.ttf',80)
test.draw_text((160,-20),'4',(255,0,0),test.fnt)



