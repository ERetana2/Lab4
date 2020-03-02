"""
@author: Efrain Retana
"""
import bst
import math
import matplotlib.pyplot as plt

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
    return x.parent.left.data == x.data
    
    
if __name__ == "__main__":

    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    T = bst.BST()

    for a in A:
        T.insert(a)

    T.inOrder()
    plt.close('all')
    T.draw()
    print('Tree size:',T.size)
    
    print(smallest(T.root))
    print(largest(T.root))
    
    t = T.find(14)
    print(isLeftChild(t))
    
    