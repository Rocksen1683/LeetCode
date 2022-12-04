class Solution:
    def isValid(self, s: str) -> bool:
        brackMap = {"(":0,")":0}
        curlMap = {"{":0,"}":0}
        boxMap = {"[":0, "]":0}
        trueCount = True

        for i in range(len(s)):
            if s[i] in brackMap.keys():
                brackMap[s[i]] += 1
            elif s[i] in curlMap.keys():
                curlMap[s[i]] += 1
            elif s[i] in boxMap.keys():
                boxMap[s[i]] += 1
        print(brackMap)
        print(curlMap)
        print(boxMap)
    
        if brackMap["("] == brackMap[")"] and curlMap["{"] == curlMap["}"] and boxMap["["] == boxMap["]"]:
            return True
        else:
            return False
