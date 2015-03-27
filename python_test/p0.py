#!/bin/env python
# -*- coding: utf-8 -*- 

import string
import random
import os
from PIL import Image, ImageFont, ImageDraw


def get_letters():
    i = ''
    for loop in range(4):
        i += random.choice(string.letters)
    return i.decode('utf-8')

def draw_pic(letters):
    im = Image.new('1', (300, 300), 'white')
    draw = ImageDraw.Draw(im)
    draw.text((150, 150), letters)
    im.save("result.png")

def main():
    letters = get_letters()
    draw_pic(letters)

if __name__ == '__main__':
    main()