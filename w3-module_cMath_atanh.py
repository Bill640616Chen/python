#https://www.w3schools.com/python/ref_cmath_atanh.asp
#Python cmath.atanh() Method
#Find the hyperbolic arctangent of a complex number:
#求出複數的雙曲反正切：
#import cmath for complex number operations
import cmath
#find the hyperbolic arctangent of a complex number
print (cmath.atanh(2+ 3j))
#Definition and Usage 定義和用法
#The method returns the inverse hyperbolic tangent of a complex number.cmath.atanh()
#該方法返回複數的反雙曲正切。cmath.atanh()
#There are two branch cuts:
#有兩個分支切口：
#Extends from 1 along the real axis to ∞, continuous from below
#從 1 沿實軸延伸到 ∞，從下方連續
#Extends from -1 along the real axis to -∞, continuous from above
#從 -1 沿實軸延伸到 -∞，從上方連續
#Syntax 語法
#cmath.atanh(x)
#Parameter Values 參數值
#Parameter	Description
#x：Required. A number to find the inverse hyperbolic arctangent of
#必填。一個數位，用於查找 的逆雙曲反正切
#Technical Details 技術細節
#Return Value:	A value, representing inverse hyperbolic tangent of a complex numbercomplex
#返回值：	值，表示複數的反雙曲正切complex
#Python Version:	1.5

