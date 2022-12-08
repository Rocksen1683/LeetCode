""" MORE EFFICIENT VERSION WITHOUT LETTING THE WHOLE DICT FORM""" 
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        numCount = {}
        for i in nums:
            if i in numCount.keys():
                return i
            else:
                numCount[i] = 1
        


""" OLD VERSION 

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
"""
