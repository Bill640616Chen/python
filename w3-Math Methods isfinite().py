#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------------isfinite()檢查數字是否有限")
#https://www.w3schools.com/python/ref_math_isfinite.asp
#Python math.isfinite() Method isfinite()的方法
#Checks whether a number is finite or not
#檢查數字是否有限
#Check whether a value is finite or not:
# Import math Library
import math
# Check whether the values are finite or not
print(math.isfinite(2000)) #True
print(math.isfinite(-45.34)) #True
print(math.isfinite(+45.34)) #True
print(math.isfinite(math.inf)) #False
print(math.isfinite(float("nan"))) #False
print(math.isfinite(float("inf"))) #False
print(math.isfinite(float("-inf"))) #False
print(math.isfinite(-math.inf)) #False
print(math.isfinite(0.0)) #True
#Definition and Usage 定義和使用
#math.isfinite() method is a library method of math module, 
# it is used to check whether a given number is a finite 
# number of not, it accepts a number (integer/float, finite, 
# infinite or NaN), and returns True if number neither an 
# infinity nor a NaN (Not A Number), else it returns False.
#math.isfinite()方法是數學模組的庫方法，用於檢查給定數是否
# 為not的有限數，它接受數字(整數/浮點數，有限，無限或NaN)，
# 如果滿足，則返回True既不是無窮大也不是NaN(不是數字)，
# 否則返回False
#The math.isfinite() method checks whether a number is
# finite or not.
#This method returns True if the specified number is 
# a finite number, otherwise it returns False.
#Syntax
#math.isfinite(x)
#Parameter Values
#Parameter：Description
#x：Required. The value to check. Must be a number 
# (float/integer/infinite/NaN/finite)
#Technical Details
#Return Value:	A bool value, True if x is finite, 
# False if x is either an infinity or a NaN
#Python Version:	New in Python 3.2