#Random gammavariate() Method gammavariate()方法
#基於 Gamma 分佈（用於統計學）返回 0 到 1 之間的隨機浮點數。
#gammavariate（） 是內置的方法random模塊。 它用於返回具有伽馬分布的隨機浮點數。
#Gamma 分佈。 （不是gamma 函數！ ） 參數的條件是 與 。alpha > 0beta > 0
'''
概率分佈函數是：

          x ** (alpha - 1) * math.exp(-x / beta)
pdf(x) =  --------------------------------------
            math.gamma(alpha) * beta ** alpha
'''
#用法： random.gammavariate（alpha， beta）
#參數：
#alpha：大於0
#beta：大於0
#返回：隨機伽馬分布浮點數
#範例1：
# import the random module 
import random 
# determining the values of the parameter 
alpha = 100
beta = 2
# using the gammavariate() method 
print(random.gammavariate(alpha, beta))
#輸出：

#範例2：我們可以多次生成該數字並繪製圖形以觀察伽瑪分布。
# import the required libraries  
import random  
import matplotlib.pyplot as plt  
# store the random numbers in a   
# list  
nums = []  
alpha = 9
beta = 0.5
for i in range(100):  
    temp = random.gammavariate(alpha, beta) 
    nums.append(temp)  
# plotting a graph  
plt.plot(nums)  
plt.show()

#範例3：我們可以創建一個直方圖來觀察伽瑪分布的密度。
# import the required libraries  
import random  
import matplotlib.pyplot as plt  
# store the random numbers in a list  
nums = []  
alpha = 9
beta = 0.5
for i in range(10000):  
    temp = random.gammavariate(alpha, beta) 
    nums.append(temp)  
# plotting a graph  
plt.hist(nums, bins = 200)  
plt.show()