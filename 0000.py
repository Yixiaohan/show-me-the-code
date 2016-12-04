# Source:https://github.com/renzongxian/show-me-the-code
# Author:renzongxian
# Date:2014-11-30
# Python 3.4

"""

第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果

"""

from PIL import Image, ImageDraw, ImageFont
import sys

def add_num_to_img(file_path):
    im = Image.open(file_path)
    im_draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", int(im.size[0]/5))
    im_draw.text((int(im.size[0]-im.size[0]/10), 5), "4", (256, 0, 0), font=font)
    del im_draw
    im.save(file_path)

if __name__ == "__main__":
    for infile in sys.argv[1:]:
        try:
            add_num_to_img(infile)
        except IOError:
            pass