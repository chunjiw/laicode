# Given a binary tree, flatten it to a linked list in-place.

# For example,
# Given

#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:

#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import TreeNode

class Solution(object):
  def flatten(self, root):
    """
    input: TreeNode root
    return: TreeNode
    """
    # write your solution here
    # approach: in-order traverse, fake root
    fakeroot = TreeNode(0)
    self.traverse(fakeroot, root)
    return fakeroot.right

  def traverse(self, leaf, root):
    # append root as leaf's right child
    if not root:
      return leaf
    # preserve the two children
    left = root.left
    right = root.right
    # should have no left branches in the flattened tree
    root.left = None
    # append node to flattened tree
    leaf.right = root
    # do the same to left child
    leaf = self.traverse(leaf.right, left)
    # do the same to right child
    leaf = self.traverse(leaf, right)
    return leaf


