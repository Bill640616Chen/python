#https://www.w3schools.com/python/ref_cmath_isinf.asp
#Python cmath.isinf() Method
#Check whether a complex value is infinite or not:
#檢查複數值是否無限：
#import cmath for complex number operations
import cmath
#find whether a complex number is infinite or not
print (cmath.isinf(complex(10 + float('inf'))))
print (cmath.isinf(11 + 4j))
#Definition and Usage 定義和用法
#The method checks whether a value is positive or negative infinity, or not. This method returns a Boolean value: if the value is infinity, otherwise .cmath.isinf()TrueFalse
#該方法檢查值是正無窮大還是負無窮大。此方法傳回一個布林值：如果該值為無窮大，否則 。cmath.isinf()True False
#Syntax 語法
#cmath.isinf(x)
#Parameter Values
#Parameter	Description
#x：Required. The value to check for infinity
#必填。要檢查無窮大的值
#Technical Details 技術細節
#Return Value:	A value, if the value is infinity, otherwise boolTrueFalse
#返回值：	一個值，如果該值為無窮大，否則bool True False
#Python Version:	2.6

