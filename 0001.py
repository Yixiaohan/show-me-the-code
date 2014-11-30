# Source:https://github.com/renzongxian/show-me-the-code
# Author:renzongxian
# Date:2014-11-30
# Python 3.4

"""

做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？

"""

import uuid


def generate_key():
    key_list = []
    for i in range(200):
        uuid_key = uuid.uuid3(uuid.NAMESPACE_DNS, str(uuid.uuid1()))
        key_list.append(str(uuid_key).replace('-', ''))
    return key_list

if __name__ == '__main__':
    print(generate_key())