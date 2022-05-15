#https://www.w3schools.com/python/numpy/numpy_random_normal.asp
#Random Normal (Gaussian) Distribution 隨機資料視覺化(以圖表顯示)
#Normal Distribution 正態分佈
#The Normal Distribution is one of the most important distributions.
#正常分佈是最重要的分佈之一。
#It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.
#在德國數學家卡爾弗裡德里希高斯後,它也被稱為高斯分佈。
#It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
#它符合許多事件的概率分佈，例如。智商分數、心跳等。
#Use the random.normal() method to get a Normal Data Distribution.
#使用隨機.正常（）方法獲取正常數據分佈。
#It has three parameters:
#它有三個參數：
#loc - (Mean) where the peak of the bell exists.
#loc - （平均） 鐘峰存在的地方。(表示正態分佈的均值)
#scale - (Standard Deviation) how flat the graph distribution should be.
#scale - （標準差） 圖形分佈應有多平。(表示正態分佈的標準差，預設為1)
#size - The shape of the returned array.
#size - 傳回陣列的形狀。(表示生成隨機數的數量)

print("------------------------------normal(size=(2, 3))")
#Generate a random normal distribution of size 2x3:
#產生大小 2x3 的隨機正常分佈：
from numpy import random
x = random.normal(size=(2, 3))
print(x)
#size=(2, 3),輸出2維陣列,每個陣列有3個元素
print("--------------------測試1-----normal(1000)")
from numpy import random
x = random.normal(1000)
print(x)
print("--------------------測試2-----normal(size=1000)")
from numpy import random
x = random.normal(size=1000)
print(x)
print("---------------normal(loc=1, scale=2, size=(2, 3))")
#Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
#生成大小 2x3 的隨機正常分佈，平均值為 1，標準偏差為 2：
from numpy import random
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)
print("--圖表(random.normal(loc=1, scale=2, size=(2, 3)))")
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)
sns.distplot(x)
plt.show()
print("-----distplot(random.normal(size=1000), hist=False)")
#Visualization of Normal Distribution
#正常分佈的可視化
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(size=1000), hist=False)
plt.show()
#Note: The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve.
#注意：由於鍾形曲線，正常分佈的曲線也稱為鍾形曲線。
