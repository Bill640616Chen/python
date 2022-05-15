#https://www.w3schools.com/python/python_math.asp
#Python Math 數學
#Python has a set of built-in math functions, including 
# an extensive math module, that allows you to perform 
# mathematical tasks on numbers.
#Python 具有一套內建的數學功能，包括一個廣泛的數學模組，允許
# 您在數字上執行數學任務。
#Built-in Math Functions 內建的數學函數
print("--------min()和max()函數可用於找可迭中的最低值或最高值")
#The min() and max() functions can be used to find the lowest or highest value in an iterable:
#min()和max()函數可用於找可迭中的最低值或最高值：
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x) #5
print(y) #25

print("--------------------------------The abs() function")
#The abs() function : 絕對值的函數
#Return the absolute value of a number. The argument may 
# be an integer, a floating point number, or an object 
# implementing. If the argument is a complex number, its 
# magnitude is returned.
#傳回數字的絕對值。參數可能是整數、浮動點號或物件實現，如果
# 參數是一個複雜的數字，則返回其規模
x = abs(-7.25) #'絕對值'出來都是正數
print(x) #7.25
print("----------------------------------The pow(x, y, mod)")
#The pow(x, y) function returns the value of x to the power of y (xy).
#pow(x, y)函數傳回x值,傳回來的值是x的y次方
#Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
x = pow(4, 3)
print(x) #64
a = pow(38, -1, mod=97)
print(a) #23
#pow(x,y,z) 前面x的y次方算完後,%除以z後取餘數,mod是關鍵字,不能改
#Equivalent to base**exp with 2 arguments or base**exp % 
# mod with 3 arguments
#相當於base**exp 與 2 個參數或base**exp %除以 mod=n 3個參數
#pow(x,y,z)x是base,y是**exp,z是mod(除數)=n
#modulo與mod很相似,但不相同,modulo是取餘數
#Some types, such as ints, are able to use a more efficient 
# algorithm when invoked using the three argument form.
#某些類型（如 ints）能夠使用三種參數形式調用時使用更高效的演算法。

print("-----------------------------The Math Module 數學模組")
#The Math Module 數學模組
#Python has also a built-in module called math, which extends the list of mathematical functions.
#Python 還有一個內建模組，稱為數學，它擴展了數學函數清單。
#To use it, you must import the math module:
#要使用它，您必須導入數學模組：
import math
#When you have imported the math module, you can start 
# using methods and constants of the module.
#導入數學模組后，可以開始使用模組的方法和常數。
#The math.sqrt() method for example, returns the square 
# root of a number:
#例如，math.sqrt()方法傳回數字的平方根：
import math
x = math.sqrt(64)
print(x) #8.0
#sqrt()開平方根
print("-------------------------math.ceil()和math.floor()")
#The math.ceil() method rounds a number upwards to its 
# nearest integer, and the math.floor() method rounds a 
# number downwards to its nearest integer, and returns 
# the result:
#math.ceil()方法將數字向上轉到最接近的整數，math.floor()
# 方法將數位向下轉到最接近的整數，並返回結果：
import math
x = math.ceil(1.4)  #ceiling天花板的縮寫ceil
y = math.floor(1.4) #floor是地板
print(x) # returns 2
print(y) # returns 1

print("---------------------------------------The math.pi")
#The math.pi constant, returns the value of PI (3.14...):
#math.pi常數， 傳回 PI 值 （3.14...）：
import math
x = math.pi
print(x) #3.141592653589793