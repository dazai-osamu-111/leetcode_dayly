# 7. Reverse Integer
class Solution:
    def reverse(self, x:int) -> int:
        result = 0
        sign = 1
        if x < 0:
            x *= -1
            sign = -1
        while x > 0:
            # divide x by 10
            quotitent = x//10
            remainder = x%10
            result = result*10 + remainder
            x = quotitent
        if not (-2**31 <= result <= 2**31 - 1):        
            return 0
        if sign == 1:
            return result
        else:
            return -result
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(12345))