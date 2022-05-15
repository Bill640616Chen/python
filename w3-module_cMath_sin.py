#https://www.w3schools.com/python/ref_cmath_sin.asp
#Python cmath.rect() Method
#Convert polar coordinates to rectangular form:
#將極座標轉換為矩形：
#import cmath for complex number operations
import cmath
#convert a polar coordinate to rectangular form
print(cmath.rect(3.1622776601683795, 1.2490457723982544))
#Definition and Usage 定義和用法
#The method converts polar coordinates to rectangular form of the complex number. It creates a complex number with phase and modulus.cmath.rect()
#該方法將極座標轉換為複數的矩形形式。它創建一個具有相位和模量的複數。cmath.rect()
#This method is equivalent to .r * (math.cos(phi) + math.sin(phi)*1j)
#此方法等效於 。r * (math.cos(phi) + math.sin(phi)*1j)
#Note: The radius r is the length of the vector, and phi (phase angle) is the angle made with the real axis.
#注意：半徑r是向量的長度，phi（相位角）是用實軸形成的角度。
#Syntax 語法
#cmath.rect(r, phi)
#Parameter Values 參數值
#Parameter	Description
#r：Required. Represents the modulus of a complex number
#必填。表示複數的模量
#phi：Required. Represents the phase of a complex number
#必填。表示複數的相位
#Technical Details 技術細節
#Return Value:	A value, representing the rectangular form of a complex numbercomplex
#返回值：	值，表示複數的矩形形式complex
#Python Version:	2.6

