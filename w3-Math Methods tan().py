#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("----------------------tan()傳回三角函數tangent的值")
#https://www.w3schools.com/python/ref_math_tan.asp
#Python math.tan() Method tan()的方法
#Returns the tangent of a number
#傳回三角函數tangent的值
#Find the tangent of different numbers (angles):
#尋找不同數字（角度）的切線：
# Import math Library
import math
# Return the tangent of different numbers
print (math.tan(90))
print (math.tan(-90))
print (math.tan(45))
print (math.tan(60))
#Definition and Usage 定義和使用
#The math.tan() method returns the tangent of a number.
#math.tan()方法傳回數字的切線tangent。
#Syntax
#math.tan(x)
#Parameter Values
#Parameter：Description
#x：Required. A number to find the tangent of. If the 
# value is not a number, it returns a TypeError
#必需的參數， 尋找正切的數位。如果該值不是數位，則返回TypeError
#Technical Details
#Return Value:	A float value, representing the tangent of a number
#Python Version:	1.4