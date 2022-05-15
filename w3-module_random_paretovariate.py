#Random paretovariate() Method paretovariate()方法
#基於 Pareto 分佈（用於概率論）返回 0 到 1 之間的隨機浮點數。
#帕累托分佈。 alpha是形狀參數。
#This article demonstrates how to use random.paretovariate function . paretovariate() is an inbuilt method of the random module. It is used to return a random floating point number with Pareto distribution.
#本文演示如何使用隨機.paretovariate  函數 。  paretovariate（）是隨機模組的內置方法。它用於傳回具有帕累托分佈的隨機浮點數
#Syntax : 語法
#random.paretovariate(alpha)
#Parameter Values : 參數值 ：
#Parameter：Description
#alpha：Required.  It is a shape parameter.
#Return Value : 傳回值 ：
#a random Pareto distribution floating number
#隨機帕累托分佈浮點數
#1.import the random module 
import random 
# determining the values of the parameter 
alpha = 3
# using the paretovariate() method 
print(random.paretovariate(alpha)) 
#Output : 
#1.5139483121308261

#2.We can generate the number multiple times and plot a graph to observe the Pareto distribution.
#我們可以多次生成該數位並繪製一個圖形來觀察帕累托分佈。
# import the required libraries 
import random 
import matplotlib.pyplot as plt 
# store the random numbers in a 
# list 
nums = [] 
alpha = 3
for i in range(100): 
    temp = random.paretovariate(alpha) 
    nums.append(temp) 
# plotting a graph 
plt.plot(nums) 
plt.show()

#3.We can create a histogram to observe the density of the Pareto distribution.
#我們可以創建一個直方圖來觀察帕累托分佈的密度。
# import the required libraries 
import random 
import matplotlib.pyplot as plt 
# store the random numbers in a 
# list 
nums = [] 
alpha = 3
for i in range(100): 
    temp = random.paretovariate(alpha) 
    nums.append(temp) 
# plotting a graph 
plt.plot(nums) 
plt.show() 