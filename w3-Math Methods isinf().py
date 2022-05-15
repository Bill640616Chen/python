#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------------isinf()檢查數字是否無限")
#https://www.w3schools.com/python/ref_math_isinf.asp
#Python math.isinf() Method isinf()的方法
#Checks whether a number is infinite or not
#檢查數字是否無限
#Check whether a value is infinity or not:
# Import math Library
import math
# Check whether the values are infinite or not
print(math.isinf(56)) #False
print(math.isinf(-45.34)) #False
print(math.isinf(+45.34)) #False
print(math.isinf(math.inf)) #True
print(math.isinf(float("nan"))) #False
print(math.isinf(float("inf"))) #True
print(math.isinf(float("-inf"))) #True
print(math.isinf(-math.inf)) #True
#Definition and Usage 定義和使用
#The math.isinf() method checks whether a number is infinite or not.
#This method returns True if the specified number is a positive or negative infinity, otherwise it returns False.
#Syntax
#math.isinf(x)
#Parameter Values
#Parameter：Description
#x：Required. The number to check
#Technical Details
#Return Value:	A bool value, True if x is a positive or negative infinity, False otherwise
#Python Version:	2.6

