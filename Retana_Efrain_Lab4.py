# -*- coding: utf-8 -*-
"""
@author: Efrain Retana
@Professor: Olac Fuentes
"""

# Implementation of binary search trees using lists
import matplotlib.pyplot as plt
import numpy as np

def insert(T,newItem): # Insert newItem to BST T
    if T == None:  # T is empty
        T = [newItem,None,None]
    else:
        if newItem< T[0]:
            T[1] = insert(T[1],newItem) # Insert newItem in left subtree
        else:
            T[2] = insert(T[2],newItem) # Insert newItem in right subtree
    return T

def inOrder(T):
    if T!=None:
        inOrder(T[1])
        print(T[0],end=' ')
        inOrder(T[2])
    
if __name__ == "__main__":
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 20, 13]             
    T = None

    for a in A:
        print('Inserting',a)
        T = insert(T,a)   
        print(T)    
        