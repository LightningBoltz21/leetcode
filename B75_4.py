from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group Anagrams
        
        Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
        
        An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
        
        Time complexity: O(m * n)
        Space complexity: O(m)
        """
        
        def isAnagram (word1: str, word2: str):
            
            letter_counts = [0] * 26
            base = ord ('a')
            for letter in word1:
                letter_counts [ord (letter) - base] += 1
            for letter in word2:
                letter_counts [ord (letter) - base] -= 1
            
            for count in letter_counts:
                if count != 0: 
                    return False
                
            return True
        
        out = []
        
        for word in strs:
            added_word = False
            # check all lists to see if matching anagram list
            for word_list in out:
                if isAnagram(word, word_list[0]):
                    word_list.append(word)
                    added_word = True
                    break
                
            if not added_word:    
            # if not, create new list
                out.append([word])
            
        return out            

solution = Solution()

# Test cases
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(solution.groupAnagrams([""]))  # [[""]]
print(solution.groupAnagrams(["a"]))  # [["a"]]
