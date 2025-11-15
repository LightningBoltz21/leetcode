from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Top K Frequent Elements
        
        Given an integer array nums and an integer k, return the k most frequent elements within the array.
        
        The test cases are generated such that the answer is always unique.
        
        You may return the output in any order.
        
        Time complexity: O(n log k)
        Space complexity: O(n)
        """
        
        
solution = Solution()

# Test cases
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
print(solution.topKFrequent([1], 1))  # [1]
print(solution.topKFrequent([1, 2], 2))  # [1, 2]
