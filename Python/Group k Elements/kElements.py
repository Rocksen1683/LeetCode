class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        intCounts = {}
        for elem in nums:
            if elem in intCounts.keys():
                intCounts[elem] += 1
            else:
                intCounts[elem] = 1
        # sorting dictionary by value
        sortedInts = sorted(intCounts.items(),
                            key=lambda x: x[1], reverse=True)

        freqElements = []

        for i in range(k):
            freqElements.append(sortedInts[i][0])

        return freqElements
