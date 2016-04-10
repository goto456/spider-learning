#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: test.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.04.07
#########################################################################

import urllib2

#response = urllib2.urlopen('http://www.baidu.com')
#print response.read()

request = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(request)
print response.read()
