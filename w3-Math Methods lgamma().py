#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("------------------lgamma()求不同數值的對數gamma值")
#https://www.w3schools.com/python/ref_math_lgamma.asp
#Python math.lgamma() Method lgamma()的方法
#Returns the log gamma value of x
#求不同數值的對數gamma值
#Find the log gamma value of different numbers:
# Import math Library
import math
# Return the log gamma value of different numbers
print (math.lgamma(7))
print (math.lgamma(-4.2))
#Definition and Usage 定義和使用
#The math.lgamma() method returns the natural logarithm 
# gamma value of a number.
#math.lgamma()方法返回數位的自然對數伽瑪值。
#Tip: We can find also find the log gamma value by using the
# math.gamma() method to find the gamma value, and then use 
# the math.log() method to calculate the log of that value.
#提示：我們還可以通過使用math.gamma（）方法找到伽馬值，然後使用
# math.log（）來找到對數gamma值方法來計算該值的對數。
#Tip: The gamma value is equal to factorial(x-1).
#提示：伽瑪值等於階乘（x-1）
#Syntax
#math.lgamma(x)
#Parameter Values
#Parameter	Description
#x	Required. The number to find the log gamma value of. If the number is a negative integer, it returns a ValueError. If it is not a number, it returns a TypeError.
#Technical Details
#Return Value:	A float value, representing the log gamma value of a number
#Python Version:	3.2

