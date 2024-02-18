# 6. Zigzag conversion
class Solution:
    def convert(self, s:str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [[] for _ in range(numRows)]
        current_row = 0
        direction = 1 # bat dau di chuyen xuong
        
        for char in s:
            # them ki tu vao hang hien tai
            rows[current_row].append(char)
            # kiem tra va doi huong neu can
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            current_row += direction
        result = ''.join(''.join(row) for row in rows)
            
        return result
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 4))