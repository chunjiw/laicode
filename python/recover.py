# Given a Binary Search Tree with only two nodes swapped. Try to find them and recover the binary search tree.

# Input: 

#                4

#               / \

#              2   6  

#             / \   / \

#            1  5 3  7

# Output:       4

#                   / \

#                 2   6

#                /  \   / \

#             1  3   5  7

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def recover(self, root):
    """
    input: TreeNode root
    return: TreeNode
    """
    # write your solution here
    # approach: inorder traversal
    traversal = []
    backward = []
    if not root:
      return root
    self.inorder(root, traversal, backward)
    backward[0].val, backward[-1].val = backward[-1].val, backward[0].val
    return root

  def inorder(self, root, traversal, backward):
    if not root:
      return
    self.inorder(root.left, traversal, backward)
    traversal.append(root)
    if len(traversal) > 1 and root.val < traversal[-2].val:
      backward.append(traversal[-2])
      backward.append(root)
    self.inorder(root.right, traversal, backward)
