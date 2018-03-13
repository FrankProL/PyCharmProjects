#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/9 11:32
# @Author  : Frank
# @Site    : 
# @File    : ConfigParser_test4.py
# @Software: PyCharm
"""
import ConfigParser
"""Defaults are available in all three types of ConfigParsers. They are used in interpolation if an option used is not defined elsewhere."""

# New instance with 'bar' and 'baz' defaulting to 'Life' and 'hard' each
config = ConfigParser.SafeConfigParser({'bar': 'Life', 'baz': 'hard'})
config.read('example.cfg')

print config.get('Section1', 'foo')  # -> "Python is fun!"
config.remove_option('Section1', 'bar')
config.remove_option('Section1', 'baz')
print config.get('Section1', 'foo')  # -> "Life is hard!"

