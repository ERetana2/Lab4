
"""
@author: Efrain Retana
@Professor: Olac Fuentes 
"""

# Implementation of binary search trees using lists
import matplotlib.pyplot as plt
import numpy as np
import time

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
    if T is None: # base case for empty tree
        return 0 
    # count each node in tree
    return 1 + size(T[1]) + size(T[2])
#--------------------------------
#PROBLEM 2
def minimum(T):
    if T is None:
        return None 
    #iterate to the leftmost part of the tree and return the leaf
    if T[1] is None and T[2] is None:
        return T[0]
    if T[1] is None and T[2] is not None:
        return minimum(T[2])
    
    return minimum(T[1])
#--------------------------------
#PROBLEM 3
def maximum(T):
    if T is None:
        return None
    # iterate to the rightmost part of the tree
    if T[1] is None and T[2] is None:
        return T[0]
    if T[2] is None and T[1] is not None:
        return maximum(T[1])
    
    return maximum(T[2])
#--------------------------------
#PROBLEM 4
def height(T):
    if T is None: #whentree is empty return -1
        return -1
    #check height of right side and the left side
    left_tree = 1 + height(T[1])
    right_tree = 1 + height(T[2])
     # return biggest max of the whole tree
    return max(left_tree,right_tree)
#----------------------------------
#PROBLEM 5
def inTree(T,i):
    if T is None: # if empty return false
        return False
    if T[0] == i: # if found return true
        return True
     # iterate to left or right depending whether i < T[0] or greater
    if i < T[0]:
        return inTree(T[1],i)
        
    elif i > T[0]:
        return inTree(T[2],i)
        
#--------------------------------
#PROBLEM 6
def printByLevel(T):
    if T is None: # when tree is none return
        return
    L = []
    L.append(T)
    # create a queue and print level bt level of true
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
    # base case to return empty list, then concatenate left side of tree and right side
    if T is None:
        return []
    return tree2List(T[1]) + [T[0]] + tree2List(T[2])
#----------------------------------------------------
#PROBLEM 8
def leaves(T):
    if T is None: #if tree is empty or 
        return
    # if node is a leaf node then print its data
    if T[1] is None and T[2] is None:
        print(T[0],end=' ')
    # iter left and right side
    leaves(T[1])
    leaves(T[2])
#--------------------------------------------------
#PROBLEM 9
def itemsAtDepthD(T,d):
    if T is None: # base case that returns empty list
        return [] 
    if d == 0: # when height is reached, return a list containing the current node data
        return [T[0]]
    else:
        # iterate to left and right side until depth d
        return itemsAtDepthD(T[1],d-1) + itemsAtDepthD(T[2],d-1)
#--------------------------------------------------
#PROBLEM 10
def depthOfK(T,k):
    counter,temp = 0,T
    found = False
    # check k with current value, then move left or right according to its valuue
    # then increase counter by one each move
    while temp is not None:
        if temp[0] < k:
            temp = temp[2]
            counter += 1
        elif temp[0] > k:
            temp = temp[1]
            counter += 1
        else:
            #if number is found return the depth
            found = True
            return counter
        # if num not in tree return -1
    if not found:
        return -1
    return counter
#-----------------------------------------------------------------
#PROBLEM 11
def draw(T,ax,x0=0,y0=0,delta_x=1000,delta_y=120):
    if T is None: #when tree is empty
        return
    delta_x = max([20,delta_x])
    #draw left branch
    if T[1] is not None:
        ax.plot([x0-delta_x,x0],[y0-delta_y,y0],linewidth=1.5,color='gray')
        draw(T[1],ax, x0-delta_x, y0-delta_y, delta_x/2, delta_y)  # draw line and circle
    # draw right branch
    if T[2] is not None:
        ax.plot([x0+delta_x,x0],[y0-delta_y,y0],linewidth=1.5,color='gray')
        draw(T[2],ax, x0+delta_x, y0-delta_y, delta_x/2, delta_y) # draw line and circle
    ax.text(x0,y0, str(T[0]), size=14,ha="center", va="center", # insert text into node circle
        bbox=dict(facecolor='r',boxstyle="circle"))
    
    
    
if __name__ == "__main__":
    plt.close('all')
    A = np.random.randint(1,1001,200)     
    B =[3,5,6,4,2,1,0]       
    T = None
    T2 = None
    T_empty = None 

    for a in A:
        print('Inserting',a)
        T = insert(T,a)   
        print(T)  
    for b in B:
        T2 = insert(T2,b)   
    inOrder(T)
    print()
    print()
    
    start_time = time.time()
    print(size(T)) # 
    end_time = time.time()
    print('Size Total Time:', end_time - start_time)
    print(size(T2)) # 7
    print(size(T_empty)) # 0
    print()
    
    start_time = time.time()
    print(minimum(T)) # 
    end_time = time.time()
    print('Minimum Total Time:', end_time - start_time)
    print(minimum(T2)) # 0
    print(minimum(T_empty)) # None
    print()
    
    start_time = time.time()
    print(maximum(T)) # 
    end_time = time.time()
    print('Maximum Total Time:', end_time - start_time)
    print(maximum(T2)) # 6
    print(maximum(T_empty)) # None
    print()
    
    start_time = time.time()
    print(height(T))# 
    end_time = time.time()
    print('height Total Time:', end_time - start_time)
    print(height(T2)) # 3
    print(height(T_empty)) # -1
    print()
    
    start_time = time.time()
    print(inTree(T,8)) # 
    end_time = time.time()
    print('inTree Total Time:', end_time - start_time)
    print(inTree(T,0))  # False
    print(inTree(T2,1)) # True
    print(inTree(T_empty,14)) # False
    print()
    
    start_time = time.time()
    printByLevel(T)
    print()
    end_time = time.time()
    print('printByLevel Total Time:', end_time - start_time)
    printByLevel(T2)
    print()
    
    start_time = time.time()
    print(tree2List(T)) # [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15....,49]
    end_time = time.time()
    print('tree2List Total Time:', end_time - start_time)
    print(tree2List(T2)) # [0 1 2 3 4 5 6]
    print(tree2List(T_empty)) # []
    print()
    
    start_time = time.time()
    leaves(T) # 0 4 7 10 13 15 18 21 24 28 31 33 35 39 41 43 45 49 
    print()
    end_time = time.time()
    print('leaves Total Time:', end_time - start_time)
    leaves(T2) # 0 4 6
    print()
    leaves(T_empty)
    print()
    
    start_time = time.time()
    print(itemsAtDepthD(T,3)) # [0,3,6,9,25,34,46]
    end_time = time.time()
    print('itemsAtDepthD Total Time:', end_time - start_time)
    print(itemsAtDepthD(T,2)) # [1,5,19,42]
    print(itemsAtDepthD(T2,1)) # [2,5]
    print(itemsAtDepthD(T2,0)) # [3]
    print(itemsAtDepthD(T_empty,5)) # []
    print()
    
    start_time = time.time()
    print(depthOfK(T,16)) # 6
    end_time = time.time()
    print('DepthOfK Total Time:', end_time - start_time)
    print(depthOfK(T,58)) # -1
    print(depthOfK(T2,0)) # 3
    print(depthOfK(T_empty,10)) # -1
    print()
    
    fig,ax = plt.subplots()
    start_time = time.time()
    draw(T,ax)
    end_time = time.time()
    print('Draw Total Time:', end_time - start_time)
    fig,ax = plt.subplots()
    draw(T2,ax)
    fig,ax = plt.subplots()
    draw(T_empty,ax)