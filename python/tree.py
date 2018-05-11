# This module implements tree related classes and methods.

class TreeNode(object):

  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

  def __str__(self):
    return str(self.val)

  def traverse_breath_first(self):
    # print tree level by level
    if not self:
      print "empty tree"
      return
    print "breath first traverse"
    level = [self]
    while level:
      if any(level):
        for i in range(0, len(level)):
          node = level.pop(0)
          if node:
            print node.val,
            level.append(node.left)
            level.append(node.right)
          else:
            print '#',
      else:
        break
      print

  def traverse_pre_order(self):
    # print tree nodes in pre-order
    print "pre order traverse"
    self._traverse_pre_order_inline(self)
    print

  def _traverse_pre_order_inline(self, node):
    if not node:
      return
    print node.val,
    node._traverse_pre_order_inline(node.left)
    node._traverse_pre_order_inline(node.right)


def construct_tree(x):
  # contruct root
  if not x:
    return None
  root = TreeNode(x.pop(0))
  level = [root]
  # construct the rest nodes
  while x:
    nextlevel = list()
    for parent in level:
      if parent:
        if x:
          if x[0] != '#':
            parent.left = TreeNode(x.pop(0))
            nextlevel.append(parent.left)
          else:
            parent.left = None
            x.pop(0)
        if x:
          if x[0] != '#':
            parent.right = TreeNode(x.pop(0))
            nextlevel.append(parent.right)
          else:
            parent.right = None
            x.pop(0)
    level = nextlevel
  return root