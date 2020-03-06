
"""
@Author: Efrain Retana
@Professor: Olac Fuenters
@TA: Oscar Galindo

"""

import bst
import matplotlib.pyplot as plt

def printSmaller(t,k):
    # print all the values in the tree that are smaller than k
    if t is None: # when tree is empty
        return
    temp = t
    # in order traversal through tree, but only print those values < k
    if temp.left is not None:
        printSmaller(t.left,k)
    if temp is not None and temp.data < k :
        print(t.data,end=' ')
    if temp.right is not None:
        printSmaller(t.right,k)

def printLeaves(t):
    # print the leaves of the binary tree
    if t is None:
        return
    temp = t
    # iterate until you find the node that contains no right or left, and print its data
    if temp.left is not None:
        printLeaves(t.left)
    if temp.left is None and temp.right is None :
        print(t.data,end=' ')
    if temp.right is not None:
        printLeaves(t.right)
        
def atDepth(t,d):
    if t is None: # is empty return empty list
        return []
    if d == 0 : # when we reach desired level, return a list containing current node data
        return [t.data]
    else:
        # iterate through left side and right side
        return atDepth(t.left,d-1) + atDepth(t.right,d-1)  

def depthOfK(t,k):
    # return the depth of the node that contains K
    if t is None: # return 1 when t is empty
        return -1
    temp = t
    depth = 0
    inTree = False
    #iterate through tree until it finds k
    while temp is not None:
        if temp.data == k:
            inTree = True
            return depth
        # each iteration down the tree, increaes the depth and search the data
        if k > temp.data:
            temp = temp.right
            depth+=1
        elif k <= temp.data:
            temp = temp.left 
            depth+=1
    # if never found k
    if not inTree:
        return -1
    return depth
            
def treeToList(t):
    if t is None:
        return []
    # in order list of the tree, left data + current + right 
    return treeToList(t.left) + [t.data] + treeToList(t.right)      

def list2Tree(L):
    if len(L) == 0: # when list is empty return none
        return None
    # find mid of list
    midpoint = len(L)//2
     # set root as a node containing the data of midpoint then create recursive call
     # for left half and then right half, then return the root
    root = bst.BSTNode(L[midpoint])
    root.left = list2Tree(L[:midpoint])
    root.right = list2Tree(L[midpoint+1:])
    
    return  root
    
    
    
if __name__ == '__main__':
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    B =[8, 15, 5, 13, 11, 6, 7, 2, 4, 18, 14]
    
    T_empty = bst.BST()
    T_oneNode = bst.BST()
    T_oneNode.insert(23)
    TA = bst.BST()
    for a in A:
        TA.insert(a)
    TB = bst.BST()
    for b in B:
        TB.insert(b)
    

    plt.close('all')
    TA.draw()
    TB.draw()
    
    printSmaller(T_empty.root, 16) # 
    print()
    printSmaller(T_oneNode.root, 30) # 23
    print()
    printSmaller(TA.root, 16) # 1 2 4 6 7 8 11 13 14 15
    print()
    printSmaller(TA.root, 5)  # 1 2 4
    print()
    printSmaller(TB.root, 2302) # 2 4 5 6 7 8 11 13 14 15 18 
    print()
    
    print(atDepth(T_empty.root,2))      # []
    print(atDepth(T_oneNode.root,0))    # [23]
    print(atDepth(TA.root,0))           # [11]
    print(atDepth(TA.root,2))           # [2, 7, 14, 17]              
    print(atDepth(TA.root,3))           # [1, 4, 8, 13, 15, 18]
    print(atDepth(TA.root,4))           # [20]
    print(atDepth(TA.root,5))           # []
    print(atDepth(TB.root,2))           # [2, 6, 13, 18]
    
    print(depthOfK(T_empty.root,2301))   # -1
    print(depthOfK(T_oneNode.root,0))    # -1
    print(depthOfK(TA.root,11))          # 0
    print(depthOfK(TA.root,6))           # 1
    print(depthOfK(TA.root,18))          # 3
    print(depthOfK(TA.root,21))          # -1
    print(depthOfK(TB.root,11))          # 3             
    
    print(treeToList(TA.root))  # [1, 2, 4, 6, 7, 8, 11, 13, 14, 15, 16, 17, 18, 20]
    print(treeToList(TB.root))  # [2, 4, 5, 6, 7, 8, 11, 13, 14, 15, 18]
    
    A.sort()
    
    root_a = list2Tree(A)
    Ta = bst.BST()
    Ta.root = root_a
    Ta.size = len(A)
    Ta.draw()
    
    L = [i for i in range(31)]
    
    root_a = list2Tree(L)
    Ta = bst.BST()
    Ta.root = root_a
    Ta.size = len(L)
    Ta.draw()
    

