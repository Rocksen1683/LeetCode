class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in sDict.keys():
                sDict[s[i]] = sDict[s[i]] + 1
            else:
                sDict[s[i]] = 0
            if t[i] in tDict.keys():
                tDict[t[i]] = tDict[t[i]] + 1
            else:
                tDict[t[i]] = 0

        if sDict == tDict:
            return True
        else:
            return False
