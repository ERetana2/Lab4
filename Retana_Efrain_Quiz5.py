# =============================================================================
# @Author: Efrain Retana
# @Professor: Olac Fuentes
# @TA: Oscar Galindo
# @Assignment: Quiz 5
# =============================================================================
import btree
import matplotlib.pyplot as plt

def nodeRange(t):
    # base case to check when tree has one element or none
    if len(t.data) <= 1:
        return 0
    return t.data[-1] - t.data[0]

def countNodes(t):
    count = 1
    if t.is_leaf: # when t is a leaf return 1
        return count
    # iterate through all the tree and count Nodes
    for i in range(len(t.child)):
        count += countNodes(t.child[i])
    return count

def countItemsAtDepthD(t,d)  :
    count = 0
    # iterate until depth and return the len of the data at that node
    if d == 0:
        return len(t.data)
    elif d != 0 and t.is_leaf: # base case for out of bounds or no elements
        return 0
    # recurse through the whole tree to find the depth d at each branch
    for i in range(len(t.child)):
        count += countItemsAtDepthD(t.child[i],d-1)
    return count

if __name__ == "__main__":
    plt.close('all')
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    t = T.find(4)
    for num in nums:
        T.insert(num)
        
    T.draw()
    
    print(nodeRange(T.root))  # 0
    t = T.find(4)
    print(nodeRange(t))       # 4
    t = T.find(25)
    print(nodeRange(t))       # 2
    
    print(countNodes(T.root))  # 9
    
    print(countItemsAtDepthD(T.root,0))   # 1
    print(countItemsAtDepthD(T.root,1))   # 4
    print(countItemsAtDepthD(T.root,2))   # 25
    print(countItemsAtDepthD(T.root,3))   # 0
    