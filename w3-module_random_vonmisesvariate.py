#Random vonmisesvariate() Method vonmisesvariate()方法
#基於 von Mises 分佈（用於定向統計學）返回 0 到 1 之間的
# 隨機浮點數。
#馮·米塞斯分佈。 mu是平均角度，以弧度表示，介於0和 2*pi之間，
# kappa是濃度參數，必須大於或等於零。 如果kappa等於零，
# 則該分佈在 0 到 2*pi的範圍內減小到均勻的隨機角度。
#本文整理匯總了Python中random.vonmisesvariate方法的典型
# 用法代碼示例。 如果您正苦於以下問題：
# Python random.vonmisesvariate方法的具體用法？ 
# Python random.vonmisesvariate怎麼用？ 
# Python random.vonmisesvariate使用的例子？ 
# 那麼恭喜您， 這裡精選的方法代碼示例或許可以為您提供説明。 
# 您也可以進一步瞭解該方法所在類random的用法示例。
#在下文中一共展示了random.vonmisesvariate方法的9個代碼示例，
# 這些例子默認根據受歡迎程度排序。 您可以為喜歡或者感覺
# 有用的代碼點讚，您的評價將有助於我們的系統推薦出更棒的
# Python代碼示例。
# 1.import the random module 
import random 
# determining the values of the parameters 
mu = 0
kappa = 4
# using the vonmisesvariate() method 
print(random.vonmisesvariate(mu, kappa))

#2.We can generate the number multiple times and plot a graph to observe the Von Mises distribution.
#我們可以多次生成這個數位，並繪製一個圖表來觀察馮·米塞斯分佈。
# import the required libraries 
import random 
import matplotlib.pyplot as plt 
# store the random numbers in a 
# list 
nums = [] 
mu = 0
kappa = 4
for i in range(100): 
    temp = random.vonmisesvariate(mu, kappa) 
    nums.append(temp) 
# plotting a graph 
plt.plot(nums) 
plt.show() 

#3.We can create a histogram to observe the density of the Von Mises distribution.
#我們可以創建一個直方圖來觀察馮·米塞斯分佈的密度。
# import the required libraries 
import random 
import matplotlib.pyplot as plt 
# store the random numbers in a list 
nums = [] 
mu = 0
kappa = 4
for i in range(10000): 
    temp = random.vonmisesvariate(mu, kappa) 
    nums.append(temp) 
# plotting a graph 
plt.hist(nums, bins = 200) 
plt.show()
'''
#示例1： test_zeroinputs
# 需要導入模組： import random [as 別名]
# 或者： from random import vonmisesvariate [as 別名]
from _typeshed import Self
import random
def test_zeroinputs(self):
        # Verify that distributions can handle a series of zero inputs'
        g = random.Random()
        x = [g.random() for i in xrange(50)] + [0.0]*5
        g.random = x[:].pop; g.uniform(1,10)
        g.random = x[:].pop; g.paretovariate(1.0)
        g.random = x[:].pop; g.expovariate(1.0)
        g.random = x[:].pop; g.weibullvariate(1.0, 1.0)
        g.random = x[:].pop; g.vonmisesvariate(1.0, 1.0)
        g.random = x[:].pop; g.normalvariate(0.0, 1.0)
        g.random = x[:].pop; g.gauss(0.0, 1.0)
        g.random = x[:].pop; g.lognormvariate(0.0, 1.0)
        g.random = x[:].pop; g.vonmisesvariate(0.0, 1.0)
        g.random = x[:].pop; g.gammavariate(0.01, 1.0)
        g.random = x[:].pop; g.gammavariate(1.0, 1.0)
        g.random = x[:].pop; g.gammavariate(200.0, 1.0)
        g.random = x[:].pop; g.betavariate(3.0, 3.0)
        g.random = x[:].pop; g.triangular(0.0, 1.0, 1.0/3.0) 

#示例2： test_constant
# 需要導入模組： import random [as 別名]
# 或者： from random import vonmisesvariate [as 別名]
def test_constant(self):
        g = random.Random()
        N = 100
        for variate, args, expected in [
                (g.uniform, (10.0, 10.0), 10.0),
                (g.triangular, (10.0, 10.0), 10.0),
                (g.triangular, (10.0, 10.0, 10.0), 10.0),
                (g.expovariate, (float('inf'),), 0.0),
                (g.vonmisesvariate, (3.0, float('inf')), 3.0),
                (g.gauss, (10.0, 0.0), 10.0),
                (g.lognormvariate, (0.0, 0.0), 1.0),
                (g.lognormvariate, (-float('inf'), 0.0), 0.0),
                (g.normalvariate, (10.0, 0.0), 10.0),
                (g.paretovariate, (float('inf'),), 1.0),
                (g.weibullvariate, (10.0, float('inf')), 10.0),
                (g.weibullvariate, (0.0, 10.0), 0.0),
            ]:
            for i in range(N):
                self.assertEqual(variate(*args), expected) 

#示例3： test_constant
# 需要導入模組： import random [as 別名]
# 或者： from random import vonmisesvariate [as 別名]
def test_constant(self):
        g = random.Random()
        N = 100
        for variate, args, expected in [
                (g.uniform, (10.0, 10.0), 10.0),
                (g.triangular, (10.0, 10.0), 10.0),
                #(g.triangular, (10.0, 10.0, 10.0), 10.0),
                (g.expovariate, (float('inf'),), 0.0),
                (g.vonmisesvariate, (3.0, float('inf')), 3.0),
                (g.gauss, (10.0, 0.0), 10.0),
                (g.lognormvariate, (0.0, 0.0), 1.0),
                (g.lognormvariate, (-float('inf'), 0.0), 0.0),
                (g.normalvariate, (10.0, 0.0), 10.0),
                (g.paretovariate, (float('inf'),), 1.0),
                (g.weibullvariate, (10.0, float('inf')), 10.0),
                (g.weibullvariate, (0.0, 10.0), 0.0),
            ]:
            for i in range(N):
                self.assertEqual(variate(*args), expected) 
'''