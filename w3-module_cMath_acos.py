#https://www.w3schools.com/python/ref_cmath_acos.asp
#Python cmath.acos() Method
#Find the arc cosine of a complex number:
#求出複數的餘弦弧：
#import cmath for complex number operations
import cmath
#find the arc cosine of a complex number
print (cmath.acos(2+3j))
#Definition and Usage 定義和用法
#The cmath.acos() method returns the arc cosine of a complex number.
#該方法返回複數的弧餘弦。cmath.acos()
#There are two branch cuts:
#有兩個分支切口：
#Extends right from 1 along the real axis to ∞
#從 1 沿實軸向右延伸到∞
#Extends left from -1 along the real axis to -∞.
#沿實軸從 -1 向左延伸至 -∞。
#Syntax 語法
#cmath.acos(x)
#Parameter Values 參數值
#Parameter：Description
#x：Required. A number to find the arc cosine of
#必填。用於查找的弧餘弦的數位
#Technical Details 技術細節
#Return Value:	A complex value, representing the arc cosine of a number. If the return value can be expressed as a real number, the return value has an imaginary part of 0
#返回值：	一個值，表示數位的餘弦弧。如果返回值可以表示為實數，則返回值的虛部為0complex
#Python Version:	1.5

