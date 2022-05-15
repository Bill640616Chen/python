#Random expovariate() Method expovariate()方法
#基於指數分佈（用於統計學），返回 0 到 1 之間的隨機浮點數，如果參數為負，則返回 0 到 -1 之間的隨機浮點數。
#指數分佈。 lambd是 1.0 除以所需的平均值，它應該是非零的。 
# （該參數本應命名為 「lambda」 ，但這是 Python 中的保留字。 ）
# 如果lambd為正，則返回值的範圍為 0 到正無窮大;如果lambd為負，
# 則返回值從負無窮大到 0。
#random模組用於在Python中生成隨機數。 實際上不是隨機的，而是用於生成偽隨機數的。 這意味著可以確定這些隨機生成的數位。
#expovariate()
#expovariate（） 是內置的方法random模組。 它用於返回具有 index 分佈的隨機浮點數。
#用法： random.expovariate（lambd）
#參數：
#lambd：非零值
#返回：隨機 index 分佈浮點數
#如果參數為正，則結果範圍為0到正無窮大
#如果參數為負，則結果範圍為0到負無窮大
#範例1：
# import the random module 
import random 
# determining the values of the parameter 
lambd = 1.5
# using the expovariate() method 
print(random.expovariate(lambd))
#輸出：

#範例2：我們可以多次生成該數字並繪製圖形以觀察 index 分佈。
# import the required libraries  
import random  
import matplotlib.pyplot as plt  
# store the random numbers in a   
# list  
nums = []  
alpha = 3
for i in range(100):  
    temp = random.expovariate(alpha) 
    nums.append(temp)  
# plotting a graph  
plt.plot(nums)  
plt.show()

#範例3：我們可以創建一個直方圖來觀察 index 分佈的密度。
# import the required libraries  
import random  
import matplotlib.pyplot as plt  
# store the random numbers in a list  
nums = []  
lambd = 1.5
for i in range(10000):  
    temp = random.expovariate(lambd) 
    nums.append(temp)  
# plotting a graph  
plt.hist(nums, bins = 200)  
plt.show()