#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------------log()找不同數字的自然對數")
#https://www.w3schools.com/python/ref_math_log.asp
#Python math.log() Method log()的方法
#Returns the natural logarithm of a number, or the 
# logarithm of number to base
#傳回自然的對數數字,或對數到基數
#Find the natural logarithm of different numbers
#找不同數字的自然對數
# Import math Library
import math
# Return the natural logarithm of different numbers
#傳回不同數字的自然對數
print(math.log(2.7183))
print(math.log(2))
print(math.log(1))
print(math.log(math.pi))
print(math.log(10,2))
print(math.log(8,2))
#log2(2為底數)8(以2為底的3的對數)=3
#Definition and Usage 定義和使用
#The math.log() method returns the natural logarithm of a number, or the logarithm of number to base.
#math.log()方法返回數字的自然對數，或數字以對數為底的對數。
#Syntax
#math.log(x, base)
#x稱做以base為底的傳回值的對數
#英語名詞：logarithms。如果'base'b='x'，那麼log'base''x'=b
#其中，base叫做“底數”，n叫做“真數”，x叫做“以base為底的n的對數”。
# logan=b函數叫做對數函數。對數函數中n的定義域是n>0，零和負數
# 沒有對數；base的定義域是base>0且base≠1。
#Parameter Values
#Parameter：Description
#x：Required. Specifies the value to calculate the logarithm
# for. If the value is 0 or a negative number, it returns
# a ValueError. If the value is not a number, it returns a 
# TypeError
#必需的參數， 指定要為其計算對數的值。
#如果值為0或負數，則返回ValueError。
#如果該值不是數字，則返回TypeError
#base：Optional. The logarithmic base to use. Default is 'e'
#可選的。 使用的對數底數。 默認為"e"
#Technical Details
##Return Value:	A float value, representing the natural logarithm of a number, or the logarithm of number to base
#Python Version:	Changed in version 2.3
#Change Log:	The base parameter was added

