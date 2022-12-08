""" CORRECT SOLUTION """
class Solution:
    def isValid(self, s: str) -> bool:
        
        openBracks = set("({[")
        closeBracks = set("]})")
        pairMap = {')':'(','}':'{',']':'['}
        parenStack = []

        for i in s:
            if i in openBracks:
                parenStack.append(i) 
            #not an opening bracket
            if i in closeBracks:
                if not parenStack:
                    return False
                    #can't be in closing if there's no opening
                elif parenStack.pop() != pairMap[i]:
                    return False
                else:
                    continue
        if not parenStack:
            #everything is popped so it's True
            return True
        else:
            return False

""" PREVIOUS SOLUTION

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
"""
