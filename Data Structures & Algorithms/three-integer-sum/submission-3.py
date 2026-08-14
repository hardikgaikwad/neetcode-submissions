class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## HashMap
        n = len(nums)
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        res = []

        for i in range(n):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                count[nums[j]] -= 1
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                target = -(nums[i] + nums[j])
                if count.get(target):
                    res.append([nums[i], nums[j], target])
            for j in range(i+1, n):
                count[nums[j]] += 1

        return res