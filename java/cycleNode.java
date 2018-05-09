// Check if a given linked list has a cycle. Return the node where the cycle starts. Return null if there is no cycle.

/**
 * class ListNode {
 *   public int value;
 *   public ListNode next;
 *   public ListNode(int value) {
 *     this.value = value;
 *     next = null;
 *   }
 * }
 */

public class Solution {
  public ListNode cycleNode(ListNode head) {
    // write your solution here
    HashSet<ListNode> set = new HashSet<ListNode>();
    while (head != null) {
      if (set.contains(head)) {
        return head;
      } else {
        set.add(head);
      }
      head = head.next;
    }
    return null;
  }
}
