#Filename:21.py
#-*- coding:utf-8 -*-

from Crypto.Hash import SHA

h = SHA.new()
h.update("hello world")
print h.hexdigest()
