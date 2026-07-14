class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ## HASH SET

        numSet = set(nums)          #initiate set

        res = 0
        streak = 0                  # initiate res (max consecutive) and streak (current max consecutive)

        for num in numSet:                      # loop to visit every number
            if (num - 1) not in numSet:         # and check if num - 1 exists
                streak = 1                      # if it does, current max becomes 1
                while num+streak in numSet:     # now if num+max is in the set
                    streak+=1                   # increment the streak until consecutive num+max exists
                res = max(res, streak)          # update res
        return res
            