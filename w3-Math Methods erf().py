#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------------erf()傳回錯誤函數的數字")
#https://www.w3schools.com/python/ref_math_erf.asp
#Python math.erf() Method erf()的方法
#Returns the error function of a number
#傳回錯誤函數的數字
#Print error function for different numbers:
# Import math Library
import math
# Print error function for different numbers
print (math.erf(0.67))
print (math.erf(1.34))
print (math.erf(-100))
#Definition and Usage 定義和使用
#The math.erf() method returns the error function of a number.
#This method accepts a value between - inf and + inf, and returns a value between - 1 to + 1.
#這個方法接受正負數的值,傳回的值介於1和-1之間
#Syntax
#math.erf(x)
#Parameter Values
#Parameter：Description
#x：Required. A number to find the error function of
#Technical Details
#Return Value:	A float value, representing the error function of a number
#Python Version:	3.2
print("-------------------------erf()傳回錯誤函數的數字測試")
#Calculate the mathematical error function of the same number, positive and negative:
print (math.erf(1.28))
print (math.erf(-1.28))