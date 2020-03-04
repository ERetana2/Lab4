
"""
@Professor: Olac Fuentes
@Author: Efrain Retana
"""
import bst
import matplotlib.pyplot as plt

def childrenOfRoot(t):
    # count the children of the root ,0 or 1 or 2 max
    if t is None:
        return 0
    count = 0
    # check left side
    if t.root.left is not None:
        count += 1
    # check right side
    if t.root.right is not None:
        count += 1
    return count

def rootPredecessor(t):
    # if tree is empty
    if t is None:
        return
    
    temp = t.left
    # iter to the farthest right on the right subtree
    if temp.left is None :
        return
    while temp is not None:
        if temp.right is not None:
            temp = temp.right
        else:
            break
    return temp.data
            
    
def treeToList(t):
    # if tree is empty
    if t is None:
        return []
    #iterate through the left side of the tree and add a list containing [t.data]
    # then iterate through the right side of the tree
    return treeToList(t.left) + [t.data]+ treeToList(t.right)

if __name__ == "__main__":

    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    B =[25, 13, 11, 6, 7, 18, 14]
    

    T = bst.BST()
    T2 = bst.BST()
    
    for a in A:
        T.insert(a)

    for b in B:
        T2.insert(b)

    plt.close('all')
    T.draw()
    T2.draw()
    
    print(childrenOfRoot(T))  # 2
    print(childrenOfRoot(T2)) # 1
    
    print(rootPredecessor(T.root))  # 8
    print(rootPredecessor(T2.root)) # 18
    
    print(treeToList(T.root))  # [1, 2, 4, 6, 7, 8, 11, 13, 14, 15, 16, 17, 18, 20]
    print(treeToList(T2.root)) # [6, 7, 11, 13, 14, 18, 25]
