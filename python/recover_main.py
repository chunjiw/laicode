import recover
import tree

if __name__ == "__main__":
  sol = recover.Solution()
  root = tree.construct_tree([4,2,6,1,5,3,7])
  root.traverse_breath_first()
  sol.recover(root)
  root.traverse_breath_first()

