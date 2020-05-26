#binary tree 
#class that represents an individual role in binary tree
class Node():
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

# creating root of the tree 
root = Node(1)
''' following is the tree after above statement 
        1 
      /   \ 
     None  None'''

root.left = Node(2)
root.right = Node(3)

''' 2 and 3 become left and right children of 1 
           1 
         /   \ 
        2      3 
     /    \    /  \ 
   None None None None'''

'''
Properties of a binary tree :

1) The maximum number of nodes at level ‘0’ of a binary tree is 2^l.If the root node is at level '1'
then the maximum nuber of nodes is 2^(l-1)

2) Maximum number of nodes in a binary tree of height ‘h’ is 2h – 1.Here height of a tree is maximum
number of nodes on root to leaf path. Height of a tree with single node is considered as 1.

A tree has maximum nodes if all levels have maximum nodes. So maximum number of nodes in a binary tree
 of height h is 1 + 2 + 4 + .. + 2h-1. This is a simple geometric series with h terms and sum of this
 series is 2h – 1. 

3) In a Binary Tree with N nodes, minimum possible height or minimum number of levels is  Log2(N+1)   
This can be directly derived from point 2 above. If we consider the convention where height of a leaf
 node is considered as 0, then above formula for minimum possible height becomes Log2(N+1) – 1

 
4) A Binary Tree with L leaves has at least   ? Log2L ? + 1   levels
A Binary tree has maximum number of leaves (and minimum number of levels) when all levels are fully
 filled. Let all leaves be at level l, then below is true for number of leaves L.

   L =  2l-1  [From Point 1]
   l =  Log2L + 1 
   where l is the minimum number of levels. 

5) In Binary tree where every node has 0 or 2 children, number of leaf nodes is always one more than
 nodes with two children.

   L = T + 1
Where L = Number of leaf nodes
      T = Number of internal nodes with two children  

'''

