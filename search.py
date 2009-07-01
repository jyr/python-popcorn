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

from popcorn import Api
import sys

params = []

if len(sys.argv) >= 6 or len(sys.argv) == 1:
    print "Usage: \n\tpython search \'day\' \'place\' \'hour\' \'movie\'"
    print "\tpython search \'day\' \'place\' \'hour\'"
    print "\tpython search \'day\' \'place\'"
    print "\tpython search \'place\'"
    sys.exit(-1)

for i in range(len(sys.argv)):
    if i != 0:
        params.append(sys.argv[i])

if len(params) == 4:
    day = params[0]
    place = params[1]
    hour = params[2]
    movie = params[3]
    
if len(params) == 3:
    day = params[0]
    place = params[1]
    hour = params[2]
    movie = ''

if len(params) == 2:
    day = params[0]
    place = params[1]
    hour = ''
    movie = ''

if len(params) == 1:
    day = ''
    place = params[0]
    hour = ''
    movie = ''

api = Api()
query = api.search(day, place, hour, movie)