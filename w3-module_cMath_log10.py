#https://www.w3schools.com/python/ref_cmath_log10.asp
#Python cmath.log10() Method
#Find the base-10 logarithm of a complex number:
#求出複數的以 10 為底數的對數：
#Import cmath Library
import cmath
#print base-10 log value of complex numbers
print (cmath.log10(2+ 3j))
print (cmath.log10(1+ 2j))
#Definition and Usage 定義和用法
#The cmath.log10() method returns the base-10 logarithm of a complex number.
#該方法返回複數的以10為底的對數。cmath.log10()
#There is one branch cut, from 0 along the negative real axis to -∞, continuous from above.
#有一個分支切口，從0沿負實軸到-∞，從上面連續。
#Syntax 語法
#cmath.log10(x)
#Parameter Values 參數值
#Parameter	Description
#x：Required. Specifies the value to calculate the base-10 logarithm for. If the value is 0 or a negative number, it returns a ValueError. If the value is not a number, it returns a TypeError
#必填。指定要為其計算以 10 為底數的值。如果值為 0 或負數，則返回 ValueError。如果該值不是數位，則返回 TypeError
#Technical Details 技術細節
#Return Value:	A complex value, representing the base-10 logarithm of a number
#返回值：	一個值，表示數位的以10為底的對數complex
#Python Version:	1.5