# -*- coding:utf8 -*-
# Source:https://github.com/renzongxian/show-me-the-code
# Author:renzongxian
# Date:2014-12-06
# Python 2.7

"""
将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。 

"""

import uuid
import redis


def generate_key():
    key_list = []
    for i in range(200):
        uuid_key = uuid.uuid3(uuid.NAMESPACE_DNS, str(uuid.uuid1()))
        key_list.append(str(uuid_key).replace('-', ''))
    return key_list


def write_to_redis(key_list):
    re = redis.StrictRedis(host='localhost', port=6379, db=0)
    for i in range(200):
        re.sadd('ukey', key_list[i])


if __name__ == '__main__':
    write_to_redis(generate_key())
