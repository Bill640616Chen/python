#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-----------------------------fmod()傳回ｘ／ｙ的餘數")
#https://www.w3schools.com/python/ref_math_fmod.asp
#Python math.fmod() Method fmod()的方法
#Returns the remainder of x/y
#傳回ｘ／ｙ的餘數
#Return the remainder of x/y:
# Import math Library
import math
# Return the remainder of x/y
print(math.fmod(20, 4))
print(math.fmod(20, 3))
print(math.fmod(15, 6))
print(math.fmod(-10, 3))
#print(math.fmod(0, 0)) y是除數不能為0
#Definition and Usage 定義和使用
#The math.fmod() method returns the remainder (modulo) of x/y.
#Syntax
#math.fmod(x, y)
#Parameter Values
#Parameter：Description
#x：Required. A positive or negative number to divide
#y：Required. A positive or negative number to divide x with
#Note: If both x and y = 0, it returns a ValueError.
#Note: If y = 0, it returns a ValueError.
#Note: If x or y is not a number, it returns a TypeError.
#Technical Details
#Return Value:	A float value, representing the remainder of x/y
#Python Version:	1.4