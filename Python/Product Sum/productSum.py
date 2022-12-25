class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nStr = str(n)
        product = 1
        sum = 0
        for char in nStr:
            product *= int(char)
            sum += int(char)

        return product - sum