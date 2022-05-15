#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("--------------------------sin()傳回三角函數sine的值")
#https://www.w3schools.com/python/ref_math_sin.asp
#Python math.sin() Method sin()的方法
#Returns the sine of a number
#傳回三角函數sine的值
#Find the sine of different numbers:
#尋找不同數值的正弦值：
# Import math Library
import math
# 傳回不同值的正弦值
print (math.sin(0.00))
print (math.sin(-1.23))
print (math.sin(10))
print (math.sin(math.pi))
print (math.sin(math.pi/2))
#Definition and Usage 定義和使用
#The math.sin() method returns the sine of a number.
#math.sin()方法返回數位的正弦值。
#Note: To find the sine of degrees, it must first be 
# converted into radians with the math.radians() method (see example below).
#注意：要查找度數的正弦，必須首先使用方法將其轉換為弧度
# （請參見下面的示例）。math.radians()
#Syntax
#math.sin(x)
#Parameter Values
#Parameter：Description
#x：Required. The number to find the sine of. 
# If the value is not a number, it returns a TypeError
#必需的參數， 尋找正弦的數位。如果該值不是數位，則返回TypeError
#Technical Details
#Return Value:	A float value, from -1 to 1, representing the sine of an angle
#Python Version:	1.4
print("------------------範例2---sin()傳回三角函數sine的值")
#Find the sine of different degrees:
# Import math Library
import math
# Return the sine value of 30 degrees
print(math.sin(math.radians(30)))
# Return the sine value of 90 degrees
print(math.sin(math.radians(90)))