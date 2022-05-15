#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-----------------prod()傳回可迭代物件裡所有元素的乘積")
#https://www.w3schools.com/python/ref_math_prod.asp
#Python math.prod() Method prod()的方法
#Returns the product of all the elements in an iterable
#傳回可迭代物件裡所有元素的乘積
#Return the product of the elements from the given iterable:
#從給定的反覆運算器傳回元素的乘積
# Import math Library
import math
sequence = (2, 2, 2)
#Return the product of the elements
print(math.prod(sequence))
#Definition and Usage 定義和使用
#The math.prod() method returns the product of the elements from the given iterable.
#math.prod()方法返回給定反覆運算器中元素的乘積。
#Syntax
print("------------語法測試---math.prod(sequence,start= 2")
#math.prod(iterable, start=)
#Parameter Values
#Parameter：Description
#iterable：Required. Specifies the elements of the iterable
# whose product is computed by the function
#iterable：必需的參數， 指定由函數計算乘積的Iterable的元素
#start：Optional. Specifies the starting value of the product. 
# Default value is 1
#start：可選的。 指定產品的起始值。 預設值為1
#Technical Details
#Return Value:	The product of the elements from the iterable
#Python Version:	3.8
import math
sequence = (2, 2, 2,1,2,1)
print(math.prod(sequence,start= 2))
#start= 2,由3開始乘sequence,start=(寫法一定要有=)
