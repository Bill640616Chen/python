#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("--------------------------------hypot()返回開平方值")
#https://www.w3schools.com/python/ref_math_hypot.asp
#Python math.hypot() Method hypot()的方法
#Find the hypotenuse of a right-angled triangle where perpendicular and base are known:
#傳回歐幾里德範數 sqrt(x*x + y*y)。sqrt是開平方值
#Import math Library
import math
#set perpendicular and base
parendicular = 10
base = 5
#print the hypotenuse of a right-angled triangle
print(math.hypot(parendicular, base))
#Definition and Usage 定義和使用
#The math.hypot() method returns the Euclidean norm. The Euclidian norm is the distance from the origin to the coordinates given.
#Prior Python 3.8, this method was used only to find the hypotenuse of a right-angled triangle: sqrt(x*x + y*y).
#From Python 3.8, this method is used to calculate the Euclidean norm as well. For n-dimensional cases, the coordinates passed are assumed to be like (x1, x2, x3, ..., xn). So Euclidean length from the origin is calculated by sqrt(x1*x1 + x2*x2 +x3*x3 .... xn*xn).
#Syntax
#math.hypot(x1, x2, x3, ..., xn)
#Parameter Values
#Parameter	Description
#x1, x2, x3, ..., xn	Required. Two or more points representing coordinates
#Technical Details
#Return Value:	A float value, representing the Euclidean distance from the origin for n inputs, or hypotenuse of a right-angled triangle for two inputs
#Change Log:	From 3.8: Also supports n-dimensional points. Earlier versions only support two-dimensional points
#Find the Euclidean norm for the given points:
#Import math Library
print("------------------------第二範例----hypot()返回開平方值")
import math
#print the Euclidean norm for the given points
print(math.hypot(10, 2.1, 4, 13))
print(math.hypot(4, 7, 8))
print(math.hypot(12, 14))
#把其中一個參數改成負數,不影響原正數的結果