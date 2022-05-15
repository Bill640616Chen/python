#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("----------------------remainder()傳回x/y最接近的餘數")
#https://www.w3schools.com/python/ref_math_remainder.asp
#Python math.remainder() Method remainder()的方法
#Returns the closest value that can make numerator completely divisible by the denominator
#傳回最接近值，使數值器完全由分母可分割
#Return the remainder of x with respect to y:
# Import math Library
import math
# Return the remainder of x/y
#傳回x/y餘數
print (math.remainder(9, 2))
print (math.remainder(9, 3))
print (math.remainder(18, 4))
#Definition and Usage 定義和使用
#The math.remainder() method returns the remainder of 
# x with respect to y.
#math.remainder()方法返回相對於y的x的餘數。
#Syntax
#math.remainder(x, y)
#Parameter Values
#Parameter：Description
#x：Required. The number you want to divide.
#x：必需的參數， 您要除的數位。
#y：Required. The number you want to divide with. 
# It must be a non-zero number, or a ValueError occurs.
#y：必需的參數， 您要除以的數位。它必須是一個非零數字，
# 否則會發生ValueError。
#Technical Details
#Return Value:	A float value, representing the remainder
#Python Version:	3.7
print("------------範例2---remainder()傳回x/y最接近的餘數")
#Return the remainder of x/y:
print (math.remainder(23.5, 5))
#若23.5-4*5=3.5,但23.5-5*5=-1.5,-1.5<3.5,所以最接近為-1.5
print (math.remainder(23, 5.5))
print (math.remainder(12.5, 2.5))
print (math.remainder(12, 2))