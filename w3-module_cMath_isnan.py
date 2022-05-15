#https://www.w3schools.com/python/ref_cmath_isnan.asp
#Python cmath.isnan() Method
#Check whether a complex value is NaN or not:
#檢查複數值是否為 NaN：
#import cmath for complex number operations
import cmath
#find whether a complex number is NaN or not
print (cmath.isnan(12 + float('nan')))
print (cmath.isnan(2 + 3j))
#Definition and Usage 定義和用法
#The cmath.isnan() method checks whether a value is nan (Not a Number), or not. This method returns a Boolean value: True if the value is nan, otherwise False
#該方法檢查值是否為 nan（不是數位）。此方法返回一個布爾值：如果該值為 nan，否則cmath.isnan()True False
#Syntax 語法
#cmath.isnan(x)
#Parameter Values 參數值
#Parameter	Description
#x：Required. The value to check for NaN
#必填。要檢查 NaN 的值
#Technical Details 技術細節
#Return Value:	A bool value, True if any part (real or imaginary) of a complex number is NaN, otherwise False
#返回值：	如果複數的任何部分（實數或虛數）為 NaN，則為值，否則boolTrueFalse
#Python Version:	2.6

