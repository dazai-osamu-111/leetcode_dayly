# 8. String to Integer (atoi)
class Solution:
    def myAtoi(self, s:str)->int:
        res = 0
        i = 0
        found = 0
        sign = 1
        for i in range(len(s)):
            if s[i].isdigit():
                found = 1
                res = res*10 + int(s[i])
                
            elif s[i] == '+' and found == 0:
                sign = 1
                found = 1
            elif s[i] == '-' and found == 0:
                sign = 0
                found = 1
            elif s[i] == ' ' and found == 0:
                continue
            else:
                break
        if sign == 1:
            pass
        else:
            res = -res 
        if res < -2**31:
            res = -2**31
        if res > 2**31-1:
            res = 2**31-1
        return res

if __name__=='__main__':
    solution = Solution()
    print(solution.myAtoi("00000-42a1234"))