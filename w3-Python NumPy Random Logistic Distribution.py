#https://www.w3schools.com/python/numpy/numpy_random_logistic.asp
#Random Logistic Distribution 增長分佈
#增長分佈的分佈函數是"增長函數"，亦稱"邏輯斯諦函數"
# （logistic function），故增長分佈亦稱做"邏輯斯諦分佈"。
#  邏輯斯諦分佈（logistic distribution）是一種連續型的概率分佈
#Logistic Distribution 增長分佈
#Logistic Distribution is used to describe growth.
#增長分佈用於描述增長
#Used extensively in machine learning in logistic regression, neural networks etc.
#廣泛應用於後勤回歸、神經網路等機器學習。
#It has three parameters:
#它有三個參數：
#loc - mean, where the peak is. Default 0.
#loc - （平均） 鐘峰存在的地方,預設值0。(表示正態分佈的均值)
#scale - standard deviation, the flatness of distribution. Default 1.
#scale - （標準差） 圖形分佈應有多平。(表示正態分佈的標準差，預設為1)
#size - The shape of the returned array.
#size - 傳回陣列的形狀
#Draw 2x3 samples from a logistic distribution with mean at 1 and stddev 2.0:
#從增長分佈中抽取 2x3 樣本，平均值為 1 和 標準差 2.0：
print("---------------logistic(loc=1, scale=2, size=(2, 3)")
# stddev：標準偏差 (Std Dev,Standard Deviation)
from numpy import random
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

print("--------------------------------可視化增長分佈")
#Visualization of Logistic Distribution
#可視化增長分佈
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()

print("------------------圖表-----增長分佈與正常分佈的差異")
#Difference Between Logistic and Normal Distribution
#增長分佈與正常分佈的差異
#Both distributions are near identical, but logistic distribution has more area under the tails. ie. It representage more possibility of occurence of an events further away from mean.
#兩種分佈幾乎相同，但增長分佈在尾部下有更多的區域。即.它表示更有可能發生遠離平均值的事件。
#For higher value of scale (standard deviation) the normal and logistic distributions are near identical apart from the peak.
#對於高值的規模（標準偏差），正常和增長分佈與峰值幾乎相同。
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
plt.show()