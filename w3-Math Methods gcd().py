#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("------------------------gcd()傳回兩個整數的最大公因子")
#https://www.w3schools.com/python/ref_math_gcd.asp
#Python math.gcd() Method gcd()的方法
#Returns the greatest common divisor of two integers
#傳回兩個整數的最大公因子
#最高公因子(HCF)也稱為gcd
#Find the greatest common divisor of the two integers:
#Import math Library
import math
#find the  the greatest common divisor of the two integers
print (math.gcd(3, 6))
print (math.gcd(6, 12))
print (math.gcd(12, 36))
print (math.gcd(-12, -36))
print (math.gcd(5, 12))
print (math.gcd(10, 0))
print (math.gcd(0, 34))
print (math.gcd(0, 0))
#Definition and Usage 定義和使用
#The math.gcd() method returns the greatest common divisor of the two integers int1 and int2.
#GCD is the largest common divisor that divides the numbers without a remainder.
#GCD is also known as the highest common factor (HCF).
#Tip: gcd(0,0) returns 0.
#Syntax
#math.gcd(int1, int2)
#Parameter Values
#Parameter：Description
#int1：Required. The first integer to find the GCD for
#int2：Required. The second integer to find the GCD for
#Technical Details
#Return Value:	An int value, representing the greatest common divisor (GCD) for two integers
#Python Version:	3.5
