#https://www.w3schools.com/python/python_ml_data_distribution.asp
#Python Machine Learning - Data Distribution 機器學習- 數據分佈
#Data Distribution 數據分佈
#Earlier in this tutorial we have worked with very small amounts of data in our examples, just to understand the different concepts.
#在本教程的早期，我們用非常少量的數據來理解不同的概念。
#In the real world, the data sets are much bigger, but it can be difficult to gather real world data, at least at an early stage of a project.
#在現實世界中，數據集要大得多，但收集真實世界的數據可能很困難，至少在專案的早期階段是這樣。
#How Can we Get Big Data Sets? 如何獲取大數據集合？
#To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.
#為了創建用於測試的大數據集，我們使用 Python 模組 NumPy，該模組附帶許多方法來創建任意大小的隨機數據集。
#Create an array containing 250 random floats between 0 and 5:
print("----------建立包含 0 到 5 之間的 250 個隨機浮子的陣列")
#建立包含 0 到 5 之間的 250 個隨機浮子的陣列：
import numpy
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)
#uniform 均勻分佈

print("----------------------------------Histogram 直方圖")
#Histogram 直方圖
#To visualize the data set we can draw a histogram with the data we collected.
#要可視化數據集，我們可以用我們收集的數據繪製直方圖。
#We will use the Python module Matplotlib to draw a histogram.
#我們將使用 Python 模組 Matplotlib 繪製直方圖。
#Learn about the Matplotlib module in our Matplotlib Tutorial.
#了解我們的Matplotlib教程中的Matplotlib模組。
print("-----------------------Draw a histogram: 繪製直方圖")
#Draw a histogram: 繪製直方圖：
import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(0.0, 5.0, 250)
plt.hist(x, 5)
plt.show()
#uniform 均勻分佈

print("---------------------Histogram Explained 直方圖解釋")
#Histogram Explained 直方圖解釋
#We use the array from the example above to draw a histogram with 5 bars.
#我們使用上面示例中的陣列繪製帶有 5 條的直方圖。
#The first bar represents how many values in the array are between 0 and 1.
#第一個條形表示陣列中的值數值在 0 到 1 之間。
#The second bar represents how many values are between 1 and 2.
#第二個條形表示 1 到 2 之間的值數。
#Etc.等等
#Which gives us this result:
#這給了我們這個結果：
#52 values are between 0 and 1
#48 values are between 1 and 2
#49 values are between 2 and 3
#51 values are between 3 and 4
#50 values are between 4 and 5
#Note: The array values are random numbers and will not show the exact same result on your computer.
#注意：陣列值是隨機數，不會在計算機上顯示完全相同的結果。

#Big Data Distributions 大數據分佈
#An array containing 250 values is not considered very big, but now you know how to create a random set of values, and by changing the parameters, you can create the data set as big as you want.
#包含 250 個值的陣列並不被認為是很大的，但現在您知道如何創建隨機的一組值，通過更改參數，您可以創建隨您想要的大數據集。
#Create an array with 100000 random numbers, and display them using a histogram with 100 bars:
print("---------------------建立具有 100000 個隨機數的陣列")
#建立具有 100000 個隨機數的陣列，並使用帶有 100 條條形圖的直方圖顯示它們：
import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()
#uniform 均勻分佈
