# Given the preorder and inorder traversal sequence of a binary tree, reconstruct the original tree.
#
# Assumptions
#
# The given sequences are not null and they have the same length
# There are no duplicate keys in the binary tree
# Examples
#
# preorder traversal = {5, 3, 1, 4, 8, 11}
#
# inorder traversal = {1, 3, 4, 5, 8, 11}
#
# the corresponding binary tree is
#
#         5
#
#       /    \
#
#     3        8
#
#   /   \        \
#
# 1      4        11
#
# How is the binary tree represented?
#
# We use the pre order traversal sequence with a special symbol "#" denoting the null node.
#
# For Example:
#
# The sequence [1, 2, #, 3, 4, #, #, #] represents the following binary tree:
#
#     1
#
#   /   \
#
#  2     3
#
#       /
#
#     4

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from tree import TreeNode

class Solution(object):
  def reconstruct(self, inn, pre):
    """
    input: int[] in, int[] pre
    return: TreeNode
    """
    # write your solution here
    # approach
    # pre[0] is root,
    # pre[0] divides in into left and right part, which are root's left and right tree
    # recursively reconstruct root - left tree - right tree
    if not pre:
      return None
    root = TreeNode(pre[0])
    if len(pre) > 1:
      root_index_in_in = inn.index(pre[0])
      in_left = inn[0 : root_index_in_in]
      in_right = inn[(root_index_in_in + 1) :]
      pre_left = pre[1 : (len(in_left) + 1)]
      pre_right = pre[(len(in_left) + 1) : ]
      root.left = self.reconstruct(in_left, pre_left)
      root.right = self.reconstruct(in_right, pre_right)
    return root


