from tree import TreeNode, construct_tree
import verticalOrder

if __name__ == "__main__":
  root = construct_tree([3,9,8,4,0,1,7,'#','#','#',2,5])
  root.traverse_breath_first()

  sol = verticalOrder.Solution()
  print sol.verticalOrder(root)
