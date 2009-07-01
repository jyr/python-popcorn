#!/usr/bin/python

# The MIT License
#
# Copyright (c) 2009 Osvaldo Jair Gaxiola Mercado
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

'''A wrapper library for popcorn Mexico http://popcornmexico.com'''

__author__ =  'jyr.gaxiola@gmail.com'
__version__ = '0.0.1'

from urllib2 import urlopen, Request
from urllib import urlencode

class Api:
    def __init__(self):
        pass
        
    def search(self, day = None, place = None, hour = None, movie = None):
        self.day = day
        self.place = place
        self.hour = hour
        self.movie = movie
        
        self.url = 'http://popcornmexico.com/WebServices/simpleQuery_V1.php?'
        self.query = self.day + ' ' + self.place + ' ' + self.hour + ', ' + self.movie 
        self.values = {'input': self.query}
        
        self.params = urlencode(self.values)
        self.response = urlopen(self.url + self.params)
        self.page = self.response.read()
        print self.page
