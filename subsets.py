class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        output = []
        subset = []

        def dfs(index):
            # base case
            if (index >= len(nums)):
                # add the subset to the output list
                output.append(subset.copy())
                return 

            # in each recursion
            subset.append (nums[index])
            dfs(index + 1)

            subset.pop()
            dfs(index + 1)

        # call the recursive method
        dfs (0)

        # return output
        return output




