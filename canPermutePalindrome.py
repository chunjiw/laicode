# Given a string, determine if a permutation of the string could form a palindrome.

# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.

class Solution(object):
  def canPermutePalindrome(self, s):
    """
    input: string s
    return: boolean
    """
    # write your solution here
    import collections
    bag = collections.Counter(s)
    flag = False
    for letter in bag:
      if bag[letter] % 2:
        if flag:
          return False
        flag = True
    return True
        
