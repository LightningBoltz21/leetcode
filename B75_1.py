from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # takes in list of integers called nums
        # returns true if contains duplicates
        # returns false if doesnt

        # create set of all checked nums
        checked = set()

        for num in nums: 
            if num in checked:
                return True
            else: 
                checked.add(num) 
        
        return False
    
solution = Solution()
print (solution.hasDuplicate({1,1,1,2,4}))

