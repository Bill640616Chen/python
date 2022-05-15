#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------tanh()傳回雙曲三角函數tangent的值")
#https://www.w3schools.com/python/ref_math_tanh.asp
#Python math.tanh() Method tanh()的方法
#Returns the hyperbolic tangent of a number
#傳回雙曲三角函數tangent的值
#Find the hyperbolic tangent of different numbers:
#尋找不同數字的雙曲正切值：
# Import math Library
import math
# Return the hyperbolic tangent of different numbers
print(math.tanh(8))
print(math.tanh(1))
print(math.tanh(-6.2))
print(math.tanh(0))

#print(math.tanh(int('1'))
#EOF，為End Of File的縮寫，通常在文字的最後存在此字元表示資料結束。
#unexpected EOF while parsing
#解析時意外 Eof

#Definition and Usage 定義和使用
#The math.tanh() method returns the hyperbolic tangent of a number.
#math.tanh()方法返回數位的雙曲正切值。
#Syntax
#math.tanh(x)
#Parameter Values
#Parameter：Description
#x：Required. A number to find the hyperbolic tangent of. 
# If the value is not a number, it returns a TypeError
#必需的參數， 尋找雙曲正切的數位。如果該值不是數位，
# 則返回TypeError
#Technical Details
#Return Value:	A float value, representing the hyperbolic tangent of a number
#Python Version:	1.4