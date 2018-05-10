# Given a string, determine if it is a palindrome, considering only alphanumeric characters('0'-'9','a'-'z','A'-'Z') and ignoring cases.

# For example,
# "an apple, :) elp pana#" is a palindrome.

# "dia monds dn dia" is not a palindrome.

class Solution(object):
  def valid(self, input):
    """
    input: string input
    return: boolean
    """
    # write your solution here
    if not input:
      return True
    input = list(input)
    # remove other charactors
    # [0, i] is the result
    # [0, j] is already examined
    i, j = 0, 0
    while j < len(input):
      if input[j].isalpha():
        input[i] = input[j].lower()
        i += 1
        j += 1
      elif input[j].isdigit():
        input[i] = input[j]
        i += 1
        j += 1
      else:
        j += 1
    return self.isPalindrome(input[0:i])
  
  def isPalindrome(self, input):
    if len(input) < 2:
      return True
    i, j = 0, len(input) - 1
    while i < j:
      if input[i] != input[j]:
        return False
      i += 1
      j -= 1
    return True
