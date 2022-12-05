class Solution:
    def minimumSum(self, num: int) -> int:
        ints = [int(n) for n in str(num)]
        sortInts = ints.sort()
        """no as the list is sorted the minimum sum would be 10*(list[0] + list[1]) + 
        (list[2] + list[3])"""

        minSum = (10*(int(sortInts[0]) + int(sortInts[1])) + (int(sortInts[2]) + int(sortInts[3])))

        return minSum
