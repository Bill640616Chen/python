#Random betavariate() Method betavariate()方法
#基於 Beta 分佈（用於統計學）返回 0 到 1 之間的隨機浮點數。
#Beta 分佈。 參數的條件是 和 。 返回值的範圍介於 0 和 1 之間。alpha > 0beta > 0
#betavariate（）是內置的方法random模塊。 它用於返回具有beta分布的隨機浮點數。 返回值在0到1之間。
#用法： random.betavariate（alpha， beta）
#參數：
#alpha：大於0
#beta：大於0
#返回：一個介於0和1之間的隨機beta分布浮點數
#範例1：
# import the random module 
import random 
# determining the values of the parameters 
alpha = 5
beta = 10
# using the betavariate() method 
print(random.betavariate(alpha, beta))

#範例2：我們可以多次生成該數字並繪製圖表以觀察beta分布。
# import the required libraries 
import random 
import matplotlib.pyplot as plt 
# store the random numbers in a  
# list 
nums = [] 
low = 10
high = 100
mode = 20
for i in range(100):
    temp = random.betavariate(5, 10) 
    nums.append(temp) 
# plotting a graph 
plt.plot(nums) 
plt.show()
#random.triangular(low, high, mode)