class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedDict = {}
        groupAnagram = []
        elemCount = 0

        for elem in strs:
            sortElemList = sorted(elem)
            sortElem = "".join(sortElemList)
            if sortElem in sortedDict.keys():
                index = sortedDict[sortElem]
                groupAnagram[index].append(elem)

            else:
                # doesn't exist
                sortedDict[sortElem] = elemCount
                nestedList = []
                nestedList.append(elem)
                groupAnagram.append(nestedList)
                elemCount += 1

        return groupAnagram
