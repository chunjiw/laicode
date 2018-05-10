# This module implements tree related classes and methods.

class TreeNode(object):

  def __init__(self, x):
    xlist = list(x)
    if len(xlist) == 1:
      self.val = x
      self.left = None
      self.right = None
    elif len(xlist) > 1:
      pass
      

  def __str__(self):
    return str(self.val)

  def traverse_breath_first(self):
    # print tree level by level
    if not self:
      return
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
    self._traverse_pre_order_inline(self)
    print

  def _traverse_pre_order_inline(self, node):
    if not node:
      return
    print node.val,
    node._traverse_pre_order_inline(node.left)
    node._traverse_pre_order_inline(node.right)