# 12. Integer to Roman
class Solution: 
    def inToRoman(self, num: int) -> str:
        inToRomanConstant = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",            
            5: "V",        
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",    
            10 : "X", 20: "XX", 30: "XXX", 40: "XL",          
            50 : "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",            
            100: "C", 200: "CC", 300: "CCC", 400: "CD",              
            500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",           
            1000: "M", 2000: "MM", 3000: "MMM"                 
        }
        result = ""
        init_arr = []
        while num > 0:
            thuong = num//10
            du = num %10
            num = thuong
            init_arr.append(du)
        n = len(init_arr)
        for i in range(len(init_arr) - 1, -1, -1):
            key = init_arr[i]*(10**i)
            if key in inToRomanConstant:
                result = result + inToRomanConstant[key]
            # print(init_arr[i])
        return result
if __name__ == '__main__':
    solution = Solution()
    print(solution.inToRoman(3999))