class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #given that length of nums is 2n 
        shuffleList = []

        for i in range(len(nums)):
            if i % 2 == 0:
                #even 
                shuffleList.append(nums[(i//2)])
            else :
                shuffleList.append(nums[n + (i//2)])

        return shuffleList