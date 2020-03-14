"""
@Author: Efrain Retana
@Professor: Olac Fuentes
@TA: Oscar Galindo
@Assignment: Exercises BTrees 3
"""

import btree
import matplotlib.pyplot as plt
import math

def largestAtDepthD(T,d):
    # base case to check that d is not out of range
    if d > T.height() or d < 0:
        return - math.inf
    if type(T) == btree.BTree: # convert tree to iterable node
        T = T.root
    if T.data == []: # if tree is empty
        return - math.inf
    temp = T
    #iterate to the farthest right side of the tree until its leaf then return data[-1]
    while not temp.is_leaf and d != 0:
        temp = temp.child[-1]
        d -= 1
    return temp.data[-1]

def findDepth(t,k): 
    if type(t) == btree.BTree:  # make tree into iterable node
        t = t.root
    # if k in data return 0
    if k in t.data:
        return 0
    # if k is not in the tree return -1
    if t.is_leaf:
        return -1
    # increment until we find the branch that most be iterated to
    i = 0
    while i < len(t.data) and k > t.data[i]:
        i += 1
        
    count = findDepth(t.child[i],k) # recursive call for child of tree to find k
    # if it does not find k, return -1
    if count == -1:
        return -1
    return count  + 1
        

    
def printAtDepthD(t,d):
    if type(t) == btree.BTree: #make tree into iterable node
        t = t.root
        #iterate through each branch recursively until it finds depth d then print its node data
    for i in range(len(t.child)):
        if d != 0 and t.is_leaf:
            return
        if d == 0:
            for i in t.data:
                print(i,end =' ')
            break
        printAtDepthD(t.child[i],d-1)
    
def numLeaves(t):
    if type(t) == btree.BTree: # iterable node
        t = t.root
    count = 0
    # if finds leaf return 1
    if t.is_leaf: # when t is a leaf return 1
        return 1
    # iterate through all the tree and count Nodes
    for i in range(len(t.child)):
        count += numLeaves(t.child[i])
    return count

def fullNodesAtDepthD(t,d):
    if type(t) == btree.BTree: # iterable node
        t = t.root
    if t.is_leaf and d != 0: # if d is out of range of tree height
        return 0
    # if it finds depth d and node is full return 1
    if d == 0 and t.is_full():
        return 1
    count = 0
    #iterate through each branch of the tree recursively
    for i in t.child:
        count += fullNodesAtDepthD(i,d-1)
    return count
#---------------------------------
def printDescending(t):
    # print the list in reverse
    l = printDescending_n(t)
    for i in range(1,len(l)+1):
        print(l[-i],end= ' ')
        
def printDescending_n(t): # wrapper function for printDescending
    if type(t) == btree.BTree: #makes iterable node
        t = t.root
    tempL = []
    # when at leaf, add the node data to a list and return the list
    if t.is_leaf:
        tempL.extend(t.data)
        return tempL
    # iterate through each branch of the tree, but add the returned list to the current list
    for i in range(len(t.child)):
        tempL.extend(printDescending_n(t.child[i]))
        # if i is less than the amount of childs - 1, then append current node data[i]
        if i != len(t.child) - 1:
            tempL.append(t.data[i])
    return tempL
#--------------------------------            

def printItemsInNode(t,k):
    if type(t) == btree.BTree:  # make tree into iterable node
        t = t.root
    # if k is in current nodes data, print the data
    if k in t.data:
        for i in t.data:
            print(i,end = ' ')
        return
    # if t is leaf and doest not contain k, return
    if t.is_leaf:
        return
    # increment to desired child of tree, then recursively traverse that child[i]
    i = 0
    while i < len(t.data) and k > t.data[i]:
        i += 1
    printItemsInNode(t.child[i],k)

            
if __name__ == "__main__":
    plt.close('all')
    
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    t = T.find(4)
    for num in nums:
        T.insert(num)
        
    T2 = btree.BTree()   
    for num in [32,12,58,7,43]:
        T2.insert(num)
        
    T_empty = btree.BTree()
    
    T.draw()
    T2.draw()
    print('---------------')
    print(largestAtDepthD(T,0)) # 17
    print(largestAtDepthD(T,1)) # 27
    print(largestAtDepthD(T,2)) # 30
    print(largestAtDepthD(T,3)) # -inf
    
    print(largestAtDepthD(T2,0)) # 58
    print(largestAtDepthD(T2,1)) # -inf
    
    print(largestAtDepthD(T_empty,0)) # -inf 
    print(largestAtDepthD(T_empty,1)) # -inf
    print('--------------')
    print(findDepth(T,17)) # 0
    print(findDepth(T,11)) # 1
    print(findDepth(T,18)) # 2
    print(findDepth(T,31)) # -1
    
    print(findDepth(T2,7)) # 0
    print(findDepth(T2,61)) # -1
    
    print(findDepth(T_empty,0)) # -1
    print('--------------')
    printAtDepthD(T,0) # 17
    print()
    printAtDepthD(T,1) # 6 11 23 27
    print()
    print('--------------')
    
    print(numLeaves(T.root))         # 6
    print(numLeaves(T2.root))        # 1
    print(numLeaves(T_empty.root))   # 1
    print('--------------')
    
    print(fullNodesAtDepthD(T,0)) # 0
    print(fullNodesAtDepthD(T,1)) # 0
    print(fullNodesAtDepthD(T,2)) # 3
    print(fullNodesAtDepthD(T,3)) # 0
    
    print(fullNodesAtDepthD(T2,0)) # 1
    print(fullNodesAtDepthD(T2,1)) # 0
    
    print(fullNodesAtDepthD(T_empty,0)) # 0
    print(fullNodesAtDepthD(T_empty,1)) # 0
    print('--------------')
    
    printDescending(T)  # 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
    print()
    printDescending(T2) # 58 43 32 12 7 
    print()
    print('--------------')
    printItemsInNode(T,3)   # 1 2 3 4 5
    printItemsInNode(T,32)  #
    print()
    printItemsInNode(T2,43) # 7 12 32 43 58
    printItemsInNode(T2,20) #