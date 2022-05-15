#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("--frexp()傳回將尾數和 index 作為給定數字x的一對(m，e)值")
#https://www.w3schools.com/python/ref_math_frexp.asp
#Python math.frexp() Method frexp()的方法
#Returns the mantissa and the exponent, of a specified number
#傳回將尾數和 index 作為給定數字x的一對(m，e)值
#它以給定值x的一對(m，e)返回尾數和 index ，其中尾數m是浮點數，
# e index 是整數。 m是一個浮點數，e是一個整數，
# 使得x == m * 2 ** e正好。
#Find the mantissa and exponent of a number:
#Import math Library
import math
#Return mantissa and exponent of numbers
print(math.frexp(4))
print(math.frexp(-4))
print(math.frexp(7))
#Definition and Usage 定義和使用
#The math.frexp() method returns the mantissa and the exponent of a specified number, as a pair (m,e).
#The mathematical formula for this method is: number = m * 2**e.
#Syntax
#math.frexp(x)
#Parameter Values
#Parameter：Description
#x：Required. A positive or negative number. If the value is not a number, it returns TypeError
#Technical Details
#Return Value:	A tuple value, representing the mantissa and exponent of x, as a pair (m,e). Mantissa is returned as float exponent returned as integer
#Python Version:	2.6
