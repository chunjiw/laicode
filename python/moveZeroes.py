# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution(object):
  def moveZeroes(self, nums):
    """
    input: int[] nums
    return: int[]
    """
    # write your solution here
    # approach: 1) count how many zeros (nz)
    # 2) move all non-zeros to the front, move len(nums) - nz times, one by one.
    # time complexity: n
    # space complexity: in place
    nz = 0
    for i in range(0, len(nums)):
      if nums[i] == 0:
        nz += 1
    if nz == 0:
      return nums
    # move non-zeros
    line = 0
    for i in range(0, len(nums)):
      if nums[i] != 0:
        nums[line] = nums[i]
        line += 1
    for i in range(len(nums) - nz, len(nums)):
      nums[i] = 0
    return nums
