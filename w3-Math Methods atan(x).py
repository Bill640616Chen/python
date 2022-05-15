#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-----------------------arc atan(反正切三角函數)方法")
#https://www.w3schools.com/python/ref_math_atan.asp
#Python math.atan() Method 的方法
#Returns the arc tangent of a number in radians
# 傳回反正切三角函數弧度值
#Return the arc tangent of different numbers:
#傳回不同數字的反正切三角函數值arc tan:
#Import math Library
import math
#fReturn the arc tangent of different numbers
print (math.atan(0.39))
print (math.atan(67))
print (math.atan(-21))
#https://dqydj.com/inverse-tangent-calculator/
#在網站計算時,要選擇輸出Radians
#Definition and Usage 定義和使用
#The math.atan() method returns the arc tangent of a number
# (x) as a numeric value between -PI/2 and PI/2 radians.
#傳回的是radians弧度
#Arc tangent is also defined as an inverse tangent function
# of x, where x is the value of the arc tangent is to be 
# calculated.
#Syntax 語法
#math.atan(x)
#Parameter Values
#Parameter：Description
#x：Required. A positive or negative number. If x is not a 
# number, it returns error a TypeError
#Technical Details
#Return Value:	A float value, from -PI/2 to PI/2, 
# representing the arc tangent of a number
#Python Version:	1.6.1
