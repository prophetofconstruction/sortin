#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:40:02 2018

@author: poc
"""

import unittest 
import numpy as np
import random

from sortin_funcs import insertion, selection


class TestSortinFuncs(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        random.seed(10)
    
#    @classmethod
#    def compare(cls, sortin_func):
#        cls.assertTrue(sortin_func([]) == [])
#        ints = np.random.randint(-10000, 10000, 100)
#        cls.assertEquals(sortin_func(ints), sorted(ints))
#        floats = np.random.uniform(-10000, 10000, 100)
#        cls.assertEquals(sortin_func(floats), sorted(floats))
        
        
    def test_insertion(self):
#        self.compare(insertion)
        self.assertTrue(insertion([]) == [])
        ints = np.random.randint(-10000, 10000, 100)
        self.assertTrue(all(insertion(ints) == sorted(ints)))
        floats = np.random.uniform(-10000, 10000, 100)
        self.assertTrue(all(insertion(floats) == sorted(floats)))
        
    def test_selection(self):
        self.assertTrue(selection([]) == [])
        ints = np.random.randint(-10000, 10000, 100)
        self.assertTrue(all(selection(ints) == sorted(ints)))
        floats = np.random.uniform(-10000, 10000, 100)
        self.assertTrue(all(selection(floats) == sorted(floats)))
        