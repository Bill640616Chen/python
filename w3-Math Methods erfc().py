#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------------erfc()傳回補充錯誤函數的數字")
#https://www.w3schools.com/python/ref_math_erfc.asp
#Python math.erfc() Method erfc()的方法
#Returns the complementary error function of a number
#傳回補充錯誤函數的數字
#Print the complementary error function for different numbers:
# Import math Library
import math
# Print complementary error function for different numbers
print (math.erfc(0.67))
print (math.erfc(1.34))
print (math.erfc(-6))
#Definition and Usage 定義和使用
#The math.erfc() method returns the complementary error 
# function of a number.
#This method accepts a value between - inf and + inf, 
# and returns a value between 0 and 2.
#這個方法接受正負數,傳回的值介於0和2
#Syntax
#math.erfc(x)
#Parameter Values
#Parameter：Description
#x：Required. A number to find the complementary error function of
#Technical Details
#Return Value:	A float value, representing the complementary error function of a number
#Python Version:	3.2

