#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("--------------------sinh()傳回雙曲三角函數sinh的值")
#https://www.w3schools.com/python/ref_math_sinh.asp
#Python math.sinh() Method sinh()的方法
#Returns the hyperbolic sine of a number
#傳回雙曲三角函數sinh的值
#Find the hyperbolic sine of different numbers:
#尋找不同數字的雙曲正弦值：
# Import math Library
import math
# Return the hyperbolic sine of different values
print(math.sinh(0.00))
print(math.sinh(-23.45))
print(math.sinh(23))
print(math.sinh(1.00))
print(math.sinh(math.pi))
#Definition and Usage 定義和使用
#The math.sinh() method returns the hyperbolic sine of a 
# number.
#math.sinh()方法返回數位的雙曲正弦值。
#Syntax
#math.sinh(x)
#Parameter Values
#Parameter：Description
#x：Required. A number to find the hyperbolic sine of. 
# If the value is not a number, it returns a TypeError
#必需的參數， 尋找雙曲正弦的數字。如果該值不是數字
# ，則返回TypeError
#Technical Details
#Return Value:	A float value, representing the hyperbolic 
# sine of a number
#Python Version:	1.4