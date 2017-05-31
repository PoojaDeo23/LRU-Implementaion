
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:52:32 2017
Implemented Doubly link list datasturcutre 
@author: poojadeo
"""

class Node :
  def __init__( self, data,key ) :
    self.data = data
    self.key = key
    self.next = None
    self.prev = None

class LinkedList :
    def __init__( self ) :
        self.head = None
        self.tail = None

    def push( self, node ) :
        '''Push new values in the list incresing Head(priority) with each insert '''
        if self.head == None :
            self.head = node
            self.tail = node
        else :
            node.next = self.head
            node.next.prev = node
            self.head = node

            
    def pop(self):
        '''Pops the last(Tail) node out of the list'''
        old_last_node = self.tail
        to_be_last = self.tail.prev
        to_be_last.next = None
        old_last_node.prev = None
        self.tail= to_be_last
        return old_last_node
    

    def remove( self, p ) :
       '''Remove node from amywhere in list'''
       if p == self.head:
           self.head=p.next
           p.next.prev= None
       elif p == self.tail :
           self.tail=p.prev
           p.prev.next=None
       else:
           p.prev.next = p.next
           p.next.prev = p.prev
    
    def returnlist(self):
        rlist=[]
        p=self.head
        if p != None:
            while p != None:
                rlist.append(p.data)
                p=p.next
        return rlist


  

