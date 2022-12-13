class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        indexMap = {}
        for i in range(len(s)):
            indexMap[indices[i]] = s[i]
        
        shuffle = ""

        newMap = {k: indexMap[k] for k in sorted(indexMap)}

        for key in newMap.keys():
            shuffle += newMap[key]

        return shuffle 