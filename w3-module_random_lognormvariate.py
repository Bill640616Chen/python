#Random lognormvariate() Method lognormvariate()方法
#基於對數正態分佈（用於概率論）返回 0 到 1 之間的隨機浮點數。
#對數正態分佈。 如果你採用這個分佈的自然對數，你將得到一個
# 正態分佈，平均值為mu和標準差為sigma 。 mu可以是任何值，
# sigma必須大於零。
#lognormvariate（） 是內置的方法random模塊。 它用於返回具有log-normal分布的隨機浮點數。
#用法： random.lognormvariate（mu， sigma）
#參數：
#mu：平均
#sigma：標準偏差，大於0
#返回：隨機的log-normal分配浮點數
#範例1：
# import the random module 
import random 
# determining the values of the parameters 
mu = 0
sigma = 0.25
# using the lognormvariate() method 
print(random.lognormvariate(mu, sigma))
#輸出：

#範例2：我們可以多次生成該數字並繪製圖形以觀察log-normal的分布。
# import the required libraries  
import random  
import matplotlib.pyplot as plt  
# store the random numbers in a   
# list  
nums = []  
mu = 0
sigma = 0.25
for i in range(100):  
    temp = random.lognormvariate(mu, sigma) 
    nums.append(temp)  
# plotting a graph  
plt.plot(nums)  
plt.show()

#範例3：我們可以創建一個直方圖來觀察log-normal分布的密度。
# import the required libraries  
import random  
import matplotlib.pyplot as plt  
# store the random numbers in a list  
nums = []  
mu = 0
sigma = 0.25
for i in range(10000):  
    temp = random.lognormvariate(mu, sigma)  
    nums.append(temp)  
# plotting a graph  
plt.hist(nums, bins = 200)  
plt.show()