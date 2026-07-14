class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # BRUTE FORCE
        """
        1. convert the array into a set
        2. start with 0th element and check if it exists in the set,
            if it does, increment streak and element counter
        """

        res = 0             # storing longest consecutive
        store = set(nums)   # store array in set

        for num in nums:
            streak = 0
            curr = num      # each element is checked and kept a count of its following numbers
            while curr in store:    # if curr element is found, increment streak and curr
                streak+=1                   
                curr+=1
                res = max(res, streak)  # result is updated, if the incremented curr is still found, the loop repeats
        return res