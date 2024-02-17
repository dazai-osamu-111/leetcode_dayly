class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        count = 1
        maxLength = 0
        n = len(s)
        charSet = set()
        for i in range(n):
            charSet.add(s[i])
            for j in range(i+1, n):
                if s[j] not in charSet:
                    charSet.add(s[j])
                else:
                    break
            count = len(charSet)
            charSet = set()
            if count > maxLength:
                maxLength = count
            
        return maxLength

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("bbbbb"))