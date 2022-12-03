class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        valueMap = {}
        valueMap["I"] = 1
        valueMap["V"] = 5
        valueMap["X"] = 10
        valueMap["L"] = 50
        valueMap["C"] = 100
        valueMap["D"] = 500
        valueMap["M"] = 1000

        for i in range(len(s)-1):
            if valueMap[s[i]] < valueMap[s[i +1]]:
                num -= valueMap[s[i]]
            else:
                num += valueMap[s[i]]
        num += valueMap[s[len(s)-1]]
    
        return num
