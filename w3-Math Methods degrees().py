#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------degrees()從弧度到度轉換到角度")
#https://www.w3schools.com/python/ref_math_degrees.asp
#Python math.degrees() Method degrees()的方法
#Converts an angle from radians to degrees
#從弧度到度轉換到角度
#Convert angles from radians to degrees:
# Import math Library
import math
# Convert from radians to degrees:
print (math.degrees(8.90))
print (math.degrees(-20))
print (math.degrees(1))
print (math.degrees(90))
#Definition and Usage 定義和使用
#The mmath.degrees() method converts an angle from 
# radians to degrees.
#Tip: PI (3.14..) radians are equal to 180 degrees, 
# which means that 1 radian is equal to 57.2957795 degrees.
#Tip: See also math.radians() to convert a degree value 
# into radians.
#Syntax 語法
#math.degrees(x)
#Parameter Values
#Parameter：Description
#x：Required. A radian value to convert into degrees. 
# If the parameter is not a number, it returns a TypeError
#Technical Details
#Return Value:	A float value, representing the value 
# in degrees
#Python Version:	2.3

