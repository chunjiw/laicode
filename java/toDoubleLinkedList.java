// Given a binary tree, convert it to a doubly linked list in place (use the left pointer as previous, use the right pointer as next).

// The values in the nodes of the doubly linked list should follow the in-order traversal sequence of the binary tree.

// Examples:

//     10

//    /  \

//   5    15

//  /

// 2

// Output:  2 <-> 5 <-> 10 <-> 15


// public class TreeNode {
//   public int key;
//   public TreeNode left;
//   public TreeNode right;
//   public TreeNode(int key) {
//     this.key = key;
//   }
// }

public class Solution {
  public TreeNode toDoubleLinkedList(TreeNode root) {
    // Write your solution here.
   TreeNode fakehead = TreeNode(0);
    traverse(root, fakehead);
    TreeNode head = fakehead.right;
    head.left = null;
    return head;
  }

  private void traverse(TreeNode root, TreeNode tail) {
  	if (root == null) {
  		return;
  	}  	
  	traverse(root.left, tail);
  	// keep the left and right subtree
  	TreeNode right = root.right;
  	tail.right = root;
  	root.left = tail;
    tail = root;
  	traverse(right, tail);
  }
}
