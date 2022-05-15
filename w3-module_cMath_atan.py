#https://www.w3schools.com/python/ref_cmath_atan.asp
#Python cmath.atan() Method
#Find the arctangent of a complex number:
#求出複數的反正切：
#import cmath for complex number operations
import cmath
#find the arc tangent of a complex number
print (cmath.atan(2 + 3j))
#Definition and Usage 定義和用法
#The method returns the arc tangent of a complex number.cmath.atan()
#該方法返回複數的圓弧切線。cmath.atan()
#There are mainly two branch cuts:
#主要有兩個分支切口：
#Extending from 1j along the imaginary axis to ∞j towards the right
#沿虛軸從 1j 延伸到右側的 ∞j
#Extending from -1j along the imaginary axis to -∞j towards left
#沿虛軸從 -1j 向左延伸至 -∞j
#Syntax 語法
#cmath.atan(x)
#Parameter Values 參數值
#Parameter	Description
#x：Required. A number to find the arctangent of
#必填。要查找的反正切值的數位
#Technical Details 技術細節
#Return Value:	A value, representing arc tangent of a complex numbercomplex
#返回值：	一個值，表示複數的圓角切線complex
#Python Version:	2.6

