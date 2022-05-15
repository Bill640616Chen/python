#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("--------------------------sqrt()傳回平方根的值")
#https://www.w3schools.com/python/ref_math_sqrt.asp
#Python math.sqrt() Method sqrt()的方法
#Returns the square root of a number
#傳回平方根的值
#Find the square root of different numbers:
#求不同數的平方根：
# Import math Library
import math
# Return the square root of different numbers
print (math.sqrt(9))
print (math.sqrt(25))
print (math.sqrt(16))
#Definition and Usage 定義和使用
#The math.sqrt() method returns the square root of a number.
#math.sqrt()方法返回數位的平方根。
#Note: The number must be greater than or equal to 0.
#注意：該數字必須大於或等於0。
#Syntax
#math.sqrt(x)
#Parameter Values
#Parameter：Description
#x：Required. A number to find the square root of. If the number is less than 0, it returns a ValueError. If the value is not a number, it returns a TypeError
#Technical Details
#x：必需的參數， 找到一個數位的平方根。如果數位小於0，則返回ValueError。
#如果該值不是數字，則返回TypeError
#Return Value:	A float value, representing the square root of a number
#Python Version:	1.4