class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        numCount = {}
        for i in nums:
            if i in numCount.keys():
                numCount[i] += 1
            else:
                numCount[i] = 1
        
        for key in numCount.keys():
            if numCount[key] == n:
                return key
