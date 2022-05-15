#https://www.w3schools.com/python/numpy/numpy_random_chisquare.asp
#Random Chi Square Distribution 卡方分佈
#若n個相互獨立的隨機變數ξ₁，ξ₂,...,ξn ，均服從標準正態分佈（也稱
# 獨立同分佈於標準正態分佈），則這n個服從標準正態分佈的隨機變數的
# 平方和構成一新的隨機變數
#Chi Square distribution is used as a basis to verify the hypothesis.
#卡方分佈為驗證假說的基礎。
#It has two parameters:
#它有兩個參數：
#df - (degree of freedom).
#df - （自由度） 。
#size - The shape of the returned array.
#size - 傳回陣列的形狀。
print("-------------------chisquare(df=2, size=(2, 3)")
#Draw out a sample for chi squared distribution with degree of freedom 2 with size 2x3:
#繪製具有 2x3 大小的自由度 2 的卡方分佈範例：
from numpy import random
x = random.chisquare(df=2, size=(2, 3))
#size=(2, 3),()可以N維
print(x)

print("------------chisquare(df=1, size=1000)可視化卡方分佈")
#Visualization of Chi Square Distribution
#可視化卡方分佈
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()
