#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("----------------------fsum()傳回任何可迭代的項目總和")
#https://www.w3schools.com/python/ref_math_fsum.asp
#Python math.fsum() Method fsum()的方法
#Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
#傳回任何可迭代的項目總和(tuples, arrays, lists, etc.)
#Return the sum of all items:
# Import math Library
import math
# Print the sum of all items
print(math.fsum([1, 2, 3, 4, 5]))
print(math.fsum([100, 400, 340, 500]))
print(math.fsum([1.7, 0.3, 1.5, 4.5]))
#Definition and Usage 定義和使用
#The math.fsum() method returns the sum of all items in any iterable (tuples, arrays, lists, etc.).
#Syntax
#math.fsum(iterable)
#Parameter Values
#Parameter	Description
#iterable	Required. The list, tuple, array to sum. If the iterable is not numbers, it returns a TypeError
#Technical Details
#Return Value:	A float value, representing the sum of all items in the iterable
#Python Version:	2.6
print("-----------------測試-fsum()傳回任何可迭代的項目總和")
import math
# Print the sum of all items
a = [1, 2, 3, 4, 5]
b = [100, 400, 340, 500]
c = [1.7, 0.3, 1.5, 4.5]
print(math.fsum(a))
print(math.fsum(b))
print(math.fsum(c))