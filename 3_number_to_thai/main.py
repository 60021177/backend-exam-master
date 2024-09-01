"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        units = {"1" :"หนึ่ง", "2" :"สอง", "3" :"สาม", "4" :"สี่", "5" :"ห้า", "6" :"หก", "7" :"เจ็ด", "8" :"แปด", "9":"เก้า", "0":""} 
        tens = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน", "สิบล้าน"]
        text = []
        
        if type(number) == int:
            
            if number < 0:
                return "number can not less than 0"
            
            if number > 10000000:
                return "number out of limit 1 - 10,000,000"
            words = list(reversed(str(number)))

            for i in range(len(words)):
                text.append(tens[i])
                text.append(units[words[i]])

            if len(text) > 2 :
                if text[1] == "หนึ่ง":
                    text[1] = "เอ็ด"
                if text[3] == "สอง":
                    text[3] = "ยี่"
                if text[3] == "หนึ่ง" and len(text) < 5:
                    text[3] = ''
            elif len(text) == 2:
                if text[1] == '':
                    text[1] = "ศูนย์"
            
            len_text = len(text)

            if text[len_text-2] != '' and text[len_text-1] != '' and len_text > 4:
                for i in range(2,len_text-2):
                    if text[i+1] == '':
                        text[i] = ''

            if len(text) > 14:
                if text[15] == "หนึ่ง":
                    text[15] = ''
            elif len(text) > 5:
                if text[3] == "หนึ่ง":
                    text[3] = ''
                    
            text.reverse()
            return "".join(text)
        else:
            return "number type must be an integer"
    
solution = Solution()
while True:
    try:
        numbers = input("\ninput = ")
        output = solution.number_to_thai(int(numbers.replace(',', '')))
        print("Output = ",output)
    except ValueError:
        print(f"number format is incorrect (must be an integer): {numbers}")
        

