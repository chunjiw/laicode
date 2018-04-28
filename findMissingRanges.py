# Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

class Solution(object):
  def findMissingRanges(self, num, lower, upper):
    """
    input: int[] num, int lower, int upper
    return: List<String>
    """
    # write your solution here
    # approach: get the interval from neighboring elements in num
    # approach: attach lower - 1 and upper + 1 to num to make all intervals consistent 
    result = []
    while num and num[0] < lower:
      num.pop(0)
    while num and num[len(num) - 1] > upper:
      num.pop()
    num.insert(0, lower - 1)
    num.append(upper + 1)
    for i in range(0, len(num) - 1):
      if num[i + 1] - num[i] == 1:
        continue
      elif num[i + 1] - num[i] == 2:
        result.append(str(num[i] + 1))
      elif num[i + 1] - num[i] > 2:
        result.append(str(num[i] + 1) + "->" + str(num[i + 1] - 1))
    return result