#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------------log2()傳回以2為底的對數x")
#https://www.w3schools.com/python/ref_math_log2.asp
#Python math.log2() Method log2()的方法
#Returns the base-2 logarithm of x
#傳回以2為底的對數x
#Find the base-2 logarithm of different numbers
#查找不同數字的以2為底的對數
# Import math Library
import math
# Return the base-2 logarithm of different numbers
print(math.log2(2.7183))
print(math.log2(2))
print(math.log2(1))
#Definition and Usage 定義和使用
#The math.log2() method returns the base-2 logarithm of a 
# number.
#math.log2()方法返回數位的以2為底的對數。
#Syntax
#math.log2(x)
#Parameter Values
#Parameter：Description
#x：Required. Specifies the value to calculate the logarithm for. If the value is 0, or a negative number, it returns a ValueError. If the value is not a number, it returns a TypeError
#Technical Details
#Return Value:	A float value, representing the base-2 logarithm of a number
#Python Version:	3.3