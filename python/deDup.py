# Remove Adjacent Repeated Characters I
# Description
# Remove adjacent, repeated characters in a given string, leaving only one character for each group of such characters.

# Assumptions

# Try to do it in place.
# Examples

# "aaaabbbc" is transferred to "abc"
# Corner Cases

# If the given string is null, we do not need to do anything.


class Solution(object):
  def deDup(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    input = list(input)
    if not input:
      return ''
    i, j = 1, 1
    while i < len(input):
      if input[i] != input[j - 1]:
        input[j] = input[i]
        i += 1
        j += 1
      else:
        i += 1
    return ''.join(input[0:j])

