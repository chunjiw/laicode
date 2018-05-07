# Given a linked list, remove the nth node from the end of list and return its head.

# Assumptions
# If n is not valid, you do not need to do anything to the original list.
# Try to do this in one pass.

# Examples

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def removeNthFromEnd(self, head, n):
    """
    input: ListNode head, int n
    return: ListNode
    """
    # write your solution here
    # approach: queue of length n + 1
    if not head or n <= 0:
      return head
    queue = list()
    node = head
    while node:
      queue.append(node)
      if len(queue) == n + 2:
        queue.pop(0)
      node = node.next
    
    if len(queue) < n:
      return queue[0]
    if len(queue) == n:
      return queue[0].next
    if len(queue) == 2:
      queue[0].next = None
      return head
    # if len(queue) >= n + 1
    queue[0].next = queue[2]
    return head  

