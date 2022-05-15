#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("---------------ceil()(將數字無條件進到最接近的整數)方法")
#https://www.w3schools.com/python/ref_math_ceil.asp
#Python math.ceil() Method ceil()(天花板)的縮寫的方法
#Rounds a number up to the nearest integer
#將數字無條件進到最接近天花板數字的整數
#Round a number upward to its nearest integer:
# Import math library
import math
# Round a number upward to its nearest integer
print(math.ceil(1.0001))
print(math.ceil(5.3))
print(math.ceil(-5.99))
print(math.ceil(22.6))
print(math.ceil(10.0))
#Definition and Usage 定義和使用
#The math.ceil() method rounds a number UP to the nearest integer, if necessary, and returns the result.
#Tip: To round a number DOWN to the nearest integer, look at the math.floor() method.
#Syntax 語法
#math.ceil(x)
#Parameter Values
#Parameter：Description
#x：Required. Specifies the number to round up
#Technical Details
#Return Value:	An int value, representing the rounded number.
#Change Log:	Python 3+ : Returns an int value
#Python 2.x :   Returns a float value.
