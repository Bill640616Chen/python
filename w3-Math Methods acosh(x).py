#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("---------------------arc acosh(反雙曲餘弦三角函數)方法")
#https://www.w3schools.com/python/ref_math_acosh.asp
#Python math.acosh() Method 反雙曲餘弦三角函數的方法
#Return the inverse hyperbolic cosine of different numbers:
#傳回不同數字的反正弦值inverse hyperbolic cosine：
# Import math Library
import math
# Return the inverse hyperbolic cosine of different numbers
print (math.acosh(7))
print (math.acosh(56))
print (math.acosh(2.45))
print (math.acosh(1))
#https://dqydj.com/inverse-hyperbolic-cosine-calculator/
#Definition and Usage 定義和使用
#The math.acosh() method returns the inverse hyperbolic 
# cosine of a number.
#Note: The parameter passed in acosh() must be greater than or equal to 1.
#參數通過acosh()一定要大於或等於1
#Syntax
#math.acosh(x)
#Parameter Values
#Parameter：Description
#x：Required. A positive number >= 1. If x is not a number, 
# it returns a TypeError
#Technical Details
#Return Value:	A float value, representing the inverse 
# hyperbolic cosine of x
#Python Version: 2.6