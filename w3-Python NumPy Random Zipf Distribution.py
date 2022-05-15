#https://www.w3schools.com/python/numpy/numpy_random_zipf.asp
#Random Zipf Distribution 冪律分佈
#Zipf 分佈（也稱為 zeta 分佈）
#帕累托分佈屬於連續概率分佈。 "“吉普夫定律"， 也稱為"zeta 
# 分佈"， 也可以被認為是在離散概率分佈中的帕累托分佈。 
#Zipf distritutions are used to sample data based on zipf's law.
#Zipf 分離用於根據 zipf 定律對數據進行採樣。
#Zipf's Law: In a collection the nth common term 
# is 1/n times of the most common term. E.g. 5th 
# common word in english has occurs nearly 1/5th 
# times as of the most used word.
#Zipf 的定律：在集合中，第 n 個常用術語是最常見術語的 
# 1/n 倍。例如，英語中的第5個常用單詞在最常用的單詞中
# 已經發生了近1/5倍。
#It has two parameters:
#它有兩個參數：
#a - distribution parameter.
#a - 分布參數.
#size - The shape of the returned array.
#size - 傳回陣列的形狀。
print("-----------------------zipf(a=2, size=(2, 3))")
#Draw out a sample for zipf distribution with distribution parameter 2 with size 2x3:
#繪製具有分佈參數 2 的 zipf 分佈示例，尺寸為 2x3：
from numpy import random
x = random.zipf(a=2, size=(2, 3))
#size=(2, 3),()可以N維
print(x)

print("----------zipf(a=2, size=1000)可視化Zipf分佈")
#Visualization of Zipf Distribution
#可視化Zipf分佈
#Sample 1000 points but plotting only ones with value < 10 for more meaningful chart.
#示例 1000 點，但僅繪製值< 10 點的點，以獲得更有意義的圖表。
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False, label='Zipf')
plt.legend() #顯示標籤
plt.show()

print("----測試---zipf(a=2, size=1000)可視化Zipf分佈")
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.zipf(a=2, size=1000)
sns.distplot(x, label='Zipf')
plt.legend() #顯示標籤
plt.show()