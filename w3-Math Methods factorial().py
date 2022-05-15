#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-----------------------------factorial()傳回數字的階乘")
#https://www.w3schools.com/python/ref_math_factorial.asp
#Python math.factorial() Method factorial()的方法
#Returns the factorial of a number
#傳回數字的階乘
#Find the factorial of a number:
#Import math Library
import math
#Return factorial of a number
print(math.factorial(9))
print(math.factorial(6))
print(math.factorial(12))
#Definition and Usage 定義和使用
#The math.factorial() method returns the factorial of 
# a number.
#Note: This method only accepts positive integers.
#The factorial of a number is the sum of the multiplication, 
# of all the whole numbers, from our specified number down 
# to 1. For example, the factorial of 6 would be 
# 6 x 5 x 4 x 3 x 2 x 1 = 720
#Syntax
#math.factorial(x)ｘ只能是正數
#Parameter Values
#Parameter：Description
#x：Required. A positive integer. If the number is 
# negative, or not an integer, it returns a ValueError. 
# If the value is not a number, it returns a TypeError
#Technical Details
#Return Value:	A positive int value
#Python Version:	2.6