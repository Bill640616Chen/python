#https://www.w3schools.com/python/numpy/numpy_random_uniform.asp
#Random Uniform Distribution 均勻分佈
#Uniform Distribution 均勻分佈
#Used to describe probability where every event has equal chances of occuring.
#用於描述每個事件發生機會相等的概率。
#E.g. Generation of random numbers.
#例如，隨機數字的生成。
#It has three parameters:
#它有三個參數：
#a - lower bound - default 0 .0.
#a - 輸出間隔的下邊界。生成的所有值將大於或等於低值。預設值為 0
#b - upper bound - default 1.0.
#b - 輸出間隔的上邊界。生成的所有值將小於或等於高值。預設值為 1.0。
#size - The shape of the returned array.
#size - 傳回陣列的形狀
#Create a 2x3 uniform distribution sample:
print("--------------------------------建立 2x3 均勻分佈範例")
#建立 2x3 均勻分佈範例：
from numpy import random
x = random.uniform(size=(5, 3))
print(x)
#size=(1維陣列的n個(不管n是多少,都是2維),每個陣列n個元素)
print("--------------------測試1-----建立均勻分佈範例")
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
y = random.uniform(1,10,size=(3,5))
#uniform(1(最低0),10(最低1),size=(3,5))
#uniform(a,b,size),a跟b不同分大小,
# size可以使用size=N 或 N 或 size=(3,5)
print(y)
sns.distplot(y)
plt.show()
print("--------------------測試2-----建立均勻分佈範例")
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
z = random.uniform(10,1,size=(3,5))
#uniform(10(最低0),1(最低1),size=(3,5))
print(z)
sns.distplot(z)
plt.show()

print("---------------------------------圖表--可視化均勻分佈")
#Visualization of Uniform Distribution
#可視化均勻分佈
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.uniform(size=(1000,100))
print(x)
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()
