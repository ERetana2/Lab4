# -*- coding: utf-8 -*-
"""
@Author: Efrain Retana
@Professor: Olac Fuenters
@TA: Oscar Galindo

"""

import bst

def printSmaller(t,k):
    if t is None:
        return
    temp = t
    if temp.left is not None:
        printSmaller(t.left,k)
    if temp is not None and temp.data < k :
        print(t.data,end=' ')
    if temp.right is not None:
        printSmaller(t.right,k)

def printLeaves(t):
    if t is None:
        return
    temp = t
    
    if temp.left is not None:
        printLeaves(t.left)
    if temp.left is None and temp.right is None :
        print(t.data,end=' ')
    if temp.right is not None:
        printLeaves(t.right)
        
def atDepth(t,d):
    if t is None:
        return
    if d == 0:
        print(t.data,end=' ')
    else:
        atDepth(t.left,d-1)
        atDepth(t.right,d-1)

def depthOf(t,k):
    if t is None:
        return -1
    temp = t
    depth = 0
    inTree = False
    while temp is not None:
        if temp.data == k:
            return depth
        if k > temp.data:
            temp = temp.right
            depth+=1
        elif k <= temp.data:
            temp = temp.left 
            depth+=1
        else:
            inTree = True
            break
    if not inTree:
        return -1
    return depth
            
         

    
    
    
    
if __name__ == '__main__':
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    T = bst.BST()

    for a in A:
        T.insert(a)
        
    printSmaller(T.root,6)
    print()
    printLeaves(T.root)
    print()
    atDepth(T.root,2)
    print()
    print(depthOf(T.root,65))
    

