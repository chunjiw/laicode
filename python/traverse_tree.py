# This module implements three methods to traverse a binary tree.

class Solution(object):
  def traverse_pre_order(self, root):
    self.traverse_pre_order_inline(root)
    print

  def traverse_pre_order_inline(self, root):
    if not root:
      return
    print root.val,
    self.traverse_pre_order_inline(root.left)
    self.traverse_pre_order_inline(root.right)


