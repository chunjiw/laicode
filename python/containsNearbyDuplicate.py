# Contains Duplicate II
# Description
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

class Solution(object):
  def containsNearbyDuplicate(self, nums, k):
    """
    input: int[] nums, int k
    return: boolean
    """
    # write your solution here
    s = set()
    for i in xrange(0, len(nums)):
      if i > k:
        s.remove(nums[i - k - 1])
      if nums[i] in s:
        return True
      else:
        s.add(nums[i])
    return False
