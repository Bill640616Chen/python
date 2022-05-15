#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------log1p()傳回自然的log(1+number)")
#https://www.w3schools.com/python/ref_math_log1p.asp
#Python math.log1p() Method log1p()的方法
#Returns the natural logarithm of 1+x
#傳回自然的log(1+number)
#Find the log(1+number) for different numbers
#尋找不同數位的log（1+number）
# Import math Library
import math
# Return the log(1+number) for different numbers
#傳回不同数字的log(1+number)
print(math.log1p(2.7183))
print(math.log1p(2))
print(math.log1p(1))
#Definition and Usage 定義和使用
#The math.log1p() method returns log(1+number), computed
# in a way that is accurate even when the value of number 
# is close to zero.
#math.log1p()方法返回log（1 + number），即使在number的值接
# 近於零的情況下，其計算方式也是準確的。
#Syntax
#math.log1p(x)
#Parameter Values
#Parameter：Description
#x：Required. Specifies the number to process. If the value 
# is a negative number, it returns a ValueError. 
# If the value is not a number, it returns a TypeError
#指定要處理的數字
#如果值為負數，則返回ValueError。
#如果該值不是數字，則返回TypeError
#Technical Details
#Return Value:	A float value, representing the log value of 1+number
#Python Version:	2.6