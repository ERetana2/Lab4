"""
@author: Efrain Retana
"""
import bst
import math
import matplotlib.pyplot as plt
import queue

def smallest(t):
    temp = t
    min = math.inf
     
    while temp is not None:
        if temp.data < min:
            min = temp.data
        if temp.left is not None:
            temp = temp.left
        elif temp.right is not None:
            temp = temp.right
        else:
            return min
        
def largest(t):
    temp = t
    max = -math.inf
     
    while temp is not None:
        if temp.data > max:
            max = temp.data
        if temp.right is not None:
            temp = temp.right
        elif temp.left is not None:
            temp = temp.left
        else:
            return max
        
def isLeftChild(x):
    if t.parent is not None:
        return t.parent.left == x
    return False

def printByLevel(t):
    if t is None:
        return
    temp = t
    tempQueue = queue.Queue(40)
    
    tempQueue.put(temp)
    
    print(tempQueue.not_empty)
    while not tempQueue.empty():
        currNode = tempQueue.get()
        print(currNode.data,end = ' ')
        
        if currNode.left is not None:
            tempQueue.put(currNode.left)
        if currNode.right is not None:
            tempQueue.put(currNode.right)
    
    
    
if __name__ == "__main__":

    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    B =[8, 15, 5, 13, 11, 6, 7, 2, 4, 18, 14]
    

    T = bst.BST()
    T2 = bst.BST()
    
    for a in A:
        T.insert(a)

    for b in B:
        T2.insert(b)

    T.inOrder()
    plt.close('all')
    T.draw()
    T2.draw()
    
    print(smallest(T.root)) # 1
    print(largest(T.root))  # 20
    
    print(smallest(T2.root)) # 2
    print(largest(T2.root))  # 18
    
    t = T.find(14)
    print(isLeftChild(t))   # True
    
    t = T.find(4)
    print(isLeftChild(t))   # False
    
    t = T2.find(14)
    print(isLeftChild(t))   # True
    
    t = T2.find(8)
    print(isLeftChild(t))   # False
    
    print('Tree size:',T.size)
    
    printByLevel(t)
    
    