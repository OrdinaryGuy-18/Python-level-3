class Solution:
    import math
    
    def judgeSquareSum(self, c: int) -> bool:
        num1=0
        num2=int(math.sqrt(c))

        while num1<=num2:
            pro=(num1*num1)+(num2*num2)
            if pro==c:
                return True
            elif pro<c:
                num1+=1
            else:
                num2-=1

        return False
