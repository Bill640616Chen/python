#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-----------------------arc cosine(反餘弦三角函數)方法")
#https://www.w3schools.com/python/ref_math_acos.asp
#Python math.acos() Method 反餘弦三角函數方法
#Return the arc cosine of different numbers:
#傳回不同數字的反餘弦值arc cosine：
# Import math Library
import math
# Return the arc cosine(反三角函數) of numbers
print(math.acos(0.55))
print(math.acos(-0.55))
print(math.acos(0))
print(math.acos(1))
print(math.acos(-1))
#https://dqydj.com/inverse-cosine-calculator/
#Definition and Usage 定義和使用
#The math.acos() method returns the arc cosine value of a number.
#math.acos()方法傳回反三角函數的值
#Note: The parameter passed in math.acos() must lie between -1 to 1.
#注意：數學中通過的參數。acos())必須在 -1 到 1 之間。
#只能在-1到1之間計算
#Tip: math.acos(-1) will return the value of PI.
#提示：math.acos(-1)將傳回 PI 的值。
#Syntax
#math.acos(x)
#Parameter Values
#Parameter：Description
#x：Required. A number in the range -1 to 1. If x is not a 
# number, it returns a TypeError
#Technical Details
#Return Value:	A float value, representing the arc cosine 
# of a number
#Python Version: 1.4
