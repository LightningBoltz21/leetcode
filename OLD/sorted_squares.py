# this isn't correct solution, just playing around to 
# try to reach O(1) complexity

def sortedSquares_inplace(nums):
    n = len(nums)
    left, right, pos = 0, n - 1, n - 1

    while left <= right:
        lv, rv = nums[left], nums[right]
        if abs(lv) > abs(rv):
            nums[pos] = lv * lv
            left += 1
        else:
            nums[pos] = rv * rv
            right -= 1
        pos -= 1

    return nums  # nums is now the sorted squares

# Quick checks
print(sortedSquares_inplace([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
print(sortedSquares_inplace([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]