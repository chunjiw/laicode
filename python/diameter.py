# Given a binary tree in which each node contains an integer number. The diameter is defined as the longest distance from one leaf node to another leaf node. The distance is the number of nodes on the path.

# If there does not exist any such paths, return 0.

# Examples

#     5

#   /    \

# 2      11

#      /    \

#     6     14

# The diameter of this tree is 4 (2 -> 5 -> 11 -> 14)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def diameter(self, root):
    """
    input: TreeNode root
    return: int
    """
    # write your solution here
    # approach: get height of each node left and right,
    # get max diameter for each node
    # then get the max diameter of all nodes
    return self.traverse(root, 0)

  def getHeight(self, root):
    if not root:
      return 0
    return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

  def getDiameter(self, root):
    if not root or not root.left or not root.right:
      return 0
    return 1 + self.getHeight(root.left) + self.getHeight(root.right)

  def traverse(self, root, maxDiameter):
    if not root:
      return maxDiameter
    maxDiameter = max(maxDiameter, self.getDiameter(root))
    maxDiameter = self.traverse(root.left, maxDiameter)
    maxDiameter = self.traverse(root.right, maxDiameter)
    return maxDiameter

