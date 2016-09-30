# -*- coding:utf-8 -*-
import urllib2
import re
import socket

def getProxy():
	url = 'http://www.66ip.cn/nmtq.php?getnum=10&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=1&proxytype=0&api=66ip'

	doc = urllib2.urlopen(url).read()

	proxies = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\:[0-9]{1,4}', doc)
	ls_return = []
	for proxy in proxies:
		print proxy
		proxy_h = urllib2.ProxyHandler({'http': proxy})
		opener = urllib2.build_opener(proxy_h)
		req = urllib2.Request('http://www.baidu.com')
		try:
			opener.open(req, timeout = 3)
			ls_return.append(proxy)
			print 'OK.'
		except urllib2.HTTPError:
			print 'BAD PROXY.'
		except urllib2.URLError as e:
			print e.reason
		except socket.timeout:
			print 'TIME OUT.'
	return ls_return
print getProxy()