#https://www.w3schools.com/python/ref_cmath_polar.asp
#Python cmath.polar() Method
#Convert a complex number to polar coordinates form:
#將複數轉換為極座標形式：
#import cmath for complex number operations
import cmath
#find the polar coordinates of complex number
print (cmath.polar(2 + 3j))
print (cmath.polar(1 + 5j))
#Definition and Usage 定義和用法
#The method converts a complex number to polar coordinates. It returns a tuple of modulus and phase.cmath.polar()
#該方法將複數轉換為極座標。它返回模組和相位的元組。cmath.polar()
#In polar coordinates, a complex number is defined by modulus r and phase angle phi.
#在極座標系中，複數由模量r和相位角φ定義。
#Syntax 語法
#cmath.polar(x)
#Parameter Values 參數值
#Parameter	Description
#x：Required. A number to find polar coordinates of
#必填。用於查找極座標的數位
#Technical Details 技術細節
#Return Value:	A value, representing polar coordinatestuple
#返回值：	表示極座標的值tuple
#Python Version:	2.6