#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("-------------------dist()找一維和二維點之間的歐幾里德距離")
#https://www.w3schools.com/python/ref_math_dist.asp
#Python math.dist() Method dist()的方法
#Returns the Euclidean distance between two points (p and q), 
# where p and q are the coordinates of that point
#從兩點之間p和q傳回歐幾里得距離,p 和 q 是該點的座標
#Find the Euclidean distance between one and two dimensional points:
#找一維和二維點之間的歐幾里德距離：
# Import math Library
import math
p = [3]
q = [1]
# Calculate Euclidean distance
#計算歐氏距離
print("-------------------------------------------測試-1")
print (math.dist(p, q))
p = [3, 3]
q = [6, 12]
# Calculate Euclidean distance
#計算歐氏距離
print (math.dist(p, q))
#Definition and Usage 定義和使用
#The math.dist() method returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point.
#Note: The two points (p and q) must be of the same dimensions.
#p和q兩個間必須是相同維度
print("-------------------------------------------測試-2")
import math
p = [3, 9, 7, 2, 4, 5, 7, 8, 10] #9個數字
q = [-5, -3, -9, 0, 6, 2, -1, 3, 5] #9個數字
# Calculate Euclidean distance
print (math.dist(p, q))
#p和q的個數必須要相同
#Syntax 語法
#math.dist(p, q)
#Parameter Values
#Parameter：Description
#p：Required. Specifies point 1
#q：Required. Specifies point 2
#Technical Details
#Return Value:	A float value, representing the Euclidean distance between p and q
#Python Version:	3.8
