#https://www.w3schools.com/python/numpy/numpy_random_distribution.asp
#Random Data Distribution 隨機數據分佈
#What is Data Distribution? 什麼是數據分佈？
#Data Distribution is a list of all possible values, and how often each value occurs.
#數據分佈是所有可能值的清單，以及每個值發生的頻率。
#Such lists are important when working with statistics and data science.
#在統計學和數據科學方面，此類清單非常重要。
#The random module offer methods that returns randomly generated data distributions.
#隨機模組提供返回隨機生成的數據分佈的方法。

#Random Distribution 隨機分佈
#A random distribution is a set of random numbers that follow a certain probability density function.
#隨機分佈是一組隨一定概率密度函數隨之的隨機數。
#Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.
#概率密度函數：描述連續概率的函數。即陣列中所有值的概率。
#We can generate random numbers based on defined probabilities using the choice() method of the random module.
#我們可以使用隨機模組的choice()方法根據定義的概率生成隨機數。
#The choice() method allows us to specify the probability for each value.
#choice()方法允許我們指定每個值的概率。
#The probability is set by a number between 0 and 1, where 0 means that the value will never occur and 1 means that the value will always occur.
#概率由 0 到 1 之間的數字設置，其中 0 表示值永遠不會發生，1 表示值始終會發生。
#Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
print("----生成包含100個值的1D陣列，其中每個值必須為3、5、7或9")
#生成包含100個值的1D陣列，其中每個值必須為3、5、7或9。
#The probability for the value to be 3 is set to be 0.1
#值為 3 的概率設置為 0.1
#The probability for the value to be 5 is set to be 0.3
#值為 5 的概率設置為 0.3
#The probability for the value to be 7 is set to be 0.6
#值為 7 的概率設置為 0.6
#The probability for the value to be 9 is set to be 0
#值為 9 的概率設置為 0
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x) #100個隨機數_1維陣列
#The sum of all probability numbers should be 1.
#所有概率數的總和應為 1。
#Even if you run the example above 100 times, the value 9 will never occur.
#即使運行示例超過 100 次，值 9 也永遠不會發生。
#You can return arrays of any shape and size by specifying the shape in the size parameter.
#您可以通過在大小參數中指定形狀來返回任何形狀和大小的陣列。
#Same example as above, but return a 2-D array with 3 rows, each containing 5 values.
print("------------返回具有 3 行的 2D 陣列，每個行包含 5 個值")
#與上文相同的範例，但返回具有 3 行的 2D 陣列，每個行包含 5 個值。
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x) #3 行的 2D 陣列，每個行包含 5 個值
print("------------測試choice([3, 5, 7, 9]只傳回一個")
from numpy import random
x = random.choice([3, 5, 7, 9])
print(x)