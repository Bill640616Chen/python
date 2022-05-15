#https://www.w3schools.com/python/python_ml_scatterplot.asp
#Python Machine Learning - Scatter Plot 機器學習- 散佈圖
#Scatter Plot 散佈圖
#A scatter plot is a diagram where each value in the data set is represented by a dot.
#散射圖是數據集中每個值由點表示的圖表。
#The Matplotlib module has a method for drawing scatter plots, it needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis:
#Matplotlib 模組具有繪製散射圖的方法，它需要兩個長度相同的陣列，一個用於 x 軸的值，另一個用於 y 軸的值：
#x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
#y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#The x array represents the age of each car.
#x 陣列表示每輛車的年齡。
#The y array represents the speed of each car.
#y 陣列表示每輛車的速度。
#Use the scatter() method to draw a scatter plot diagram:
print("----------------------使用scatter()方法繪製散射圖")
#使用scatter()方法繪製散射圖圖：
import matplotlib.pyplot as plt
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x, y)
plt.show()

#Scatter Plot Explained散佈圖解釋
#The x-axis represents ages, and the y-axis represents speeds.
#x 軸表示年齡，y 軸表示速度。
#What we can read from the diagram is that the two fastest cars were both 2 years old, and the slowest car was 12 years old.
#從圖表中我們可以讀到的是，兩輛最快的車都是2歲，最慢的車是12歲。
#Note: It seems that the newer the car, the faster it drives, but that could be a coincidence, after all we only registered 13 cars.
#注意：似乎汽車越新，開得越快，但這可能是巧合，畢竟我們只註冊了13輛車。

#Random Data Distributions 隨機數據分佈
#In Machine Learning the data sets can contain thousands-, or even millions, of values.
#在機器學習中，數據集可以包含數千甚至數百萬個值。
#You might not have real world data when you are testing an algorithm, you might have to use randomly generated values.
#在測試演算法時，您可能沒有真實世界的數據，您可能必須使用隨機生成的值。
#As we have learned in the previous chapter, the NumPy module can help us with that!
#正如我們在上一章中學到的，NumPy 模組可以幫助我們！
#Let us create two arrays that are both filled with 1000 random numbers from a normal data distribution.
#讓我們創建兩個陣列，兩個陣列都充滿了來自正常數據分佈的1000個隨機數位。
#The first array will have the mean set to 5.0 with a standard deviation of 1.0.
#第一個陣列的平均值設置為5.0，標準偏差為1.0。
#The second array will have the mean set to 10.0 with a standard deviation of 2.0:
#第二個陣列的平均值設置為 10.0，標準偏差為 2.0：
#A scatter plot with 1000 dots:
print("------------------------------具有 1000 點的散射圖")
#具有 1000 點的散射圖：
import numpy
import matplotlib.pyplot as plt
x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)
plt.show()
#normal(平均值,標準差,量)

#Scatter Plot Explained 散佈圖解釋
#We can see that the dots are concentrated around the value 5 on the x-axis, and 10 on the y-axis.
#我們可以看到，這些點集中在 x 軸上的值 5 和 y 軸上的 10 值周圍。
#We can also see that the spread is wider on the y-axis than on the x-axis.
#我們還可以看到，y 軸上的點差比 x 軸的點差更大。