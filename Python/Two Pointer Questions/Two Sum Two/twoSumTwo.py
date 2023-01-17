class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        lPointer = 0
        rPointer = length - 1
        indices = []

        while lPointer < rPointer:
            # update array if we find the pairs
            if numbers[lPointer] + numbers[rPointer] == target:
                indices.append(lPointer + 1)
                indices.append(rPointer + 1)
                break
            # increment left pointer by one if less than target
            elif numbers[lPointer] + numbers[rPointer] < target:
                lPointer += 1
            # decrement right pointer by one if more than target
            else:
                rPointer -= 1
        return indices
