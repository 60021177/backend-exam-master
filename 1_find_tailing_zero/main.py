"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""

class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        count = 0
        try:
            number = int(number)
            
            if number < 0:
                return "number can not be negative"
            
            result = 1
            for i in range(1, number + 1):
                result *= i
            
            for s in reversed(str(result)):
                if s == '0':
                    count += 1
                else:
                    break
            return count
        except ValueError:
            return 'number format is incorrect : "'+str(number)+'"' # if number is float or string
        except SyntaxError:
            return "number syntax is incorrect"
            
solution = Solution()

while True:
    number = input("\ninput = ")
    output = solution.find_tailing_zeroes(number)
    print("Output = ",output)

        
        
        
        
