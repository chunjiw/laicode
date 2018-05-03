# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.


# Example 1:

# Input: "aba"
# Output: True
# Example 2:

# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

class Solution(object):
  def validPalindrome(self, s):
    """
    input: string s
    return: boolean
    """
    # write your solution here
    slist = list(s)
    if self.isPalindrome(slist):
      return True
    else:
      for i in range(0, len(slist)):
        copy = list(slist)
        copy.pop(i)
        if self.isPalindrome(copy):
          return True
    return False

  def isPalindrome(self, slist):
    if len(slist) < 2:
      return True
    i, j = 0, len(slist) - 1
    while i < j:
      if slist[i] != slist[j]:
        return False
      i += 1
      j -= 1
    return True
