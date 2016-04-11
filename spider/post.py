#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: post.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.04.07
#########################################################################

import urllib
import urllib2

values = {'username':"xxxxx@126.com", 'password':'xxxxxx'}
data = urllib.urlencode(values)
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()
