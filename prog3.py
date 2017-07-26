# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:54:25 2017

@author: Student
"""

from bs4 import BeautifulSoup
import requests

data = requests.get('http://badstudio.in/')

soup = BeautifulSoup(data.text, 'lxml')
#print data.text

i = 1+5
print i
