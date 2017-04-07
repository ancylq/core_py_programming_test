# coding:utf-8
import os
import re

with os.popen('who', 'r') as f:
    for eachline in f:
        print re.split(r'\s\s+|\t', eachline.rstrip())