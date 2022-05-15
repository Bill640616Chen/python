#https://www.w3schools.com/python/numpy/numpy_random_binomial.asp
#Random Binomial Distribution 二元分佈
#Binomial Distribution 二元分佈
#Binomial Distribution is a Discrete Distribution.
#二元分佈是一種離散分佈。
#It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
#它描述了二元場景的結果，例如擲硬幣，它要麼是頭部，要麼是尾部。
#It has three parameters:
#它有三個參數：
#n - number of trials.
#n - 試驗次數。在x軸呈現
#p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
#p - 每次試驗發生的可能性（例如擲硬幣的概率，每個概率為0.5）。
#size - The shape of the returned array.
#size - 傳回陣列的形狀,試驗數據的數量,在y軸呈現
#Discrete Distribution:The distribution is defined at separate 
# set of events, e.g. a coin toss's result is discrete as it 
# can be only head or tails whereas height of people is 
# continuous as it can be 170, 170.1, 170.11 and so on.
#離散分佈：分佈在單獨的事件集定義，例如，擲硬幣的結果是離散的，
# 因為它只能是頭部或尾部，而人的高度是連續的，因為它可以是
# 170，170.1，170.11等。
#Given 10 trials for coin toss generate 10 data points:
print("------------binomial(n=10, p=0.5, size=10)")
#給定10個擲硬幣試驗生成10個資料點：
from numpy import random
x = random.binomial(n=10, p=0.5, size=10)
print(x)
print("------------測試")
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10, p=0.5, size=10), hist=True)
#n在x軸,size在y軸
plt.show()
#預設會附上 **kernel density estimate（KDE）**曲線

print("-----binomial(n=10, p=0.5, size=1000), hist=True, kde=False")
#Visualization of Binomial Distribution
#可視化二元分佈
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
#hist是直方圖,kde是曲線圖
plt.show()

print("--------------------------正常分佈和二元分佈之間的差異")
#Difference Between Normal and Binomial Distribution
#正常分佈和二元分佈之間的差異
#The main difference is that normal distribution is continous whereas binomial is discrete, but if there are enough data points it will be quite similar to normal distribution with certain loc and scale.
#主要區別在於，正常分佈是連續性的，而二元分佈是離散的，但如果有足夠的數據點，它將非常類似於具有一定位置和比例的正常分佈。
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show() #若沒這行,就沒有圖表
#loc - 鐘峰存在的地方,在x軸
#scale - 標準差
#size - 在y軸
#n - 試驗次數,在x軸
#p - 概率
#size - 試驗數據的數量,在y軸