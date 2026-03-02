"""
Problem: 252. Meeting Rooms
Difficulty: Easy
URL: https://neetcode.io/problems/meeting-schedule/question?list=neetcode150

My Approach:
Sort the list of objects using .sort(key=lambda x: x.start) based on .start, then use all() to determine if all of the objects start and end where they should (.end <= .start), use zip to unpack the tuple into pairs of objects, use islice() to avoid making a shallow copy of the list.

Complexity Analysis:
- Time Complexity: O(n log n)
- Space Complexity: O(1) 
"""
from itertools import islice
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        result = all(next.start >= curr.end for curr,next in zip(intervals, islice(intervals, 1, None)))
        return result
        

if __name__ == "__main__":
    test_data1 = [(0,30),(5,10),(15,20)]
    test_data2 = [(5,8),(9,15)]

    t1_objects = [Interval(x,y) for x,y in test_data1]
    t2_objects = [Interval(x,y) for x,y in test_data2]

    solver = Solution()

    print(f"Test 1: {solver.canAttendMeetings(t1_objects)} | Expected: False")
    print(f"Test 2: {solver.canAttendMeetings(t2_objects)} | Expected: True")


