#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------------floor()傳回無條件捨去的數字")
#https://www.w3schools.com/python/ref_math_floor.asp
#Python math.floor() Method floor()的方法
#Rounds a number down to the nearest integer
#傳回無條件捨去的數字
#Round numbers down to the nearest integer:
# Import math library
import math
# Round numbers down to the nearest integer
print(math.floor(0.6))
print(math.floor(1.4))
print(math.floor(5.3))
print(math.floor(-5.3))
print(math.floor(22.6))
print(math.floor(10.0))
#Definition and Usage 定義和使用
#The math.floor() method rounds a number DOWN to the nearest integer, if necessary, and returns the result.
#Tip: To round a number UP to the nearest integer, look at the math.ceil() method.
#Syntax
#math.floor(x)
#Parameter Values
#Parameter：Description
#x：Required. Specifies the number to round down
#Technical Details
#Return Value:	An int value, representing the rounded number
#Change Log:	Python 3+ : Returns an int value
#Python 2.x : Returns a float value