#https://www.w3schools.com/python/numpy/numpy_random_poisson.asp
#Random Poisson Distribution large N 二元分佈
#Poisson Distribution large N 二元分佈
#是一種統計與機率學裡常見到的離散機率分布
#Poisson dist就是次數無限多的binomial dst的結果總合
#Poisson Distribution is a Discrete Distribution.
#Poisson分佈是一個離散分佈。
#It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is probability he will eat thrice?
#它估計事件在指定時間內可能發生的次數。如果有人一天吃兩次，他吃三次的可能性是大的嗎？
#It has two parameters:
#它有兩個參數：
#lam - rate or known number of occurences e.g. 2 for above problem.
#lam - 上述問題的發生率或已知次數， 例如 2 。
#在固定時間間隔內發生的預期事件數必須>= 0。序列必須在請求的大小上廣播。
#size - The shape of the returned array.
#size - 傳回陣列的形狀。數據的數量
#輸出形狀。如果給定的形狀是，例如（m，n，k），則繪製 m * n * k 
# 樣本。如果大小為無（預設值），如果 lam 是標量，則返回單個值。
# 否則，將繪製 np.array（lam）大小樣本。
#Generate a random 1x10 distribution for occurence 2:
print("------------------------------poisson(lam=1, size=6)")
#產生隨機 1x10 分佈以用於發生 2：
from numpy import random
x = random.poisson(lam=10, size=10)
print(x)
#lam感覺是隨機出現靠近10的數字
#[12  6  8 13 14 11  4 10 11  8]
from numpy import random
x = random.poisson(lam=1, size=6)
print(x)
#lam感覺是隨機出現靠近1的數字
#[1 1 2 1 0 1]

print("------------------------------可視化Poisson分佈")
#Visualization of Poisson Distribution
#可視化Poisson分佈
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

print("-------------圖表----正常分佈和Poisson分佈之間的差異")
#Difference Between Normal and Poisson Distribution
#正常分佈和Poisson分佈之間的差異
#Normal distribution is continous whereas poisson is discrete.
#正常分佈是連續的，而Poisson是離散的。
#But we can see that similar to binomial for a large enough poisson distribution it will become similar to normal distribution with certain std dev and mean.
#但是，我們可以看到，類似於二元為足夠大的泊松分佈，它會變得類似於正常分佈與某些 std(標準差) 開發和平均。
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=True, label='poisson')
plt.show()

print("-------------圖表----Poisson和二元分佈之間的差異")
#Difference Between Poisson and Binomial Distribution
#Poisson和二元分佈之間的差異
#The difference is very subtle it is that, binomial distribution is for discrete trials, whereas poisson distribution is for continuous trials.
#區別是非常微妙的，它是，二元分佈是離散試驗，而Poisson分佈是連續試驗。
#But for very large n and near-zero p binomial distribution is near identical to poisson distribution such that n * p is nearly equal to lam.
#但對於非常大的 n 和接近零 p 雙體分佈幾乎相同的 poisson 分佈， 使 n * p 幾乎等於 lam 。
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
plt.show()
#二元分佈使 n * p 幾乎等於 lam

print("-------------圖表--正常,Poisson和二元分佈之間的差異")
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=10, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
plt.show()