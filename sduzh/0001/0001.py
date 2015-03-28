#!/usr/bin/python
# -*- coding: utf-8 -*-
# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用
# 生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码
# （或者优惠券）？

import uuid

def create_code(counts = 200):
	result = []
	while len(result) < counts:
		x= str(uuid.uuid1())
		if not x in result:
			result.append(x)
	return result


if __name__ == "__main__":
	print create_code()
