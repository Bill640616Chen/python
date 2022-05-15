#https://www.w3schools.com/python/numpy/numpy_random_exponential.asp
#Random Exponential Distribution 指數分佈
#把二元分佈公式推廣至多種狀態，就得到了多元分佈。
#Exponential Distribution 指數分佈
#Exponential distribution is used for describing time till next event e.g. failure/success etc.
#指數分佈用於描述下一個事件之前的時間，例如失敗/成功等。
#它有二個參數：
#scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
#scale - 相反的概率。(表示正態分佈的標準差，預設為1)
#size - The shape of the returned array.
#size - 傳回陣列的形狀。(表示生成隨機數的數量)
print("-------------------Exponential(scale=2, size=(2, 3))")
#Draw out a sample for exponential distribution with 2.0 scale with 2x3 size:
#繪製具有 2.0 比例的指數分佈示例，具有 2x3 大小：
from numpy import random
x = random.exponential(scale=2, size=(2, 3))
print(x)

print("-------------------Exponential(size=1000)可視化指數分佈")
#Visualization of Exponential Distribution
#可視化指數分佈
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.poisson(size=1000), hist=False)
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()

#Relation Between Poisson and Exponential Distribution
#Poisson與指數分佈之間的關係
#Poisson distribution deals with number of occurences of 
# an event in a time period whereas exponential distribution 
# deals with the time between these events.
#Poisson 分佈處理一段時間內事件的發生次數，而指數分佈則處理這些
# 事件之間的時間。