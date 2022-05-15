#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("------------------------radians()將度數轉換為弧度")
#https://www.w3schools.com/python/ref_math_radians.asp
#Python math.radians() Method radians()的方法
#Converts a degree value into radians
#將度數轉換為弧度
#Convert different degrees into radians:
# Import math Library
import math
# Convert different degrees into radians
print(math.radians(180))
print(math.radians(100.03))
print(math.radians(-20))
#Definition and Usage 定義和使用
#The math.radians() method converts a degree value into radians.
#math.radians()方法將度值轉換為弧度。
#Tip: See also math.degrees() to convert an angle from radians to degrees.
#提示：另請參見將角度從弧度轉換為度。math.degrees()
#Syntax
#math.radians(x)
#Parameter Values
#Parameter：Description
#x：Required. The degree value to be converted into radians.
# If the parameter is not a number, it returns a TypeError
#x：必需的參數， 要轉換為弧度的度值。如果參數不是數字，
# 則返回TypeError
##Technical Details
#Return Value:	A float value, representing the radian value of an angle
#Python Version:	2.0