#https://www.w3schools.com/python/ref_math_inf.asp
#Python Math Constants inf 數學常數正負無窮
#Constant   Description
#math.inf	Returns a floating-point positive infinity
#python中的正無窮或負無窮，使用float（"inf"）或float（"-inf"）來表示。
#這裡有點特殊，寫成：float（"inf"），float（"INF"）或者float（'Inf'）都是可以的。
#當涉及 > 和 < 比較時，所有數都比無窮小float（"-inf"）大，所有數都比無窮大float（"inf"）小。
#相等比較時，float（"+inf"）與float（"+inf"）、float（"inf"）三者相等
#Print the positive and negative infinity:
# Import math Library
import math
# Print the positive infinity
print (math.inf)
# Print the negative infinity
print (-math.inf)
#Definition and Usage
#The constant returns a floating-point positive infinity.math.inf
#For negative infinity, use .-math.inf
#The inf constant is equivalent to .float('inf')

#Syntax
math.inf
#Technical Details
#Return Value:	A value, representing the value of positive infinityfloat
#Python Version:	3.5
