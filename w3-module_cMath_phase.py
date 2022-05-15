#https://www.w3schools.com/python/ref_cmath_phase.asp
#Python cmath.phase() Method
#Find the phase of a complex number:
#尋找複數的相位：
#Import cmath Library
import cmath
#print phase of some given parameters
print (cmath.phase(2 + 3j))
#Definition and Usage 定義和用法
#The cmath.phase() method returns the phase of a complex number.
#該方法返回複數的相位。cmath.phase()
#A complx number can be expressed in terms of its magnitude and angle. This angle is between vector (representing complex number) and positive x-axis is called Phase.
#康普數可以用其幅度和角度來表示。此角度介於向量（表示複數）和正 x 軸之間，稱為相位。
#Note: Output is always between -π and π.
#注意：輸出始終介於 -π 和 π 之間。
#Syntax 語法
#cmath.phase(x)
#Parameter Values 參數值
#Parameter	Description
#x：Required. The number to find the phase of
#必填。要查找的相位數
#Technical Details 技術細節
#Return Value:	A float value, representing the phase of a complex number
#返回值：	值，表示複數的相位float
#Python Version:	2.6

