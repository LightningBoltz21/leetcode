class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:  # checks if equal to 1
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0

        return max_count


# create an instance of solution before calling
solution = Solution()
solution.findMaxConsecutiveOnes([1, 2, 1, 1, 1, 1])
