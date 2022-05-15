#https://www.w3schools.com/python/ref_cmath_acosh.asp
#Python cmath.acosh() Method
#Find the inverse hyperbolic arc cosine value of a complex number:
#求出複數的反雙曲弧餘弦值：
#import cmath for complex number operations
import cmath
#find the hyperbolic arc cosine of a complex number
print (cmath.acos(2 + 3j))
#Definition and Usage 定義和用法
#The cmath.acosh() method returns the inverse hyperbolic cosine of a complex number.
#該方法返回複數的反雙曲餘弦。cmath.acosh()
#There is one branch cut:
#有一個分支切口：
#Extending left from 1 along the real axis to -∞, continuous from above
#從 1 沿實軸向左延伸至 -∞，從上方連續
#Syntax 語法
#cmath.acosh(x)
#Parameter Values 參數值
#Parameter	Description
#x：Required. The number to find the inverse hyperbolic cosine of
#必填。求出的逆雙曲餘弦的數
#Technical Details 技術細節
#Return Value:	A complex value, representing the inverse hyperbolic arc cosine of a number
#返回值：	一個值，表示數位的反雙曲弧餘弦complex
#Python Version:	1.5