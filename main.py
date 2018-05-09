# This script executes implementations elsewhere in this project.

# set which implementation to execute
test = "flatten"

if test == "flatten":
  from TreeNode import TreeNode
  import traverse_tree
  import flatten

if __name__ == "__main__":

  if test == "flatten":
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    root.right.right.right = TreeNode(9)

    traverser = traverse_tree.Solution()
    traverser.traverse_pre_order(root)

    sol = flatten.Solution()
    traverser.traverse_pre_order(sol.flatten(root))