#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("------------------------pow()提高x的y次方值")
#https://www.w3schools.com/python/ref_math_pow.asp
#Python math.pow() Method pow()的方法
#Returns the value of x to the power of y
#傳回提高高x的y次方值
#Find the value of 9 raised to the power of 3:
# Import math Library
import math
#Return the value of 9 raised to the power of 3
print(math.pow(9, 3))
#Definition and Usage 定義和使用
#The math.pow() method returns the value of x raised to 
# power y.
#math.pow（）方法傳回提高到高x的y次方值。
#If x is negative and y is not an integer, it returns a 
# ValueError.
#如果x是負數，而y不是整數，則傳回ValueError。
#This method converts both arguments into a float.
#此方法將兩個參數都轉換為浮點數。
#Tip: If we use math.pow(1.0,x) or math.pow(x,0.0), it will 
# always returns 1.0.
#提示：如果我們使用math.pow(1.0,x)或math.pow(x,0.0)，
# 它將始終返回1.0。math.pow（1.0，x）math.pow（x，0.0）
#Syntax
#math.pow(x, y)
#Parameter Values
#Parameter：Description
#x：Required. A number which represents the base
#x：必需的參數。 表示底數的數位
#y：Required. A number which represents the exponent
#y：必需的參數， 代表指數的數位
#Technical Details
#Return Value:	A float value, representing the value of x to the power of y (xy)

