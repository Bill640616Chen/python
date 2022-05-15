#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-----------------------arc atanh()(反正切三角函數)方法")
#https://www.w3schools.com/python/ref_math_atanh.asp
#Python math.atanh() Method 的方法
#Returns the inverse hyperbolic tangent of a number
#傳回反雙曲正切三角函數值
#Find the hyperbolic arctangent value of different numbers:
#找到不同數字的反雙曲正切三角函數值
#Import math Library
import math
#print the hyperbolic arctangent of different numbers
print(math.atanh(0.59))
print(math.atanh(-0.12))
#https://dqydj.com/inverse-hyperbolic-tangent-calculator/
#Definition and Usage 定義和使用
#The math.atanh() method returns the inverse hyperbolic tangent of a number.
#Note: The parameter passed in math.atanh() must lie between -0.99 to 0.99.
#Syntax
#math.atanh(x)
#Parameter Values
#Parameter：Description
#x：Required. A positive or negative number between -0.99 and 0.99. If x is not a number, it returns a TypeError
#Technical Details
#Return Value:	A float value, representing the inverse hyperbolic tangent of a number
#Python Version:	2.6