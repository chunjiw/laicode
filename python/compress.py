# Compress String
# Description
# Given a string, replace adjacent, repeated characters with the character followed by the number of repeated occurrences. If the character does not has any adjacent, repeated occurrences, it is not changed.

# Assumptions

# The string is not null

# The characters used in the original string are guaranteed to be 'a' - 'z'

# There are no adjacent repeated characters with length > 9

# Examples

# "abbcccdeee" -> "ab2c3de3"


class Solution(object):
  def compress(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    i, j, k = 0, 0, 0
    n = len(input)
    input = list(input)
    while i < n:
      if i + 1 == n or input[i + 1] != input[i]:
        # single char just copy
        input[j] = input[i]
        i += 1
        j += 1
      else:
        # multiple char, k count
        k = 0
        while i + k < n:
          if input[i + k] == input[i]:
            k += 1
          else:
            break
        input[j] = input[i]
        input[j + 1] = str(k)
        j += 2
        i = i + k
    return ''.join(input[0:j])



