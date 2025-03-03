import matplotlib.pyplot as plt
import numpy as np
import btree
# finds the smallest number in the tree
def smallest(T):
    if T.root.data == [] and T.root.is_leaf:
        return -1
    if T.root.is_leaf: # base case that returns smallest element if root is leaf node
        return T.root.data[0]
    temp = T.root
    # iter to the leftmost part of the tree
    while not temp.is_leaf:
        temp = temp.child[0]
    return temp.data[0]
# finds the largest number in the tree
def largest(T):
    if T.root.data == [] and T.root.is_leaf:
        return -1
    if T.root.is_leaf: # return the last element in the root list if it is leaf node
        return T.root.data[-1]
    temp = T.root
    #iter through the right most part of the tree
    while not temp.is_leaf:
        temp = temp.child[-1]
    return temp.data[-1]

def numItems(T):
    if T.root.data == [] and T.root.is_leaf:
        return 0
    #iterate through items using the root
    return recur_numItems(T.root)

def recur_numItems(T): # wrapper function for numItems
    currNum = 0
    # base case when t is a leaf node
    if T.is_leaf:
        return len(T.data)
    
    for i in range(len(T.child)):
        currNum += recur_numItems(T.child[i])
    currNum += len(T.data)
    
    return currNum

if __name__ == "__main__":
    plt.close('all')
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    for num in nums:
        T.insert(num)
        
    T.draw()

    print(smallest(T))  # 1
    print(largest(T))   # 30
    print(numItems(T))  # 30

