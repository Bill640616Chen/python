#https://www.w3schools.com/python/ref_cmath_asin.asp
#Python cmath.asin() Method
#Find the arc sine of a complex number:
#求出複數的弧正弦：
#import cmath for complex number operations
import cmath
#find the arc sine of a complex number
print (cmath.asin(2 + 3j))
#Definition and Usage 定義和用法
#The method returns the arc sine of a complex number.cmath.asin()
#該方法返回複數的弧正弦。cmath.asin()
#There are two branch cuts:
#有兩個分支切口：
#Extends right from 1 along the real axis to ∞
#從 1 沿實軸向右延伸到∞
#Extends left from -1 along the real axis to -∞
#沿實軸從 -1 向左延伸至 -∞
#Syntax 語法
#cmath.asin(x)
#Parameter Values 參數值
#Parameter	Description
#x：Required. A number to find the arc sine of
#必填。用於查找的弧正弦的數位
#Technical Details 技術細節
#Return Value:	A value, representing the arc sine of a complex numbercomplex
#返回值：	值，表示複數的弧正弦complex
#Python Version:	1.5