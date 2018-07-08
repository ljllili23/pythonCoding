# -*- coding: utf-8 -*-
"""
Created on 2018/8/8

@author: LeeJiangLee
"""

import curses

def main(stdrc):
    print('hello world')
    curses.use_default_color('blue')
curses.wrapper(main)