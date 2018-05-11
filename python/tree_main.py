from tree import TreeNode, construct_tree

if __name__ == "__main__":
  root = construct_tree([1, 2, 6, 3, 4, '#', '#', 7, 8, 5, '#', '#', '#', 9, '#', 10])
  print root
  root.traverse_pre_order()
  root.traverse_breath_first()