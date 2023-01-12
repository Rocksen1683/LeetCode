class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # prefix and suffix solution
        products = []

        # prefix loop
        prefix = 1
        for i in range(len(nums)):
            if i == 0:
                products.append(1)
            else:
                prefix *= nums[i-1]
                products.append(prefix)

        # suffix loop
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                continue
            else:
                suffix *= nums[i+1]
                products[i] *= suffix

        return products
