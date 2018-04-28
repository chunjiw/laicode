# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.

class Solution(object):
  def canAttendMeetings(self, intervals):
    """
    input: int[][] intervals
    return: boolean
    """
    # write your solution here
    # approach: sort and compare neighbor time
    for i in range(0, len(intervals) - 1):
      for j in range(i + 1, len(intervals)):
        if intervals[i][0] > intervals[j][0]:
          intervals[i], intervals[j] = intervals[j], intervals[i]
    for i in range(0, len(intervals) - 1):
      if intervals[i][1] > intervals[i + 1][0]:
        return False
    return True
    
