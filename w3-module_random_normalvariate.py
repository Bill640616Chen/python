#Random normalvariate() Method normalvariate()方法
#基於正態分佈（用於概率論）返回 0 到 1 之間的隨機浮點數。
#正態分佈。 mu是平均值，sigma是標準差。
#normalvariate（） 是內置的方法random模組。 它用於返回具有正態分佈的隨機浮點數。
#用法： random.normalvariate（mu， sigma）
#參數：
#mu：平均
#sigma：標準偏差
#返回：隨機正態分佈浮點數
#範例1：
# import the random module 
import random 
# determining the values of the parameters 
mu = 100
sigma = 50
# using the normalvariate() method 
print(random.normalvariate(mu, sigma))
#輸出：

#範例2：我們可以多次生成該數字並繪製圖形以觀察正態分佈。
# import the required libraries  
import random  
import matplotlib.pyplot as plt  
# store the random numbers in a   
# list  
nums = []  
mu = 100
sigma = 50
for i in range(100):  
    temp = random.normalvariate(mu, sigma) 
    nums.append(temp)  
# plotting a graph  
plt.plot(nums)  
plt.show()

#範例3：我們可以創建一個直方圖來觀察正態分佈的密度。
# import the required libraries  
import random  
import matplotlib.pyplot as plt  
# store the random numbers in a list  
nums = []  
mu = 100
sigma = 50
for i in range(10000):  
    temp = random.normalvariate(mu, sigma)  
    nums.append(temp)  
# plotting a graph  
plt.hist(nums, bins = 200)  
plt.show()

