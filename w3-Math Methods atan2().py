#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-----------------------arc atan2(反正切三角函數)方法")
#https://www.w3schools.com/python/ref_math_atan2.asp
#Python math.atan2(y, x) Method 的方法
#Returns the arc tangent of y/x in radians
# 傳回y/x反正切三角函數弧度值 
# Import math Library
import math
# Return the arc tangent of y/x in radians
print(math.atan2(8, 5))
print(math.atan2(20, 10))
print(math.atan2(34, -7))
#https://dqydj.com/inverse-tangent-calculator/
#在網站計算時,要選擇輸出Radians
#Definition and Usage 定義和使用
#The math.atan2() method returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y).
#The returned value is between PI and -PI.
#Syntax 語法
#math.atan2(y, x)
#Parameter Values
#Parameter：Description
#y：Required. Specifies a positive or negative number
#x：Required. Specifies a positive or negative number
#Technical Details
#Return Value:	A float value, representing arc tangent of y/x in radians, which is between PI and -PI
#Python Version:	1.4

