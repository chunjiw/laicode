# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.

class Solution(object):
  def minSubArrayLen(self, s, nums):
    """
    input: int s, int[] nums
    return: int
    """
    # write your solution here
    result = len(nums) + 1
    for i in range(0, len(nums)):
      j = i + 1
      while j < len(nums) and sum(nums[i:j]) < s:
        j += 1
      if sum(nums[i:j]) >= s:
        result = min(result, j - i)
    if result == len(nums) + 1:
      return 0
    return result
      
