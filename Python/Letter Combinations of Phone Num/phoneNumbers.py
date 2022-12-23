class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            #empty input 
            return []

        numMap = {}
        numMap['2'] = 'abc'
        numMap['3'] = 'def'
        numMap['4'] = 'ghi'
        numMap['5'] = 'jkl'
        numMap['6'] = 'mno'
        numMap['7'] = 'pqrs'
        numMap['8'] = 'tuv'
        numMap['9'] = 'wxyz'
        
        def phoneBFS(index:int, path:List[str]):
            if len(path) == len(digits):
                #the path is as long as the input 
                #so we have to append the path to the main combinatiuons list and return 
                combinations.append("".join(path))
                return 
            #getting the letters from the dictionary 
            letters = numMap[digits[index]]

            for letter in letters:
                #appending path with possible letter
                path.append(letter)

                #getting the next letter 
                phoneBFS(index + 1, path)

                #removing the last letter of path to backtrack
                path.pop()

        
        combinations = []

        #calling recursive function 
        phoneBFS(0, [])

        return combinations