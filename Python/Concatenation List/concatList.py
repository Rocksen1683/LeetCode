class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concatList = [x for x in nums]
        concatListNew = [x for x in nums]
        concatList += concatListNew

        return concatList