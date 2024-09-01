"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        if type(number) == int:
            if number < 0:
                return "number can not less than 0"
            lists = [
                (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),(100, 'C'), (90, 'XC'), 
                (50, 'L'), (40, 'XL'),(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
            ]
    
            result = ""
    
            for value, numeral in lists:
                while number >= value:
                    result += numeral
                    number -= value
            
            return result
        else:
            return "number type must be an integer"


solution = Solution()

while True:
    try:
        numbers = input("\ninput = ")
        output = solution.number_to_roman(int(numbers))
        print("Output = ",output)
    except ValueError:
        print(f"number format is incorrect : {numbers}")