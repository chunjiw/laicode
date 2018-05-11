from tree import TreeNode, construct_tree
import reconstruct

if __name__ == "__main__":


  sol = reconstruct.Solution()
  root = sol.reconstruct([1, 3, 4, 5, 8, 11], [5, 3, 1, 4, 8, 11])
  root.traverse_breath_first()
