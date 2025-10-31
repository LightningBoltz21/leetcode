class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Valid Anagram
        
        Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
        
        An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
        
        Time complexity: O(n + m)
        Space complexity: O(1)
        """
        letter_counts = [0] * 26
        base = ord ('a')
        for letter in s:
            letter_counts [ord(letter) - base] += 1
        for letter in t:
            letter_counts [ord(letter) - base] -= 1
        
        for count in letter_counts:
            if count != 0:
                return False

        return True
        
solution = Solution()

# Test cases
print(solution.isAnagram("anagram", "nagaram"))  # True
print(solution.isAnagram("rat", "car"))  # False
print(solution.isAnagram("listen", "silent"))  # True
print(solution.isAnagram("hello", "world"))  # False
print(solution.isAnagram("", ""))  # True
print(solution.isAnagram("a", "ab"))  # False