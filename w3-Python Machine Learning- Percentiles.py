#https://www.w3schools.com/python/python_ml_percentile.asp
#Python Machine Learning - Percentiles 機器學習- 百分比
#What are Percentiles?什麼是百分位？
#Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
#百分比用於統計，用於為您提供描述給定百分比低於該值的值的數位。
#Example: Let's say we have an array of the ages of all the people that lives in a street.
#例如：假設我們有一系列生活在街道上的所有人的年齡。
#ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
#What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.
#什麼是75。百分比？答案是43，這意味著75%的人是43歲或以下。
#The NumPy module has a method for finding the specified percentile:
#NumPy 模組具有查找指定百分位的方法：
#Use the NumPy percentile() method to find the percentiles:
print("----------------使用 NumPy percentile()方法查找百分比")
#使用 NumPy percentile()方法查找百分比：
import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75) #21*75%=15.75,第16個
print(x)
#What is the age that 90% of the people are younger than?
#90% 的人比什麼年齡還小？
import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 90)
print(x)
#percentile(ages, 90),90代表90%,21*90%=18.9,第19個