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
#--------------------------------
#PROBLEM 1
def size(T):
    if T is None:
        return 0
    return 1 + size(T[1]) + size(T[2])
#--------------------------------
#PROBLEM 2
def minimum(T):
    if T is None:
        return
    if T[1] is None and T[2] is None:
        return T[0]
    
    return minimum(T[1])
#--------------------------------
#PROBLEM 3
def maximum(T):
    if T is None:
        return
    if T[1] is None and T[2] is None:
        return T[0]
    
    return maximum(T[2])
#--------------------------------
#PROBLEM 4
def height(T):
    if T is None:
        return -1
    left_tree = 1 + height(T[1])
    right_tree = 1 + height(T[2])
    
    return max(left_tree,right_tree)
#----------------------------------
#PROBLEM 5
def inTree(T,i):
    if T is None:
        return False
    if T[0] == i:
        return True
    
    if i < T[0]:
        return inTree(T[1],i)
        
    elif i > T[0]:
        return inTree(T[2],i)
        
#--------------------------------
#PROBLEM 6
def printByLevel(T):
    if T is None:
        return
    L = []
    L.append(T)
    
    while len(L) > 0:
        for i in range(len(L)):
            currList = L.pop(0)
            print(currList[0],end=' ')
            
            if currList[1] is not None:
                L.append(currList[1])
            if currList[2] is not None:
                L.append(currList[2])
        print()
#---------------------------------
#PROBLEM 7
def tree2List(T):
    if T is None:
        return []
    return tree2List(T[1]) + [T[0]] + tree2List(T[2])
#----------------------------------------------------
#PROBLEM 8
def leaves(T):
    if T is None:
        return
    if T[1] is None and T[2] is None:
        print(T[0],end=' ')
    leaves(T[1])
    leaves(T[2])
#--------------------------------------------------
#PROBLEM 9
def itemsAtDepthD(T,d):
    if T is None:
        return [] 
    if d == 0:
        return [T[0]]
    else:
        return itemsAtDepthD(T[1],d-1) + itemsAtDepthD(T[2],d-1)
#--------------------------------------------------
#PROBLEM 10
def depthOfK(T,k):
    counter,temp = 0,T
    found = False
    
    while temp is not None:
        if temp[0] < k:
            temp = temp[2]
            counter += 1
        elif temp[0] > k:
            temp = temp[1]
            counter += 1
        else:
            found = True
            return counter
    if not found:
        return -1
    return counter
#-----------------------------------------------------------------
#PROBLEM 11
def draw(T,ax,x0=0,y0=0,delta_x=1000,delta_y=120):
    delta_x = max([20,delta_x])
    if T[1] is not None:
        ax.plot([x0-delta_x,x0],[y0-delta_y,y0],linewidth=1.5,color='gray')
        draw(T[1],ax, x0-delta_x, y0-delta_y, delta_x/2, delta_y)
    if T[2] is not None:
        ax.plot([x0+delta_x,x0],[y0-delta_y,y0],linewidth=1.5,color='gray')
        draw(T[2],ax, x0+delta_x, y0-delta_y, delta_x/2, delta_y)
    ax.text(x0,y0, str(T[0]), size=14,ha="center", va="center",
        bbox=dict(facecolor='r',boxstyle="circle"))
    
    
    
if __name__ == "__main__":
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 20, 13]             
    T = None

    for a in A:
        print('Inserting',a)
        T = insert(T,a)   
        print(T)    
    inOrder(T)
    print()
    print(inTree(T,14))
    printByLevel(T)
    print(tree2List(T))
    leaves(T)
    print()
    print(itemsAtDepthD(T,3))
    print(depthOfK(T,16))
    plt.close('all')
    fig,ax = plt.subplots()
    draw(T,ax)