#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("---------------isnan()可用於檢查浮點物件中的 nan 常數")
#https://www.w3schools.com/python/ref_math_isnan.asp
#Python math.isnan() Method isnan()的方法
#Checks whether a value is NaN (not a number) or not
#可用於檢查浮點物件中的 nan 常數
#Check whether a value is NaN or not:
# Import math Library
import math
# Check whether some values are NaN or not
print (math.isnan (56)) #False
print (math.isnan (-45.34)) #False
print (math.isnan (+45.34)) #False
print (math.isnan (math.inf)) #False
print (math.isnan (float("nan"))) #True
print (math.isnan (float("inf"))) #False
print (math.isnan (float("-inf"))) #False
print (math.isnan (math.nan)) #True
#Definition and Usage 定義和使用
#The math.isnan() method checks whether a value is NaN (Not a Number), or not.
#This method returns True if the specified value is a NaN, otherwise it returns False.
#Syntax
#math.isnan(x)
#Parameter Values
#Parameter：Description
#x：Required. The value to check
#Technical Details
#Return Value:	A bool value, True if the value is NaN, otherwise False
#Python Version:	3.5