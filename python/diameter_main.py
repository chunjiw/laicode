from tree import TreeNode, construct_tree
import diameter

if __name__ == "__main__":
  root = construct_tree([1, 2, 6, 3, 4, '#', '#', 7, 8, 5, '#', '#', '#', 9, '#', 10])
  root2 = TreeNode(1)
  root.traverse_pre_order()
  root.traverse_breath_first()

  sol = diameter.Solution()
  print sol.getHeight(root)
  print sol.getDiameter(root.left.left)
  print sol.diameter(root2)
