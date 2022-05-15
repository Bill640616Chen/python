#https://www.w3schools.com/python/ref_cmath_isfinite.asp
#Python cmath.isfinite() Method
#Check whether a complex value is finite or not:
#檢查複數值是否有限：
#import cmath for complex number operations
import cmath
#find whether a complex number is finite or not
print (cmath.isfinite(2 + 3j))
print (cmath.isfinite(complex(5.0,float('inf'))))
print (cmath.isfinite(float('inf')+ 5j))
#Definition and Usage 定義和用法
#The method checks whether a complex value is finite, or not. This method returns a Boolean value: if the value is finite, otherwise .cmath.isfinite()TrueFalse
#該方法檢查複數值是否有限。此方法傳回一個布林值：如果該值是有限的，否則 。cmath.isfinite()True False
#Syntax 語法
#cmath.isfinite(x)
#Parameter Values 參數值
#Parameter	Description
#x：Required. The value to check if it is finite or not
#必填。要檢查它是否有限的值
#Technical Details 技術細節
#Return Value:	A value, if the value is finite, otherwise boolTrueFalse
#返回值：	值，如果該值是有限的，否則bool True False
#Python Version:	3.2

