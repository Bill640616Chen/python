#Random gauss() Method gauss()方法
#基於高斯分佈（用於概率論）返回 0 到 1 之間的隨機浮點數。
#正態分佈，也稱高斯分佈。 mu為平均值，而sigma為標準差。 
# 此函數要稍快於下面所定義的normalvariate（）函數。
#多線程注意事項：當兩個線程同時調用此方法時，它們有可能將獲得
# 相同的返回值。 這可以通過三種辦法來避免。 1） 讓每個線程使用
# 不同的隨機數產生器實例。 2） 在所有調用外面加鎖。 3） 改用
# 速度較慢但是線程安全的normalvariate（）函數。
#gauss（） 是內置的方法random模組。 它用於返回具有高斯分佈的隨機浮點數。
#用法： random.gauss（mu， sigma）
#參數：
#mu：平均
#sigma：標準偏差
#返回：隨機高斯分佈浮點數
#範例1：
# import the random module 
import random 
# determining the values of the parameters 
mu = 100
sigma = 50
# using the gauss() method 
print(random.gauss(mu, sigma))
#輸出：

#範例2：我們可以多次生成該數字並繪製圖形以觀察高斯分佈。
# import the required libraries  
import random  
import matplotlib.pyplot as plt  
# store the random numbers in a   
# list  
nums = []  
mu = 100
sigma = 50
for i in range(100):  
    temp = random.gauss(mu, sigma) 
    nums.append(temp)  
# plotting a graph  
plt.plot(nums)  
plt.show()
#輸出：

#範例3：我們可以創建一個直方圖來觀察高斯分佈的密度。
# import the required libraries  
import random  
import matplotlib.pyplot as plt  
# store the random numbers in a list  
nums = []  
mu = 100
sigma = 50
for i in range(10000):  
    temp = random.gauss(mu, sigma)  
    nums.append(temp)  
# plotting a graph  
plt.hist(nums, bins = 200)  
plt.show()