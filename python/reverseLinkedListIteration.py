# Reverse a singly-linked list.

# Examples

# L = null, return null
# L = 1 -> null, return 1 -> null
# L = 1 -> 2 -> 3 -> null, return 3 -> 2 -> 1 -> null

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def reverse(self, head):
    """
    input: ListNode head
    return: ListNode
    """
    # write your solution here
    if not head or not head.next:
      return head
    mid = head
    post = mid.next
    while post:
      pre = mid
      mid = post
      post = post.next
      mid.next = pre      
    head.next = None
    return mid


