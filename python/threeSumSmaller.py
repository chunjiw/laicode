
# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# For example, given nums = [-2, 0, 1, 3], and target = 2.

# Return 2. Because there are two triplets which sums are less than 2:

# [-2, 0, 1]
# [-2, 0, 3]

class Solution(object):
  def threeSumSmaller(self, num, target):
    """
    input: int[] num, int target
    return: int
    """
    # write your solution here
    if len(num) < 3:
      return 0
    result = 0
    for i in range(0, len(num) - 2):
      for j in range(i + 1, len(num) - 1):
        for k in range(j + 1, len(num)):
          if num[i] + num[j] + num[k] < target:
            result += 1
    return result
