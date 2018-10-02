#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:31:23 2018

@author: poc
"""

def insertion(array):
    for i in range(len(array)):
        while i - 1 >= 0:
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                i -= 1
            else:
                break
    return array


def selection(array):
    for i in range(len(array)):
        min_ix = i
        for j in range(i, len(array)):
            if array[j] < array[min_ix]:
                min_ix = j
        array[i], array[min_ix] = array[min_ix], array[i]
    return array
            

def mergesort(array):
    """
    """
    def merge_sorted(array1, array2):

    l1 = len(array1)#  left array length
    l2 = len(array2) #  right array legnth
    new_array = [0] * (l1 + l2)
    
    ix1 = 0
    ix2 = 0

    while ix1 < l1 and ix2 < l2:
        if array1[ix1] <= array2[ix2]:
            new_array[ix1 + ix2] = array1[ix1]
            ix1 += 1
        else:
            new_array[ix1 + ix2] = array2[ix2]
            ix2 += 1

    if ix1 < l1:
        new_array[ix1 + ix2 :] = array1[ix1:]
    else:
        new_array[ix1 + ix2 :] = array2[ix2:]
    return new_array
            
    
    if len(array) <= 1:
        return array
    return merge_sorted(mergesort(array[:len(array)//2]), mergesort(array[len(array)//2 :]))
            
    
