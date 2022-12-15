class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        maxCount = 0

        for i in sentences:
            words = i.split(" ")
            if(len(words) > maxCount):
                maxCount = len(words)

        return maxCount