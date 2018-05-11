# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
#
# Examples:
#
# Given binary tree [3,9,20,null,null,15,7],
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7
# return its vertical order traversal as:
#
# [9,3,15,20,7]
# Given binary tree [3,9,8,4,0,1,7],
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
# return its vertical order traversal as:
#
# [4,9,3,0,1,8,7]
# Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2
# return its vertical order traversal as:
#
# [4,9,5,3,0,1,8,2,7]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def verticalOrder(self, root):
    """
    input: TreeNode root
    return: List<Integer>
    """
    # write your solution here
    # approach: the tree fits into an n * (2*n-1) grid.
    # assign each node a position in the grid, and print in order.
    n = self.getHeight(root)
    nodes_list = []
    self.traverse(root, [0], nodes_list, n)
    nodes_list.sort()
    result = list()
    for node in nodes_list:
      result.append(node[1])
    return result

  def traverse(self, root, path, nodes_list, n):
    if not root:
      return
    row = len(path)
    column = sum(path)
    index = row + column * n
    nodes_list.append((index, root.val))
    path.append(-1)
    self.traverse(root.left, path, nodes_list, n)
    path.pop()
    path.append(1)
    self.traverse(root.right, path, nodes_list, n)
    path.pop()

  def getHeight(self, root):
    if not root:
      return 0
    return 1 + max(self.getHeight(root.left), self.getHeight(root.right))