#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------copysign(x, y)sign符號是+/-號)")
#https://www.w3schools.com/python/ref_math_copysign.asp
#Python math.copysign() Method copysign()的方法
#Returns a float consisting of the value of the first 
# parameter and the sign of the second parameter
#傳回第一個參數"值"和第二個參數值的"標誌",由浮點數組成的值
#Return the value of the first parameter and the sign 
# of the second parameter:
#Import math Library
import math
#Return the value of the first parameter and the sign 
# of the second parameter
print(math.copysign(4, -1))
#第一個參數是4,第二個參數的符號是-,所以輸出為-4.0(要float)
print(math.copysign(-8, 97.21))
#第一個參數是-8,第二個參數的符號是+,所以輸出為8.0(要float)
print(math.copysign(-43, -76))
#第一個參數是-43,第二個參數的符號是-,所以輸出為-43.0(要float)
#Definition and Usage 定義和使用
#The math.copysign() method returns a float consisting 
# of the value of the first parameter and the sign(+/-) 
# of the second parameter.
#Syntax 語法
#math.copysign(x, y)
#signh符號是+/-號
#Parameter Values
#Parameter：Description
#x：Required. A number. The return will have the value of this parameter
#y：Required. A number. The return will have the sign (+/-) of this parameter
#Technical Details
#Return Value:	A float value, which consists of  the value of first parameter, and sign of the second parameter
#Python Version:	2.6