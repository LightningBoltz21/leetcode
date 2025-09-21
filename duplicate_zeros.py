class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        # count the amount of zeroes in the array
        
        num_zeroes = 0
        
        for num in arr:
            if num == 0:
                num_zeroes += 1
        
        i = arr.length() - 1 + num_zeroes
        while i <= 0:
            index = arr.length() - 1 + num_zeroes
            if arr[i] != 0:
                arr[index] = arr[i]
                i -= 1
            
        
        


# create an instance of solution before calling
solution = Solution()
solution.duplicateZeros([1,0,2,3,0,4,5,0])


