#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:52:06 2017
Implemented LRU using Doubly Linkedlist and Dictionary to keep time complexity as constant - 0(1)
@author: poojadeo
"""



    
from collections import deque
from dllist import *

    
class LRUCache(object):
    """A sample class that implements LRU algorithm"""

    def __init__(self, length):
        
        self.valueDict={}
        self.hash = {}
        self.length=length
        self.linked_list = LinkedList()

    def push(self, key, value):
        """Insert new items to cache"""

        if key in self.hash:
            # Move the existing item to the head of item_list.
            delnode=self.hash[key]
            self.linked_list.remove(delnode)
            delnode.data=value
            self.linked_list.push(delnode)
            self.hash[key]=delnode
            
        else:

            # If this is a new item, just append it to
            # the front of item_list.
            # If Cache is full then First Pop least recent item from the list
            if len(self.hash)>=self.length:
                delnode=self.linked_list.pop()         
                self.hash.pop(delnode.key)
            addnode=Node(data=value,key=key)
            self.linked_list.push(addnode)
            
            self.hash[key] = addnode
            


    def pop(self,key):
        # When We get the item- pop and append this item to set its priority highest
        if key in self.hash:
            node =self.hash[key]
            self.linked_list.remove(node)
            self.linked_list.push(node)
            return node.data
        else:
            return -1
            
    def printCache(self):
        #print cache items from doubly link listd
        rlist=self.linked_list.returnlist()
        for i in rlist:
            print(i)
         
  
        

    def getItem(self,key):
        # When We get the item- pop and append this item to set its priority highest
        if key in self.hash:
            node =self.hash[key]
            self.linked_list.remove(node)
            self.linked_list.push(node)
            return node.data
        else:
            return -1


