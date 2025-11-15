class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # uses backtracking somehow

        # create list to return
        output = []

        # create temp list to add to output list
        subset = []

        def dfs(total_sum):
            # base case
            if (total_sum == 0):
                output.append(subset.copy())
            elif (total_sum <= 0):
                return

            # add one of the indexes
            for num in nums:
                if subset and subset[-1] > num:
                    continue
                subset.append(num)
                dfs (total_sum - num)
                subset.pop()
        
        dfs(target)
        return output
