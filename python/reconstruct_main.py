from tree import TreeNode, construct_tree
import reconstruct

if __name__ == "__main__":

  sol = reconstruct.Solution()

  root = sol.reconstruct([1, 3, 4, 5, 8, 11], [5, 3, 1, 4, 8, 11])
  root.traverse_breath_first()

  root = sol.reconstruct([1, 6, 5, 7, 4, 10, 9], [4, 1, 5, 6, 7, 10, 9])
  root.traverse_breath_first()

  root = sol.reconstruct([1,2,10, 9], [2,1,10, 9])
  root.traverse_breath_first()

