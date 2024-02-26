# 15. 3Sum

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = nums
        sorted_nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            left = i-1 
            right = i + 1
            while left >= 0 and right < n:
                sum = sorted_nums[left] + sorted_nums[right] + sorted_nums[i]
                if sum == 0:
                    tmp = [sorted_nums[left], sorted_nums[right], sorted_nums[i]]
                    tmp.sort()
                    if tmp not in result:
                        result.append(tmp)
                    left -= 1
                elif sum > 0:
                    left -= 1
                elif sum < 0:
                    right += 1
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([0,0,0]))