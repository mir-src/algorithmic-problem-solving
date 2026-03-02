"""
Problem: 1. Two Sum
Difficulty: Easy
URL: https://leetcode.com/problems/two-sum/

My Approach:
We use a dictionary to remember each number from the list, we calculate the difference between the current number and the target, it's "complement = target - nums[i]" because if we have target = 0 and we have nums[i] = 3, we need to find the number -3.

Complexity Analysis:
- Time Complexity: O(n) -> Because we go through the list only once from the first element until the last element.
- Space Complexity: O(n) -> Declared 1 dictionary of size n.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for i in range(0,len(nums)):
            complement = target - nums[i]
            if complement in dictionary:
                return [dictionary[complement], i]
            dictionary[nums[i]] = i
        return []


if __name__ == "__main__":
    solve = Solution()

    print(f"Test 1: {solve.twoSum([2,7,11,15], 9)}")
    print(f"Test 2: {solve.twoSum([3,2,4], 6)}")
    print(f"Test 3: {solve.twoSum([3,3], 6)}")


