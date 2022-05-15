#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------cosh()返回x的弧度的餘弦值)")
#https://www.w3schools.com/python/ref_math_cosh.asp
#Python math.cosh() Method cosh()的方法
#Returns the hyperbolic cosine of a number
#傳回cosh()的弧度的餘弦值
#FFind the hyperbolic cosine of different numbers:
# Import math Library
import math
# Return the hyperbolic cosine of different numbers
print (math.cosh(1))
print (math.cosh(8.90))
print (math.cosh(0))
print (math.cosh(1.52))
#Definition and Usage 定義和使用
#The math.cosh() method returns the hyperbolic cosine of 
# a number (equivalent to (exp(number) + exp(-number)) / 2).
#Syntax
#math.cosh(x)
#Parameter Values
#Parameter：Description
#x：Required. A number to find the hyperbolic cosine of. 
# If the value is not a number, it returns a TypeError
#Technical Details
#Return Value:	A float value, representing the hyperbolic 
# cosine of a number
#Python Version:	1.4