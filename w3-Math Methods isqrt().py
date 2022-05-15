#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("---------------isqrt()將平方根向下取整至最接近的整數")
#https://www.w3schools.com/python/ref_math_isqrt.asp
#Python math.isqrt() Method isqrt()的方法
#Rounds a square root number downwards to the nearest integer
#將平方根向下取整至最接近的整數
#Round a square root number downwards to the nearest integer:
# Import math Library
import math
# Print the square root of different numbers
#sqrt()開平方
print (math.sqrt(10)) 
print (math.sqrt (12))
print (math.sqrt (68))
print (math.sqrt (100))
# Round square root downward to the nearest integer
#isqrt()將平方根向下取整至最接近的整數
print (math.isqrt(10))
print (math.isqrt (12))
print (math.isqrt (68))
print (math.isqrt (100))
#Definition and Usage 定義和使用
#The math.isqrt() method rounds a square root number downwards to the nearest integer.
#Note: The number must be greater than or equal to 0.
#Syntax
#math.isqrt(x)
#Parameter Values
#Parameter：Description
#x：Required. The number to round the square root of. If x is negative, it returns a ValueError. If x is not a number, it returns a TypeError
#Technical Details
#Return Value:	An int value, representing the square root of a number, without decimals
#Python Version:	3.8
