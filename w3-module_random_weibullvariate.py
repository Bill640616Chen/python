#Random weibullvariate() Method weibullvariate()方法
#基於 Weibull 分佈（用於統計學）返回 0 到 1 之間的隨機浮點數。
#威布爾分佈。 alpha是比例參數，beta是形狀參數。
#This article demonstrates how to use random.weibullvariate function . weibullvariate() is an inbuilt method of the random module. It is used to return a random floating point number with Weibull distribution.
#本文演示如何使用隨機.weibullvariate  函數 。  weibullvariate（）是隨機模組的內置方法。它用於傳回具有  Weibull 分佈的隨機浮點數
#Syntax : 語法：
#random.weibullvariate(alpha,beta)
#Parameter Values : 參數值 ：
#Parameter：Description
#alpha：Required.  It is a shape parameter.
#beta：Required. It is a shape parameter. 
#Return Value : 傳回值 ：
# random Weibull distribution floating number
#隨機威布爾分佈浮動數
#1.# import the random module 
import random 
# determining the values of the parameters 
alpha = 1
beta = 1.5
# using the weibullvariate() method 
print(random.weibullvariate(alpha,beta))

#2.We can generate the number multiple times and plot a graph to observe the Weibull distribution.
#我們可以多次生成該數位並繪製一個圖形來觀察Weibull分佈。
# import the required libraries 
import random 
import matplotlib.pyplot as plt 
# store the random numbers in a 
# list 
nums = [] 
alpha = 1
beta = 1.5
for i in range(100): 
    temp = random.weibullvariate(alpha, beta) 
    nums.append(temp) 
# plotting a graph 
plt.plot(nums) 
plt.show() 

#3.We can create a histogram to observe the density of the Weibull distribution.
#我們可以創建一個直方圖來觀察 Weibull 分佈的密度。
# import the required libraries 
import random 
import matplotlib.pyplot as plt 
# store the random numbers in a list 
nums = [] 
alpha = 1
beta = 1.5
for i in range(10000): 
    temp = random.weibullvariate(alpha, beta) 
    nums.append(temp) 
# plotting a graph 
plt.hist(nums, bins = 200) 
plt.show() 