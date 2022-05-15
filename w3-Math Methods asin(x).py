#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("------------------------arc asin(反正弦三角函數)方法")
#https://www.w3schools.com/python/ref_math_asin.asp
#Python math.asin() Method 反正弦三角函數的方法
#Returns the arc sine of a number 傳回反正弦值
#Return the arc sine of different numbers:
#傳回不同數字的反正弦值arc sine：
# Import math Library
import math
# Return the arc sine of numbers
print(math.asin(0.55))
print(math.asin(-0.55))
print(math.asin(0))
print(math.asin(1))
print(math.asin(-1))
#https://dqydj.com/inverse-sine-calculator/
#Definition and Usage 定義和使用
#The math.asin() method returns the arc sine of a number.
#math.asin()方法傳回反正弦值
#Note: The parameter passed in math.asin() must lie between -1 to 1.
#筆記：math.asin()裡的參數值一定要在-1到1之間
#Tip: math.asin(1) will return the value of PI/2, and math.asin(-1) will return the value of -PI/2.
#提示：math.asin(1)將會傳回PI值的一半,math.asin(-1)將會傳回-PI值的一半
#Syntax 語法
#math.asin(x)
#Parameter Values
#Parameter：Description
#x：Required. A number in the range -1 to 1. If x is not 
# a number, it returns a TypeError
#Technical Details
#Return Value:	A float value, representing the arc sine of a number
#Python Version:	1.4