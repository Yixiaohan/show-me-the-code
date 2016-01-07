"""
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？

激活码格式:
19个字符组成,分成4组,中间用"-"连接起来
必须同时包含大小写字母数字

"""
import random
import string


def generate_active_code():
    active_code = []
    ascii_ = list(string.ascii_letters)
    for i in range(200):
        active_code_temp = ""
        for j in range(19):
            num_or_char = random.randint(0, 1)
            # 用"-"连接
            if j == 4 or j == 9 or j == 14:
                active_code_temp = active_code_temp + "-"
            # 生成数字
            elif num_or_char == 0:
                active_code_temp = active_code_temp + str(random.randint(0, 9))
            # 生成字符
            elif num_or_char == 1:
                active_code_temp = active_code_temp + \
                    str(ascii_[random.randint(0, len(ascii_) - 1)])
        active_code.append(active_code_temp)

    return active_code

if __name__ == "__main__":
    active_code = generate_active_code()
    print(active_code)
