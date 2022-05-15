#https://www.w3schools.com/python/module_math.asp
#Python Math Methods 數學方法
#Python math Module 數學模組
#Python has a built-in module that you can use for mathematical tasks.
#Python 有一個內建模組，可用於數學任務。
#The math module has a set of methods and constants.
#數學模組有一套方法和常數。

print("----perm()返回有序，無重複地從n個項中選擇k個項的方式數")
#https://www.w3schools.com/python/ref_math_perm.asp
#Python math.perm() Method perm()的方法
#Returns the number of ways to choose k items from n items
# with order and without repetition
#返回有序，無重複地從n個項中選擇k個項的方式數
#Find the number of ways to choose k things from n items:
#找到從n個項目中選擇k個事物的方法數量：結果將是：
# Import math Library
import math
# Initialize the number of items to choose from
n = 7
# Initialize the number of items to choose
k = 5
# Print the number of ways to choose k items from n items
print (math.perm(n, k)) #2520
#Evaluates to n! / (n - k)! when k <= n 
# and evaluates to zero when k > n.
#Definition and Usage 定義和使用
#The math.perm() method returns the number of ways to 
# choose k items from n items with order and without 
# repetition.
#math.perm（）方法返回從n個項中選擇有序且無重複的k個項的方式數量。
#Note: The k parameter is optional. If we do not provide 
# one, this method will return n! (for example, 
# math.perm(7) will return 5040).
#注意： k參數是可選的。 如果我們不提供一個，這個方法將返回n！ 
# （例如，將返回）。math.perm(7)5040
#Syntax
#math.perm(n, k)
#Parameter Values
#Parameter：Description
#n：Required. Positive integers of items to choose from
#必需的參數， 正整數專案可供選擇
#k：Optional. Positive integers of items to choose
#可選的。 正整數專案可供選擇
#Note: If k is greater than n, it returns 0.
#注意：如果k大於n，則返回0。 
#Note: If n or k are negative, a ValueError occurs. 
# If n or k  are not integers, a TypeError occurs.
#注意：如果n或k為負，則發生ValueError。 
# 如果n或k不是整數，則會發生TypeError。
#Technical Details
#Return Value:	An int value, representing the number of ways to choose k items from n items with order and without repetition
#Python Version:	3.8

