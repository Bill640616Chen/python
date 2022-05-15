#https://www.w3schools.com/python/ref_cmath_log.asp
#Python cmath.log() Method
#Find the logarithm of a complex value:
#求出複數值的對數：
#Import cmath Library
import cmath
#print log value of some given parameters
print (cmath.log(1+ 1j))
print (cmath.log(1, 2.5))
#Definition and Usage 定義和用法
#The cmath.log() method returns the logarithm of a complex value.
#該方法返回複數值的對數。cmath.log()
#With a single argument, this method returns the natural logarithm of that argument with base e.
#對於單個參數，此方法返回該參數的自然對數，其基數為 e。
#With two arguments, this method returns the logarithm of the first argument (x) with the base of the second argument (base).
#對於兩個參數，此方法返回第一個參數 （x） 的對數，並以第二個參數 （base） 的基數為基數。
#Syntax 語法
#cmath.log(x, base)
#Parameter Values 參數值
#Parameter：Description
#x：Required. Specifies the value to calculate the logarithm for. If the value is 0 or a negative number, it returns a ValueError. If the value is not a number, it returns a TypeError
#必填。指定要計算其對數的值。如果值為 0 或負數，則返回 ValueError。如果該值不是數位，則返回 TypeError
#base：Optional. The logarithmic base to use. Default is 'e'
#自選。要使用的對數底數。默認值為"e"
#Technical Details 技術細節
#Return Value:：A complex value, representing the natural logarithm of a number, or the logarithm of number to base
#返回值：	一個值，表示數位的自然對數，或數位到基數的對數complex
#Python Version:：Changed in version 2.4
#Python 版本：	在版本 2.4 中更改
#Python Changelog:：The base parameter was added
#Python Changelog：	添加了基本參數
