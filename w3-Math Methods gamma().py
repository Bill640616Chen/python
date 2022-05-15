#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("--------------------------gamma()在 x 傳回伽馬函數")
#https://www.w3schools.com/python/ref_math_gamma.asp
#Python math.gamma() Method gamma()的方法
#Returns the gamma function at x
#在 x 傳回伽馬函數
#Find the gamma function of different numbers:
# Import math Library
import math
# Return the gamma function for different numbers
print(math.gamma(-0.1))
print(math.gamma(8))
print(math.gamma(1.2))
print(math.gamma(80))
print(math.gamma(-0.55))
#Definition and Usage 定義和使用
#The math.gamma() method returns the gamma function at a number.
#Tip: To find the log gamma value of a number, use the math.lgamma() method.
#Syntax
#math.gamma(x)
#Parameter Values
#Parameter：Description
#x：Required. A number to find the gamma function for. If the number is a negative integer, it returns a ValueError. If it is not a number, it returns a TypeError.
#Technical Details
#Return Value:	A float value, representing the gamma function at x
#Python Version:	3.2
