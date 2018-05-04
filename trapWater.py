# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

class Solution(object):
  def trapWater(self, A):
    """
    input: int[] A
    return: int
    """
    # write your solution here
    # approach: count the top two tower; recursively look for traps at the rest
    # time complexity: within each reversion, finding two max value is O(n), add result is O(n), so overall time complexity is O(n^2)
    # use list.sort for convenience
    
    if len(A) < 3:
      return 0

    Acopy = list(A)
    table = []
    for i in range(0, len(Acopy)):
      table.append((Acopy[i], i))
    table.sort(reverse = True)
    
    # if adjacent, remove the tallest
    if abs(table[0][1] - table[1][1]) == 1:
      Acopy.remove(table[0][0])
      return self.trapWater(Acopy)
    else:
      return self.getVolumn(Acopy, table[0][1], table[1][1]) + self.trapWater(Acopy)

   
  def getVolumn(self, A, left, right):
    top = min(A[left], A[right])
    if left > right:
      left, right = right, left
    result = 0
    # add trapped water to result, and remove it from the list.
    for i in range(left + 1, right):
      result += top - A.pop(left + 1)
    return result
