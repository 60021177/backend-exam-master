"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""

import ast

class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        try:
            numbers = list(ast.literal_eval(numbers))
            if numbers == []:
                return "list can not blank"
            
            return max(numbers)
        except ValueError:
            return 'list format is incorrect : "'+str(numbers)+'"'
        except SyntaxError:
            return "number syntax is incorrect"

solution = Solution()
while True:
    numbers = input("\ninput = ")
    output = solution.find_max_index(numbers)
    print("Output = ",output)