#https://www.w3schools.com/python/python_ml_standard_deviation.asp
#Python Machine Learning - Standard Deviation 機器學習- 標準差
#What is Standard Deviation? 什麼是標準偏差？
#Standard deviation is a number that describes how spread out the values are.
#標準偏差是描述值分佈程度的數位。
#A low standard deviation means that most of the numbers are close to the mean (average) value.
#低標準偏差意味著大多數數位接近平均值（平均值）。
#A high standard deviation means that the values are spread out over a wider range.
#高標準偏差意味著值分佈在更廣泛的範圍內。
#Example: This time we have registered the speed of 7 cars:
#示例：這次我們註冊了 7 輛車的速度：
#speed = [86,87,88,86,87,85,86]
#The standard deviation is:
#標準偏差為：0.9
#Meaning that most of the values are within the range of 0.9 from the mean value, which is 86.4.
#這意味著大多數值在 0.9 範圍內，從平均值，這是 86.4。
#Let us do the same with a selection of numbers with a wider range:
#讓我們對範圍更廣的數字進行選擇：
#speed = [32,111,138,28,59,77,97]
#The standard deviation is:
#標準偏差為：37.85
#Meaning that most of the values are within the range of 37.85 from the mean value, which is 77.4.
#這意味著大多數值在平均值 37.85 範圍內，即 77.4。
#As you can see, a higher standard deviation indicates that the values are spread out over a wider range.
#正如您所看到的，較高的標準偏差表示值分佈在更廣泛的範圍內。
#The NumPy module has a method to calculate the standard deviation:
#NumPy 模組具有計算標準偏差的方法：
#Use the NumPy std() method to find the standard deviation:
print("----------------使用 NumPy std() 方法查找標準偏差")
#使用 NumPy std() 方法查找標準偏差：
import numpy
speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)
import numpy
speed = [32,111,138,28,59,77,97]
x = numpy.std(speed)
print(x)

print("------------------使用 NumPy var() Variance 方差")
#Variance 方差
#Variance is another number that indicates how spread out the values are.
#方差是另一個數位，表示值的分佈程度。
#In fact, if you take the square root of the variance, you get the standard deviation!
#事實上，如果你採取方根的方差，你得到的標準偏差！
#Or the other way around, if you multiply the standard deviation by itself, you get the variance!
#或者相反，如果你把標準偏差乘以它自己，你就會得到差異！
#To calculate the variance you have to do as follows:
#要計算方差，您必須按以下要求進行計算：
#1. Find the mean:
#1. 找到平均值：
#(32+111+138+28+59+77+97) / 7 = 77.4
#2. For each value: find the difference from the mean:
#2. 對於每個值：查找與平均值的差異：
# 32 - 77.4 = -45.4
#111 - 77.4 =  33.6
#138 - 77.4 =  60.6
# 28 - 77.4 = -49.4
# 59 - 77.4 = -18.4
# 77 - 77.4 = - 0.4
# 97 - 77.4 =  19.6
#3. For each difference: find the square value:
#3. 對於每個差異：尋找方值：
#(-45.4)2 = 2061.16
# (33.6)2 = 1128.96
# (60.6)2 = 3672.36
#(-49.4)2 = 2440.36
#(-18.4)2 =  338.56
#(- 0.4)2 =    0.16
# (19.6)2 =  384.16
#4. The variance is the average number of these squared differences:
#4. 方差是這些方形差異的平均數：
#(2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2
#Luckily, NumPy has a method to calculate the variance:
#幸運的是，NumPy 有一種方法來計算方差：
#Use the NumPy var() method to find the variance:
#使用 NumPy var()方法查找方差：
import numpy
speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x)

print("----------------使用 NumPy std() std 標準差")
#Standard Deviation 標準差
#As we have learned, the formula to find the standard deviation is the square root of the variance:
#正如我們所瞭解到的，找到標準偏差的公式是方形差異的方根：
#√1432.25 = 37.85
#Or, as in the example from before, use the NumPy to calculate the standard deviation:
#或者，與之前的示例一樣，使用 NumPy 計算標準偏差：
#Use the NumPy std() method to find the standard deviation:
#使用 NumPy std() 方法查找標準偏差：
import numpy
speed = [32,111,138,28,59,77,97]
x = numpy.std(speed)
print(x)

#Symbols 符號
#Standard Deviation is often represented by the symbol Sigma: σ
#標準偏差通常由符號西格瑪表示：σ
#Variance is often represented by the symbol Sigma Square: σ2
#方差通常由符號西格瑪廣場表示： σ2變異數「平方和的平均」減去「平均的平方」
#Chapter Summary 章節摘要
#The Standard Deviation and Variance are terms that are often used in Machine Learning, so it is important to understand how to get them, and the concept behind them.
#標準偏差和方差是機器學習中常用的術語，因此瞭解如何獲取它們以及它們背後的概念非常重要。


