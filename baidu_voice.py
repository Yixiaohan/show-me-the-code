# -*- coding:utf-8 -*-
import requests
import urllib
from settings import CLIENT_ID, CLIENT_SECRET, CUID


def get_access_token(client_id, client_secret):
	base_access_token_url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'
	full_access_token_url = base_access_token_url.format(client_id=client_id, client_secret=client_secret)
	resp = requests.get(full_access_token_url).json()
	return resp.get('access_token')


def text_to_voice(text, cuid, token):
	base_url = 'http://tsn.baidu.com/text2audio?tex={text}&lan=zh&cuid={cuid}&ctp=1&tok={token}'
	full_url = base_url.format(text=text, cuid=cuid, token=token)
	print full_url
	urllib.urlretrieve(full_url, text + '.mp3')
	resp = requests.get(full_url)
	return resp


if __name__ == '__main__':
	token = get_access_token(CLIENT_ID, CLIENT_SECRET)
	text = '我有点喜欢你'
	text_to_voice(text, CUID, token)
	
