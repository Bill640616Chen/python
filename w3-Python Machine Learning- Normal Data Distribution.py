#https://www.w3schools.com/python/python_ml_normal_data_distribution.asp
#Python Machine Learning - Normal Data Distribution 機器學習- 正常數據分佈
#Normal Data Distribution 正常數據分佈
#In the previous chapter we learned how to create a completely random array, of a given size, and between two given values.
#在前一章中，我們學會了如何創建一個完全隨機的陣列，一個給定的大小，以及兩個給定的值之間。
#In this chapter we will learn how to create an array where the values are concentrated around a given value.
#在本章中，我們將學習如何創建一個圍繞給定值的值集中值的陣列。
#In probability theory this kind of data distribution is known as the normal data distribution, or the Gaussian data distribution, after the mathematician Carl Friedrich Gauss who came up with the formula of this data distribution.
#在概率理論中，這種數據分佈被稱為正常數據分佈，或高斯數據分佈，僅次於數學家卡爾·弗里德里希·高斯，他提出了這種數據分佈的公式。
#A typical normal data distribution:
print("--------------------------------典型的正常數據分佈")
#典型的正常數據分佈：
import numpy
import matplotlib.pyplot as plt
x = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()
#Note: A normal distribution graph is also known as the bell curve because of it's characteristic shape of a bell.
#注意：正常分布圖也稱為鍾形曲線，因為它具有鍾的特徵形狀。

#Histogram Explained 直方圖解釋
#We use the array from the numpy.random.normal() method, with 100000 values,  to draw a histogram with 100 bars.
#我們使用 numpy.random.normal()方法的陣列，具有 100000 個值，繪製具有 100 條的直方圖。
#We specify that the mean value is 5.0, and the standard deviation is 1.0.
#我們指定平均值為 5.0，標準偏差為 1.0。
#Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.
#這意味著值應集中在5.0左右，並且很少遠離平均值1.0。
#And as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.
#正如你可以從直方圖中看到，大多數值在4.0到6.0之間，頂部在5.0左右。