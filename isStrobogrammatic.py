# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to determine if a number is strobogrammatic. The number is represented as a string.

# For example, the numbers "69", "88", and "818" are all strobogrammatic.

class Solution(object):
  def isStrobogrammatic(self, num):
    """
    input: string num
    return: boolean
    """
    # write your solution here
    # approach: linear scan
    stro = ["0", "1", "8"]
    if not num:
      return True
    for i in range(0, len(num) / 2):
      if num[i] in stro:
        if num[i] == num[-i - 1]:
          continue
      if num[i] == "6" and num[-i-1] == "9":
        continue
      if num[i] == "9" and num[-i-1] == "6":
        continue
      return False
    if (len(num) % 2) == 1:
      return num[len(num)/2] in stro
    else:
      return True
      

       
