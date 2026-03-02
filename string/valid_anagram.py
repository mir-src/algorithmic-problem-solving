"""
Problem: 242. Valid Anagram
Difficulty: Easy
URL: https://leetcode.com/problems/valid-anagram/

My Approach:
(1) Use Counter to return a bool, Counter stores every unique character as a key and the number of times that character appears for that specific key as a value.
(2) Use a dictionary to add each character and the frequency and then subtract the frequency from the character inside the dictionary if the character from t is the same as the character from s.

Complexity Analysis:
- Time Complexity: O(n) -> (1) Counter has to go through every single character in the string to count them. (2) We go through every single character and store them in a dictionary.
- Space Complexity: O(1) -> Because we use only lowercase english letters inside the string, if we used any character the Space Complexity would be O(n).
"""
from collections import Counter
class Solution(object):    
    def isAnagram_counter(self, s, t):
        return Counter(s) == Counter(t)
    def isAnagram_dict(self, s, t):
        if len(s) != len(t):
            return False
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1
        return True

    
if __name__ == "__main__":
    solve = Solution()

    # Test 1: t is anagram of s:
    print("---Counter Version---")
    print(f"Test 1: {solve.isAnagram_counter("anagram","nagaram")} | Expected: True")

    print("---Dict Version---")
    print(f"Test 1: {solve.isAnagram_dict("anagram","nagaram")} | Expected: True")
    print("\n")

    # Test 2: t isn't an anagram of s:
    print("---Counter Version---")
    print(f"Test 2: {solve.isAnagram_dict("rat","car")} | Expected: False")

    print("---Dict Version---")
    print(f"Test 2: {solve.isAnagram_dict("rat","car")} | Expected: False")
