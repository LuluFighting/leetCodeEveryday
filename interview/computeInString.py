class Solution:
    def compute(self,num1,num2,op):
        if op == '*':
            num = num2 * num1
        elif op == '/':
            num = num2 / num1
        elif op == '+':
            num = num2 + num1
        else:
            num = num2 - num1
        return num
    def computeInString(self,str):
        ret,opStack,opList,numStack = 0,[],[],[]
        operation = ('+','-','*','/','(',')')
        if not str:
            return ret
        if len(str)==1:
            if str[0]>='0' and str[0]<='9':
                return int(str)
            else:
                raise ValueError("the string is not valid")
        def splitStr():
            i,j=0,0
            while j<len(str):
                if str[j] in operation:
                    if i<j :
                        opList.append(str[i:j])
                    opList.append(str[j])
                    j+=1
                    i=j
                elif str[j]  in "0123456789":
                    j+=1
                else:
                    raise ValueError("the string is not valid")
            if i!=j:
                opList.append(str[i:j])
        splitStr()
        def computeTwoNum():
            num1 = numStack[- 1]
            numStack.pop()
            num2 = numStack[-1]
            numStack.pop()
            num = self.compute(num1, num2, opStack[len(opStack) - 1])
            opStack.pop()
            numStack.append(num)
        for i in range(len(opList)):
            if opList[i] in operation:
                if opList[i]=='(' or  len(opStack)==0 or opStack[-1] == '(' or (opStack[-1] in ('+','-') and opList[i] in ('*','/')):
                    opStack.append(opList[i])
                elif opList[i]==')':
                    while len(opStack)>=1 and opStack[len(opStack)-1]!='(':
                        computeTwoNum()
                    opStack.pop()
                else:
                    computeTwoNum()
                    opStack.append(opList[i])
            else:
                numStack.append(int(opList[i]))
        while len(opStack)!=0:
            computeTwoNum()
        return numStack[0]
obj = Solution()
print(obj.computeInString("4+(6*7-4)*5"))