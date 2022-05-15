#https://kknews.cc/education/2yaaa2r.html
#整數轉羅馬數字,但是看不懂,不知道怎麼修改
#from sys import stdin
num = input()
class Solution(object): 
    def intToRoman(self, num): 
        result = "" 
        result += "M"* (num / 1000) 
        num = num % 1000 
        if num / 100 == 9: 
            result += "CM" 
            num -= 900 
        elif num / 100 >=5: 
            result += "D" 
            num -= 500 
        elif num / 100 == 4: 
            result += "CD" 
            num -= 400 
        result += "C"* (num / 100) 
        num = num % 100 
        if num / 10 == 9: 
            result += "XC" 
            num -= 90 
        elif num / 10 >=5: 
            result += "L" 
            num -= 50 
        elif num / 10 == 4: 
            result += "XL" 
            num -= 40 
        result += "X"* (num / 10) 
        num = num % 10 
        if num == 9: 
            result += "IX" 
            num -= 9 
        elif num >=5: 
            result += "V" 
            num -= 5 
        elif num == 4: 
            result += "IV" 
            num -= 4 
        X_num = num 
        result += "I"*X_num 
        return result
