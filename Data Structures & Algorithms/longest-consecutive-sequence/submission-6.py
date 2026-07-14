class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## SORTING

        if not nums: return 0

        nums.sort()     # sort the array

        i = 0
        streak = 0
        res = 0
        curr = nums[0]  #initiate variables
        while i < len(nums):
            if curr != nums[i]:     # if the previously set curr is not equal to the number at i
                curr = nums[i]      # reset curr as the number at i
                streak = 0          # reset the streak to 0
            while curr in nums:
                curr+=1
                streak+=1
                res = max(streak, res)
            i+=1
        return res