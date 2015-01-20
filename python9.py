from bs4 import BeautifulSoup
import urllib

url = "http://www.baidu.com/s?wd=Android&rsv_spt=1&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug2=0&inputT=10"
html = urllib.urlopen(url)

soup = BeautifulSoup(html)

n = 0
for link in soup.find_all('a'):
	a = link.get('href')
	n += 1
	if "baidu" in str(a):
		print a

print n