from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Two Sum
        
        Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
        
        You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
        
        Return the answer with the smaller index first.
        
        Time complexity: O(n)
        Space complexity: O(n)
        """
        
        # loop through nums for each val
        # have separate hash map (dictionary in this case) with val and index
        # search hash map for (target - val)
        # if there, return index of val and index of val in dict
        
        num_dict = {}
        out = []
        for i in range (len(nums)):
            if (target - nums[i]) in num_dict:
                out.append(num_dict[target - nums[i]])
                out.append(i)
                return out
            else: 
                num_dict[nums[i]] = i # add (nums[i], i)
        
        
solution = Solution()

# Test cases
print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(solution.twoSum([3, 2, 4], 6))  # [1, 2]
print(solution.twoSum([3, 3], 6))  # [0, 1]
