#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("--------trunc()傳回截斷整數部份的數字(小數點後面去除)")
#https://www.w3schools.com/python/ref_math_trunc.asp
#Python math.trunc() Method trunc()的方法
#Returns the truncated integer parts of a number
#傳回截斷整數部份的數字(小數點後面去除)
#Find the integer part of different numbers:
#求不同數的整數部分：
# Import math Library
import math
# Return the truncated integer parts of different numbers
print(math.trunc(2.77))
print(math.trunc(8.32))
print(math.trunc(-99.29))
#Definition and Usage 定義和使用
#The math.trunc() method returns the truncated integer part of a number.
#math.trunc()方法返回數位的截斷的整數部分。
#Note: This method will NOT round the number up/down to the nearest integer, but simply remove the decimals.
#注意：此方法不會將數位向上/向下捨入到最接近的整數，而只是刪除小數。
#Syntax
#math.trunc(x)
#Parameter Values
#Parameter：Description
#x：Required. The number you want to remove the decimal 
# part of. If the value is not a number, it returns a 
# TypeError
#必需的參數， 您要刪除的小數部份的數位。如果該值不是數位，
# 則返回TypeError
#Technical Details
#Return Value:	An int value, representing the truncated integer parts of a number
#Python Version:	1.4

