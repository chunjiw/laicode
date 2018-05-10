# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.  

# Example

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

# Output: 7 -> 0 -> 8


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    input: ListNode l1, ListNode l2
    return: ListNode
    """
    # write your solution here
    extra = 0
    fakeHead = ListNode(0)
    l3 = fakeHead
    while l1 and l2:
      l3.next = ListNode((l1.val + l2.val + extra) % 10)
      extra = (l1.val + l2.val + extra) / 10
      l1, l2, l3 = l1.next, l2.next, l3.next
    if not l1:
      l1 = l2
    while l1:
      l3.next = ListNode((l1.val + extra) % 10)
      extra = (l1.val + extra) / 10
      l1, l3 = l1.next, l3.next
    if extra:
      l3.next = ListNode(extra)
    return fakeHead.next

