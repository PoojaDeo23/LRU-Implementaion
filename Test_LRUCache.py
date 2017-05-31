#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:52:32 2017
This file tests the implemented LRU
@author: poojadeo
"""


from LRUCache import *
from time import sleep


def print_cache(cache):
    for key in cache.hash:
        print ("key: {1} ".format(key))

        
print ("Initial cache items.")
cache = LRUCache(length=3)
print ("Cache Created with lenght = 3 and following values")
cache.push(1,"one")
cache.push(2,"two")
cache.push(3,"three")
cache.printCache()
print ("#" * 20)

print ("Insert a existing item with Key= 2 but value= 'Five' ")
cache.push(2,"five")
cache.printCache()
print ("#" * 20)

print ("Insert another existing item with Key 3 abd Value = 'Three'")
cache.push(3,"three")
cache.printCache()
print ("#" * 20)


print ("Insert new item with key=4 Value='Four'")
cache.push(4,"four")
cache.printCache()
print ("#" * 20)

print ("Get item with key=2 Value='Five'")
node=cache.getItem(2)
print(node)
print ("#" * 20)