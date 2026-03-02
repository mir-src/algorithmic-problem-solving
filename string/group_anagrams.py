"""
Problem: 49. Group Anagrams
Difficulty: Medium
URL: https://leetcode.com/problems/group-anagrams/

My Approach:
Create a dictionary and go through every word, get the sorted form of the word and convert it into a tuple to use it as the dictionary key, if the key doesn't exist initialize a list for the key, if it already exists .append the word to the key. Return a list of lists with the values of the keys.

Complexity Analysis:
- Time Complexity: O(N*KlogK) -> We are looping through N strings, we sort the string. Sorting takes O(KlogK) time complexity, therefore the total time complexity is O(N*KlogK).
- Space Complexity: O(N*K) -> In the worst-case scenario where no words are anagrams, the dictionary will store every single word in isolation.
"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for word in strs:
            tuple_word = tuple(sorted(word))
            if tuple_word not in d:
                d[tuple_word] = [word]
            else:
                d[tuple_word].append(word)
        return list(list(d.values()))
if __name__ == "__main__":
    solve = Solution()

    print(f"Test 1: {solve.groupAnagrams(["act","pots","tops","cat","stop","hat"])}")
    print(f"Test 1: {solve.groupAnagrams([""])}")
    print(f"Test 1: {solve.groupAnagrams(["a"])}")



