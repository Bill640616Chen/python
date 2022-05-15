#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-----------------------------expm1()傳回E的x次方—１")
#https://www.w3schools.com/python/ref_math_expm1.asp
#Python math.expm1() Method expm1()的方法
#Returns Ex - 1
#傳回E的x次方—１
#Find the exponential value of a number - 1:
#Import math Library
import math
#Return the exponential value of a number - 1
print(math.expm1(32))
print(math.expm1(-10.89))
#Definition and Usage 定義和使用
#The math.expm1() method returns Ex - 1.
#該方法返回 Emath.expm1()x- 1.
#'E' is the base of the natural system of logarithms (approximately 2.718282) and x is the number passed to it.
#"E"是自然對數系統（約2.718282）的基數，x是傳遞給它的數位。
#This function is more accurate than calling math.exp() and subtracting 1.
#此函數比調用和減去 1 更準確。 math.exp()
#Syntax
#math.expm1(x)
#Parameter Values
#Parameter：Description
#x：Required. Specifies the exponent
#Technical Details
#Return Value:	A float value, representing Ex - 1
#Python Version:	2.7

