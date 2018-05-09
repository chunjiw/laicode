# Given a binary tree, return all root-to-leaf paths from left to right.

# For example, given the following binary tree:

#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:

# ["1->2->5", "1->3"]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def binaryTreePaths(self, root):
    """
    input: TreeNode root
    return: String[]
    """
    # write your solution here
    # approach: depth first search
    if not root:
      return []
    result = []
    solution = []
    self.addPath(root, result, solution)
    return result
  
  def addPath(self, root, result, solution):
    # if leaf node: append solution to result
    if not root.left and not root.right:
      solution.append(str(root.val))
      result.append(''.join(solution))
      solution.pop()
      return
    # if left or right child:
    solution.append(str(root.val) + "->")
    if root.left:
      self.addPath(root.left, result, solution)
    if root.right:
      self.addPath(root.right, result, solution)
    solution.pop()
    return
