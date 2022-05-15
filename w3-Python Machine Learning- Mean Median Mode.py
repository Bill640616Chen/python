#https://www.w3schools.com/python/python_ml_mean_median_mode.asp
#Python Machine Learning - Mean Median Mode 機器學習- 平均中位數模式
#Mean, Median, and Mode 平均值、中位數和模式
#What can we learn from looking at a group of numbers?
#從一組數字中我們可以學到什麼？
#In Machine Learning (and in mathematics) there are often three values that interests us:
#在機器學習（和數學）中，我們通常有三個值感興趣：
#Mean - The average value    平均值 - 平均值
#Median - The mid point value中位數 - 中點值
#Mode - The most common value模式 - 最常見的值
#Example: We have registered the speed of 13 cars:
#示例：我們已經註冊了 13 輛車的速度：
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#What is the average, the middle, or the most common speed value?
#什麼是平均值、中間值或最常見的速度值？

#Mean 平均值
#The mean value is the average value.
#平均值是平均值。
#To calculate the mean, find the sum of all values, and divide the sum by the number of values:
#要計算平均值，請查找所有值的總和，並將總和除以值數：
#(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77
#The NumPy module has a method for this. Learn about the NumPy module in our NumPy Tutorial.
#NumPy 模組有此方法。了解我們的 NumPy 教程中的 NumPy 模組。
#Use the NumPy mean() method to find the average speed:
print("------------------使用 NumPy mean()方法尋找平均速度")
#使用 NumPy 平均值 （） 方法尋找平均速度：
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)

#Median 中位數
#The median value is the value in the middle, after you have sorted all the values:
#中值是中間值，在您對所有值進行排序後：
#77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111
#It is important that the numbers are sorted before you can find the median.
#在找到中位數之前，對數字進行排序非常重要。
#The NumPy module has a method for this:
#NumPy 模組對此有一種方法：
#Use the NumPy median() method to find the middle value:
print("------------------使用 NumPy median() 方法尋找中間值")
#使用 NumPy median() 方法尋找中間值：
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)
#If there are two numbers in the middle, divide the sum of those numbers by two.
#如果中間有兩個數位，則將這些數位的總和除以兩個。
#77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103
#(86 + 87) / 2 = 86.5(12個數字/2,就第6個跟第7個相加除以2)

#Mode 模式值
#The Mode value is the value that appears the most number of times:
#模式值是顯示次數最多的值：
#99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86
#The SciPy module has a method for this. Learn about the SciPy module in our SciPy Tutorial.
#SciPy 模組對此有一種方法。了解我們「SciPy教程」中的「SciPy」模組。
#Use the SciPy mode() method to find the number that appears the most:
print("-------------使用 NumPy mode() 方法尋找顯示最多的數位")
#使用 SciPy mode() 方法尋找顯示最多的數位：
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)

#Chapter Summary 章節摘要
#The Mean, Median, and Mode are techniques that are often used in Machine Learning, so it is important to understand the concept behind them.
#平均、中位數和模式是機器學習中常用的技術，因此瞭解它們背後的概念非常重要。