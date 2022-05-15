#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------------isclose()檢查兩個值是否相近")
#https://www.w3schools.com/python/ref_math_isclose.asp
#Python math.isclose() Method isclose()的方法
#Checks whether two values are close to each other, or not
#檢查兩個值是否相近
#Import math Library
import math
#compare the closeness of two values
print(math.isclose(1.233, 1.4566))
print(math.isclose(1.233, 1.233))
print(math.isclose(1.233, 1.24))
print(math.isclose(1.233, 1.233000001))
#Definition and Usage 定義和使用
#The math.isclose() method checks whether two values are 
# close to each other, or not. Returns True if the values 
# are close, otherwise False.
#This method uses a relative or absolute tolerance, to see 
# if the values are close.
#Tip: It uses the following formula to compare the values: 
# abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
#Syntax
#math.isclose(a, b, rel_tol, abs_tol)
#rel_tol：被視為"close"的最大差，相對於輸入值的大小
#abs_tol："close"的最大差異，與輸入值的大小無關
#Parameter Values
#Parameter：Description
#a：Required. The first value to check for closeness
#b：Required. The second value to check for closeness
#rel_tol = value：Optional. The relative tolerance. It is the maximum allowed difference between value a and b. Default value is 1e-09
#abs_tol = value：Optional. The minimum absolute tolerance. It is used to compare values near 0. The value must be at least 0
#Technical Details
#Return Value:	A bool value. True if the values are close, otherwise False
#Python Version:	3.5
#Use absolute tolerance:

print("--------------第二範例----isclose()檢查兩個值是否相近")
#Import math Library
import math
#compare the closeness of two values
print(math.isclose(8.005, 8.450, abs_tol = 0.4))
print(math.isclose(8.005, 8.450, abs_tol = 0.5))