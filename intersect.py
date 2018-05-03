# Given two arrays, write a function to compute their intersection.

# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

# Note:

# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.

class Solution(object):
  def intersect(self, nums1, nums2):
    """
    input: int[] nums1, int[] nums2
    return: int[]
    """
    # write your solution here
    import collections
    table1 = collections.Counter(nums1)
    table2 = collections.Counter(nums2)
    table = collections.Counter()
    for num in table1:
      table[num] = min(table1[num], table2[num])
    return list(table.elements())
