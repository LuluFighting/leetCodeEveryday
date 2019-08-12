class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToAlpha = {'2':'abc',
                       '3':'def',
                       '4':'ghi',
                       '5':'jkl',
                       '6':'mno',
                       '7':'pqrs',
                       '8':'tuv',
                       '9':'wxyz'}
        ret=[]
        if not digits:
            return ret
        def combination(start,letter=[]):
            if start == len(digits):
                ret.append(''.join(letter))
                return
            alpha = digitToAlpha[digits[start]]
            for i in range(len(alpha)):
                letter.append(alpha[i])
                combination(start+1,letter[:])
                letter.pop()
        combination(0)
        return ret