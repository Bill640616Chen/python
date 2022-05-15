#https://www.w3schools.com/python/python_ml_polynomial_regression.asp
#Python Machine Learning - Polynomial Regression 機器學習- 多面回歸
#Polynomial Regression 多面回歸
#If your data points clearly will not fit a linear regression (a straight line through all data points), it might be ideal for polynomial regression.
#如果您的數據點顯然不適合線性回歸（通過所有數據點的直線），則可能是多名額回歸的理想選擇。
#Polynomial regression, like linear regression, uses the relationship between the variables x and y to find the best way to draw a line through the data points.
#多面回歸，如線性回歸，使用變數 x 和 y 之間的關係，找到通過數據點繪製線的最佳方法。
#How Does it Work? 它是如何工作的？
#Python has methods for finding a relationship between data-points and to draw a line of polynomial regression. We will show you how to use these methods instead of going through the mathematic formula.
#Python 有查找數據點之間的關係和繪製多名額回歸線的方法。我們將向您展示如何使用這些方法，而不是通過數學公式。
#In the example below, we have registered 18 cars as they were passing a certain tollbooth.
#在下面的例子中，我們已經註冊了18輛車，因為他們通過一個收費站。
#We have registered the car's speed, and the time of day (hour) the passing occurred.
#我們已經記錄了汽車的速度，一天（小時）的通過時間發生了。
#The x-axis represents the hours of the day and the y-axis represents the speed:
#x 軸表示一天中的小時數，y 軸表示速度：
#Start by drawing a scatter plot:
print("---------------------------------------首先繪製散射圖")
#首先繪製散射圖：
import matplotlib.pyplot as plt
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
plt.scatter(x, y)
plt.show()
#Import numpy and matplotlib then draw the line of Polynomial Regression:
print("---------導入numpy和matplotlib，然後繪製多面體回歸的線")
#導入numpy和matplotlib，然後繪製多面體回歸的線：
import numpy
import matplotlib.pyplot as plt
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel = numpy.poly1d(numpy.polyfit(x, y, 10))
myline = numpy.linspace(1, 22, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
#polyfit: (x, y, deg, rcond=..., full=..., w=..., cov=...) -> Any
#deg : int...Degree of the fitting polynomial
#適合多面體的度數
#numpy.polyfit(x, y, 10)    10代表每個線盡可能連接到每個點
#linspace(start: _ArrayLikeNumber, stop: _ArrayLikeNumber, num: SupportsIndex = ..., endpoint: bool = ..., retstep: Literal[False] = ..., dtype: DTypeLike = ..., axis: SupportsIndex = ...) -> ndarray
#linspace(start: _ArrayLikeNumber, stop: _ArrayLikeNumber, num: SupportsIndex = ..., endpoint: bool = ..., retstep: Literal[True] = ..., dtype: DTypeLike = ..., axis: SupportsIndex = ...) -> Tuple[ndarray, Any]
#numpy.linspace(1, 22, 100) 22代表x軸的停止點
# 當polyfit(x,y,100)時,num:50時,所有的點都集中在最前面
# 當polyfit(x,y,100)時,num:10時,所有的點都集中在最前面

print("------------------------Example Explained 示例解釋")
#Example Explained 示例解釋
#Import the modules you need.
#匯入您需要的模組。
#You can learn about the NumPy module in our NumPy Tutorial.
#您可以在我們的 NumPy 教程中瞭解 NumPy 模組。
#You can learn about the SciPy module in our SciPy Tutorial.
#您可以在我們的「SciPy教程」中瞭解 SciPy 模組。
import numpy
import matplotlib.pyplot as plt
#Create the arrays that represent the values of the x and y axis:
#建立表示 x 和 y 軸值的陣列：
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
#NumPy has a method that lets us make a polynomial model:
#NumPy 有一種方法，可以讓我們製作一個多面模型：
mymodel = numpy.poly1d(numpy.polyfit(x, y, 10))
#Then specify how the line will display, we start at position 1, and end at position 22:
#然後指定行將如何顯示，我們從位置 1 開始，到位置 22 結束：
myline = numpy.linspace(1, 22, 100)
#Draw the original scatter plot:
#繪製原始散射圖：
plt.scatter(x, y)
#Draw the line of polynomial regression:
#繪製多面體回歸線：
plt.plot(myline, mymodel(myline))
#Display the diagram:
#顯示圖表：
plt.show()

#R-Squared R 方形
#It is important to know how well the relationship between the values of the x- and y-axis is, if there are no relationship the polynomial regression can not be used to predict anything.
#重要的是要知道x-和y軸的值之間的關係有多好，如果沒有關係，多面回歸不能用來預測任何東西。
#The relationship is measured with a value called the r-squared.
#關係的測量值稱為 r 方形。
#The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.
#r 平方值範圍從0到1，其中0表示沒有關係，1 表示100%相關。
#Python and the Sklearn module will compute this value for you, all you have to do is feed it with the x and y arrays:
#Python 和 Sklearn 模組將為您計算此值，您所要做的就是用 x 和 y 陣列饋送它：
#How well does my data fit in a polynomial regression?
print("----------------------我的數據在多面體回歸中是否適合？")
#我的數據在多面體回歸中是否適合？
import numpy
from sklearn.metrics import r2_score
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
print('r2_score:',r2_score(y, mymodel(x)))
#r2_score:(coefficient of determination) regression score function.
#（確定係數）回歸分數函數。
#numpy.poly1d (arr, root, var)
#polyfit(x, y, 10),10會影響r2_score的值,數值越高,越貼近1
#polyfit: (x, y, deg, rcond=..., full=..., w=..., cov=...) -> Any
#deg : int...Degree of the fitting polynomial
#適合多面體的度數
#numpy.polyfit(x, y, 10)    10代表每個線盡可能連接到每個點
#Note: The result 0.94 shows that there is a very good relationship, and we can use polynomial regression in future predictions.
#注：結果0.94表明，雙方關係非常好，我們可以在未來的預測中使用多面體回歸。

print("------------------------------------------預測未來值")
#Predict Future Values 預測未來值
#Now we can use the information we have gathered to predict future values.
#現在，我們可以使用我們收集到的信息來預測未來的值。
#Example: Let us try to predict the speed of a car that passes the tollbooth at around 17 P.M:
#示例：讓我們嘗試預測在 17 P.M 左右通過收費站的汽車的速度.M：
#To do so, we need the same mymodel array from the example above:
#為此，我們需要與上表相同的模組：
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
#Predict the speed of a car passing at 17 P.M:
#預測汽車在 17 P .M 的速度：
import numpy
from sklearn.metrics import r2_score
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
speed = mymodel(17)
print('預測未來值:',speed)
#The example predicted a speed to be 88.87, which we also could read from the diagram:
#該示例預測速度為 88.87，我們也可以從圖表中讀取：

print("--------------------------------Bad Fit? 不好的合適")
#Bad Fit? 不好的合適
#Let us create an example where polynomial regression would not be the best method to predict future values.
#讓我們舉一個例子，其中多面體回歸不是預測未來價值的最佳方法。
#These values for the x- and y-axis should result in a very bad fit for polynomial regression:
#X 軸和 y 軸的這些值應導致非常不適合多重回歸：
import numpy
import matplotlib.pyplot as plt
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline = numpy.linspace(2, 95, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.plot(myline)
plt.show()
print("-------------------------------------r 平方值呢？")
#And the r-squared value?
#r 平方值呢？
#You should get a very low r-squared value.
#你應該得到一個非常低的 r 平方值。
import numpy
from sklearn.metrics import r2_score
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
print('r2_score:',r2_score(y, mymodel(x)))
#The result: 0.00995 indicates a very bad relationship, and tells us that this data set is not suitable for polynomial regression.
#結果：0.00995表示關係非常糟糕，並告訴我們此數據集不適合多面體回歸。
#polyfit(x, y, 10),10會影響r2_score的值,數值越高,越貼近1
#polyfit: (x, y, deg, rcond=..., full=..., w=..., cov=...) -> Any
#deg : int...Degree of the fitting polynomial
#適合多面體的度數
#numpy.polyfit(x, y, 10)    10代表每個線盡可能連接到每個點
#r2_score:(coefficient of determination) regression score function.
#（確定係數）回歸分數函數。
#Best possible score is 1.0 and it can be negative 
# (because the model can be arbitrarily worse). A 
# constant model that always predicts the expected 
# value of y, disregarding the input features, would 
# get a R^2 score of 0.0.
#最好的分數是1.0，它可以是負的（因為模型可以任意更糟）。
# 始終預測 y 的預期值的恆定模型（忽略輸入功能）將獲得 0.0 
# 的 R=2 分數。