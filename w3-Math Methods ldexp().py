#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------ldexp(x,i)用法是x * (2**i),i代表2的幾次方")
#https://www.w3schools.com/python/ref_math_ldexp.asp
#Python math.ldexp() Method ldexp()的方法
#Returns the inverse of math.frexp() which is x * (2**i) 
# of the given numbers x and i
#傳回math.frexp()的反向,用法是x * (2**i),i代表2的幾次方
#Return value of x * (2**i):
#Import math Library
import math
#Return value of x * (2**i)
print(math.ldexp(9, 3))
print(math.ldexp(-5, 2))
print(math.ldexp(15, 2))
#Definition and Usage 定義和使用
#The math.ldexp() method returns  x * (2**i) of the given numbers x and i, which is the inverse of math.frexp().
#Syntax
#math.ldexp(x, i)
#Parameter Values
#Parameter：Description
#x：Required. A positive or negative number. If the value is not a number, it returns TypeError
#i：Required. A positive or negative number. If the value is not a number, it returns TypeError
#Technical Details
#Return Value:	The value of x * (2**i)
#Python Version:	2.6
