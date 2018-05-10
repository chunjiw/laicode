# Given two binary strings, return their sum (also a binary string).

# Input: a = “11”

#            b = “1”

# Output: “100”

class Solution(object):
  def addBinary(self, a, b):
    """
    input: string a, string b
    return: String
    """
    # write your solution here
    # approach: 1) pad '0' to shorter string;
    # 2) add digit by digit
    # time complexity: n
    
    result = []
    if len(a) > len(b):
      a, b = b, a
    for i in range(0, len(b) - len(a)):
      a = '0' + a
    prev = 0
    for i in range(1, len(a) + 1):
      dig = prev + int(a[-i]) + int(b[-i])
      if dig < 2:
        result.append(str(dig))
        prev = 0
      else:
        result.append(str(dig % 2))
        prev = 1
    if prev:
      result.append('1')
    result.reverse()
    return ''.join(result)
