#!/usr/bin/python
import random
import urllib
import re
import simplejson
for x in xrange(1,10):
	ip=random.choice(['58.56.','60.209.','110.96.','101.104.','101.236.','101.244.','106.52.','112.124.','123.64.','175.48.','175.64.','221.216.','42.208.','117.112.'])
	ip += ".".join(map(str, (random.randint(0, 255)
							for _ in range(2))))
	url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip
	f = urllib.urlopen(url).read()
	s = simplejson.loads(f) 
	#print ip+": "+s['data']['country']+s['data']['area']+s['data']['region']+s['data']['city']+s['data']['isp']
	print ip
