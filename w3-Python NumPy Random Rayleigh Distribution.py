#https://www.w3schools.com/python/numpy/numpy_random_rayleigh.asp
#Random Rayleigh Distribution 瑞利分佈
#當一個隨機二維向量的兩個分量呈獨立的、均值為0，有著相同的方差的
# 正態分佈時，這個向量的模呈瑞利分佈。
#Rayleigh distribution is used in signal processing.
#雷利分佈用於信號處理,無線網路
#It has two parameters:
#它有兩個參數：
#scale - (standard deviation) decides how flat the distribution will be default 1.0).
#scale - （標準偏差） 決定分配的平面值預設值 1.0）。
#size - The shape of the returned array.
#傳回陣列的形狀。
print("-------------------rayleigh(scale=2, size=(2, 3))")
#Draw out a sample for rayleigh distribution with scale of 2 with size 2x3:
#繪製大小為 2x3 的 2 級雷利分佈樣本：
from numpy import random
x = random.rayleigh(scale=2, size=(2, 3))
#size=(2, 3),()可以N維
print(x)

print("--------------rayleigh(size=1000)可視化雷利分佈")
#Visualization of Rayleigh Distribution
#可視化雷利分佈
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()

print("----------------------雷利和卡方分佈的相似性")
#Similarity Between Rayleigh and Chi Square Distribution
#雷利和卡方分佈的相似性
#At unit stddev the and 2 degrees of freedom rayleigh and chi square represent the same distributions.
#在單位 標準差 和 2 度的自由雷利和奇方代表相同的分佈。
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.chisquare(df=2, size=1000), hist=False)
sns.distplot(random.rayleigh(scale=2, size=1000), hist=False)
plt.show()