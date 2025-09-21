class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        temp = 0
        num_digits = 0
        count = 0

        for num in nums:
            temp = num
            num_digits = 0
            while temp >= 1:
                temp = temp // 10
                num_digits += 1
            if num_digits % 2 == 0:
                count += 1

        return count


# create an instance of solution before calling
solution = Solution()
solution.findNumbers([121, 66])
