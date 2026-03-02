"""
Problem: 704. Binary Search
Difficulty: Easy
URL: https://leetcode.com/problems/binary-search/

My Approach:
Split the indexes in two (not the list itself), compare the middle element with the target, if they are equal we return the index of the middle element, we make the while loop left <= right (<= because we want to take into account an array with only 1 element), I return -1 (no element is equal to target inside the list).

Complexity Analysis:
- Time Complexity: O(log n) -> Because we devide the search area in half each time we go through the list
- Space Complexity: O(1) -> We only use a constant amount of extra space for pointers.
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif len(nums) == 1 and ([nums[0] != target]):
                return -1
            elif target < nums[mid]:
                right = mid - 1
            elif target >= nums[mid]:
                left = mid + 1
        return -1

if __name__ == "__main__":
    solver = Solution()

    # Test 1: Element exists
    result1 = solver.search([-1,0,3,5,9,12], 9)
    print(f"Test 1: {result1} | Expected: 4")

    # Test 2: Element doesn't exist
    result2 = solver.search([-1,0,3,5,9,12], 2)
    print(f"Test 2: {result2} | Expected: -1")

