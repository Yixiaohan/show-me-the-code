#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小

from PIL import Image
import os, sys


if len(sys.argv) != 2:
	print "Usage: {0} <Image Directory>".format(sys.argv[0])

outdir = "resize_output"
if not os.path.exists(outdir):
	os.mkdir(outdir)

for root, dirnames, filenames in os.walk(sys.argv[1]):
	for infile in filenames:
		im = Image.open(os.path.join(root, infile))
		im.thumbnail((1136,640), Image.ANTIALIAS)
		im.save(os.path.join(outdir, infile))
