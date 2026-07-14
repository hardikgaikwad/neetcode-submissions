class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ## HASH SET

        numSet = set(nums)

        res = 0
        streak = 0

        for num in numSet:
            if (num - 1) not in numSet:
                streak = 1
                while num+streak in numSet:
                    streak+=1
                res = max(res, streak)
        return res
            