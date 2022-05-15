#https://www.w3schools.com/python/numpy/numpy_random_pareto.asp
#Random Pareto Distribution 帕雷托分佈
#帕累托分佈屬於連續概率分佈。 "齊夫定律"， 也稱為"zeta 
# 分佈"， 也可以被認為是在離散概率分佈中的帕累托分佈。 
# 一個遵守帕累托分佈的隨機變數的期望值為 （如果 期望值
# 為無窮大） 且隨機變數的標準差為 （如果 標準差不存在）
#A distribution following Pareto's law i.e. 80-20 
# distribution (20% factors cause 80% outcome).
#遵循帕雷托法律的分佈，即 80-20 分配（20% 因數導致 
# 80% 的結果）。
#It has two parameter:
#它有兩個參數：
#a - shape parameter.
#a - 形狀參數.
#size - The shape of the returned array.
#size - 傳回陣列的形狀。
print("-----------------------pareto(a=2, size=(2, 3))")
#Draw out a sample for pareto distribution with shape of 2 with size 2x3:
#繪製一個樣本，用於大小為 2x3 的 2 形的帕雷托分佈：
from numpy import random
x = random.pareto(a=2, size=(2, 3))
print(x)

print("--------------rayleigh(size=1000)可視化雷利分佈")
#Visualization of Pareto Distribution
#可視化帕雷托分佈
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()

print("------------------帕雷托,雷利和卡方分佈的相似性")
#Similarity Between Rayleigh and Chi Square Distribution
#雷利和卡方分佈的相似性
#At unit stddev the and 2 degrees of freedom rayleigh and chi square represent the same distributions.
#在單位 標準差 和 2 度的自由雷利和奇廣場代表相同的分佈。
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.pareto(a=2, size=1000), hist=False, label='par')
sns.distplot(random.rayleigh(scale=2, size=1000), hist=False, label='ray')
sns.distplot(random.chisquare(df=2, size=1000), hist=False, label='chi')
plt.legend() #把標籤印出來
plt.show()
