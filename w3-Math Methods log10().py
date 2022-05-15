#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("------------------------log10()傳回以10為底的對數")
#https://www.w3schools.com/python/ref_math_log10.asp
#Python math.log10() Method log10()的方法
#Returns the base-10 logarithm of x
#傳回以10為底的對數x
#Find the base-10 logarithm of different numbers
#查找不同數字的以10為底的對數
# Import math Library
import math
# Return the base-10 logarithm of different numbers
#傳回不同數字的以10為底的對數
print(math.log10(2.7183))
print(math.log10(2))
print(math.log10(1))
print(math.log10(math.pi))
print(math.log10(8,2))
#Definition and Usage 定義和使用
#The math.log10() method returns the base-10 logarithm of a number.
#math.log10()方法返回數位的以10為底的對數。
#Syntax
#math.log10(x)
#Parameter Values
#Parameter：Description
#x：Required. Specifies the value to calculate the logarithm
# for. If the value is 0 or a negative number, it returns 
# a ValueError. If the value is not a number, it returns 
# a TypeError
#必需的參數， 指定要為其計算對數的值。
#如果值為0或負數，則返回ValueError。
#如果該值不是數字，則返回TypeError
#Technical Details
#Return Value:	A float value, representing the base-10 logarithm of a number
#Python Version:	2.3

