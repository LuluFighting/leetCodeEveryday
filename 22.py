class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def generate(stack=[],res=[],level=0):
            if level==n:
                while len(stack)!=0:
                    res.append(')')
                    stack.pop()
                ret.append(''.join(res))
                return
            if len(stack)!=0:
                for i in range(2):
                    if i==0:
                        stack.append('(')
                        res.append('(')
                        generate(stack[:],res[:],level+1)
                        stack.pop()
                        res.pop()
                    else:
                        stack.pop()
                        res.append(')')
                        generate(stack[:],res[:],level)
                        res.pop()
            else:
                stack.append('(')
                res.append('(')
                generate(stack[:],res[:],level+1)
        generate()
        return ret