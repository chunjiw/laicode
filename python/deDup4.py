# Remove Adjacent Repeated Characters IV
# Description
# Repeatedly remove all adjacent, repeated characters in a given string from left to right.

# No adjacent characters should be identified in the final string.

# Examples

# "abbbaaccz" -> "aaaccz" -> "ccz" -> "z"
# "aabccdc" -> "bccdc" -> "bdc"


class Solution(object):
  def deDup(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    stack = []
    dup = ''
    for c in input:
      if c == dup:
        continue
      if not stack or stack[-1] != c:
        stack.append(c)
        continue
      if stack[-1] == c:
        stack.pop()
        dup = c
    return ''.join(stack)

