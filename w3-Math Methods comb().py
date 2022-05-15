#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("--------------comb(n, k))(如何計算?n! / (k! *(n-k)!)")
#https://www.w3schools.com/python/ref_math_comb.asp
#Python math.comb() Method comb()的方法
#Returns the number of ways to choose k items from n items without repetition and order
#用於獲取從n個項目中選擇k個項目(不重復且無順序)的方法數量
#Find the total number of possibilities to choose k things from n items:
#尋找從 n 項目中選擇 k 項目的可能性總數：
# Import math Library
import math
# Initialize the number of items to choose from
n = 7
# Initialize the number of possibilities to choose
k = 5
# Print total number of possible combinations
print (math.comb(n, k)) #21
#如何計算?n! / (k! *(n-k)!)
#n=1*2*3*4*5*6*7,k=1*2*3*4*5,n-k=2,1*2
#1*2*3*4*5*6*7/1*2*3*4*5*2=21
#Definition and Usage 定義和使用
#The math.comb() method returns the number of ways picking
# k unordered outcomes from n possibilities, without 
# repetition, also known as combinations.
#Note: The parameters passed in this method must be 
# positive integers.
#參數必項為正整數
#Syntax 語法
#math.comb(n, k)
#如果k>n,輸出是0
#Parameter Values
#Parameter：Description
#n：Required. Positive integers of items to choose from
#k：Required. Positive integers of items to choose
#Note: If the value of k is greater than the value of n 
# it will return 0 as a result.
#Note: If the parameters are negative, a ValueError occurs. 
# If the parameters are not integers, a TypeError occurs.
#參數不能是負數,會發生錯誤
#Technical Details
#Return Value:	An int value, representing the total number
# of combinations
#Python Version:	3.8

