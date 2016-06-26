# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 09:30:28 2016

@author: Richard
"""

from calculator import *
    
def test_add():
    assert add(1, 1) == 2
    assert add(0, -12.5) == -12.5
    
def test_subtract():
    assert subtract(5, 4) == 1
    assert subtract(9, 12) == -3
    
def test_multiply():
    assert multiply(5, 5) == 25
    
def test_divide():
    assert divide(10, 2) == 5
    assert divide(3, 0) == None