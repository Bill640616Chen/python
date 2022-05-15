#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-----------------------------fabs()傳回絕對值(正數)")
#https://www.w3schools.com/python/ref_math_fabs.asp
#Python math.fabs() Method fabs()的方法
#Returns the absolute value of a number
#傳回絕對值(正數)
#Return absolute value:
#Import math Library
import math
#Print absolute values from numbers
print(math.fabs(-66.43))
print(math.fabs(-7))
#Definition and Usage 定義和使用
#The math.fabs() method returns the absolute value of a number, as a float.
#Absolute denotes a non-negative number. This removes the negative sign of the value if it has any.
#Unlike Python abs(), this method always converts the value to a float value.
#Syntax
#math.fabs(x)
#Parameter Values
#Parameter	Description
#x	Required. A number. If we try anything else except a number, it returns a TypeError
#Technical Details
#Return Value:	A float value, representing the absolute value of x
#Python Version:	2.6