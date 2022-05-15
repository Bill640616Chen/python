#https://www.w3schools.com/python/ref_cmath_asinh.asp
#Python cmath.asinh() Method
#Find the hyperbolic arc sine of a complex number:
#求出複數的雙曲弧正弦：
#import cmath for complex number operations
import cmath
#find the hyperbolic arc sine of a complex number
print (cmath.asinh(2+3j))
#Definition and Usage 定義和用法
#The method returns the inverse hyperbolic sine of a number.cmath.asinh()
#該方法返回數位的反雙曲正弦。cmath.asinh()
#There are mainly two branch cuts:
#主要有兩個分支切口：
#Extending from 1j along the imaginary axis to ∞j towards the right
#沿虛軸從 1j 延伸到右側的 ∞j
#Extending from -1j along the imaginary axis to -∞j towards left
#沿虛軸從 -1j 向左延伸至 -∞j
#Syntax 語法
#cmath.asinh(x)
#Parameter Values 參數值
#Parameter	Description
#x：Required. The number to find the inverse hyperbolic sine of
#必填。求反雙曲正弦的數
#Technical Details 技術細節
#Return Value:	A value, representing inverse hyperbolic sine of a complex numbercomplex
#返回值：	一個值，表示複數的反雙曲正弦complex
#Changelog:	2.6 - Branch cuts are selected according to C99 standard
#更新紀錄：	2.6 - 根據 C99 標準選擇分支切割
