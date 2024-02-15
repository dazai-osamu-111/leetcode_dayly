from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = -1
        previous_element_sum = 0
        for num in nums:
            if num < previous_element_sum:
                ans = previous_element_sum + num
            previous_element_sum += num
        return ans
    
if __name__ == "__main__":
    solution = Solution()
    nums = [76, 31, 38, 15, 8, 2, 82, 55, 55, 57]
    print("da giac co chu vi lon nhat la: ", solution.largestPerimeter(nums))