#5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s:str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right +=1
            result = s[left+1:right]
            return result
        if len(s) < 2 or s == s[::-1]:
            return s
        
        res = ""
        for i in range(len(s)):
            # with even length palindrome
            evenPalindrome = expand(i,i)
            if len(evenPalindrome) > len(res):
                res = evenPalindrome
            # with odd length palindrome
            oddPalindrome = expand(i,i+1)
            if len(oddPalindrome) > len(res):
                res = oddPalindrome
            
        return res
    
if __name__=='__main__':
    solution = Solution()
    print(solution.longestPalindrome("babad"))