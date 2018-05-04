# Given a binary tree where all the right nodes are leaf nodes, flip it upside down and turn it into a tree with left leaf nodes as the root.

# Examples

#         1

#       /    \

#     2        5

#   /   \

# 3      4

# is reversed to

#         3

#       /    \

#     2        4

#   /   \

# 1      5

# How is the binary tree represented?

# We use the pre order traversal sequence with a special symbol "#" denoting the null node.

# For Example:

# The sequence [1, 2, #, 3, 4, #, #, #] represents the following binary tree:

#     1

#   /   \

#  2     3

#       /

#     4


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def reverse(self, root):
    """
    input: TreeNode root
    return: TreeNode
    """
    # write your solution here
    if not root or not root.left:
      return root    
    newRoot = self.reverse(root.left)
    # the actural reverse action is here
    root.left.left = root
    root.left.right = root.right
    # clean up the tail
    root.left = None
    root.right = None
    # return solution
    return newRoot
