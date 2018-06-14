# Largest Number Smaller In Binary Search Tree
# Description
# In a binary search tree, find the node containing the largest number smaller than the given target number.

# If there is no such number, return INT_MIN.

# Assumptions:

# The given root is not null.
# There are no duplicate keys in the binary search tree.
# Examples

#     5

#   /    \

# 2      11

#      /    \

#     6     14

# largest number smaller than 1 is Integer.MIN_VALUE(Java) or INT_MIN(c++)

# largest number smaller than 10 is 6

# largest number smaller than 6 is 5

# How is the binary tree represented?

# We use the level order traversal sequence with a special symbol "#" denoting the null node.

# For Example:

# The sequence [1, 2, 3, #, #, 4] represents the following binary tree:

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

  def largestSmaller(self, root, target):
    """
    input: TreeNode root, int target
    return: int
    """
    # write your solution here
    result = [-2147483648]
    self.recursive(root, target, result)
    return result[0]

  def recursive(self, root, target, result):
    if not root:
      return
    if root.val >= target:
      self.recursive(root.left, target, result)
    else:
      result[0] = max(result[0], root.val)
      self.recursive(root.right, target, result)


