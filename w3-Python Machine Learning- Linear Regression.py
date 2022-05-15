#https://www.w3schools.com/python/python_ml_linear_regression.asp
#Python Machine Learning - Linear Regression 機器學習- 線性回歸
#Regression 回歸
#The term regression is used when you try to find the relationship between variables.
#當您試圖查找變數之間的關係時，會使用"回歸"一詞。
#In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.
#在機器學習和統計建模中，這種關係用於預測未來事件的結果。
#Linear Regression 線性回歸
#Linear regression uses the relationship between the data-points to draw a straight line through all them.
#線性回歸使用數據點之間的關係，通過所有數據點繪製一條直線。
#This line can be used to predict future values.
#此行可用於預測未來值。
#In Machine Learning, predicting the future is very important.
#在機器學習中，預測未來非常重要。
#How Does it Work? 它是如何工作的？
#Python has methods for finding a relationship between data-points and to draw a line of linear regression. We will show you how to use these methods instead of going through the mathematic formula.
#Python 有查找數據點之間的關係和繪製線性回歸線的方法。我們將向您展示如何使用這些方法，而不是通過數學公式。
#In the example below, the x-axis represents age, and the y-axis represents speed. We have registered the age and speed of 13 cars as they were passing a tollbooth. Let us see if the data we collected could be used in a linear regression:
#在下面的示例中，x 軸表示年齡，y 軸表示速度。我們已經登記了13輛車的年齡和速度，因為他們通過收費站。讓我們看看我們收集的數據是否可用於線性回歸：
#Start by drawing a scatter plot:
print("------------------------------------首先繪製散射圖")
#首先繪製散射圖：
import matplotlib.pyplot as plt
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x, y)
plt.show()
#Import scipy and draw the line of Linear Regression:
#匯入scipy並繪製線性回歸線：
import matplotlib.pyplot as plt
from scipy import stats
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
#map(func, *iterables):製作一個傳數，使用每個可執行項的
# 參數計算函數。當最短的可重做已用完時停止。
#slope:坡度,intercept:(數學)截距,stats:(模組)統計
print("------------------------Example Explained 示例解釋")
#Example Explained 示例解釋
#Import the modules you need.
#匯入您需要的模組。
#You can learn about the Matplotlib module in our Matplotlib Tutorial.
#您可以在我們的Matplotlib教程中了解Matplotlib模組。
#You can learn about the SciPy module in our SciPy Tutorial.
#您可以在我們的「SciPy教程」中瞭解 SciPy 模組。
import matplotlib.pyplot as plt
from scipy import stats
#Create the arrays that represent the values of the x and y axis:
#建立表示 x 和 y 軸值的陣列：
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#Execute a method that returns some important key values of Linear Regression:
#執行返回線性回歸的一些重要關鍵值的方法：
slope, intercept, r, p, std_err = stats.linregress(x, y)
#Create a function that uses the slope and intercept values to return a new value. This new value represents where on the y-axis the corresponding x value will be placed:
#創建一個功能，使用坡度和截距值來返回新值。此新值表示 y 軸上將放置相應的 x 值的位置：
def myfunc(x):
  return slope * x + intercept
#Run each value of the x array through the function. This will result in a new array with new values for the y-axis:
#通過函數運行 x 陣列的每個值。這將產生一個新的陣列，其中具有 y 軸的新值：
mymodel = list(map(myfunc, x))
#map(func, *iterables):製作一個傳數，使用每個可執行項的
# 參數計算函數。當最短的可重做已用完時停止。
# #Draw the original scatter plot:
#繪製原始散射圖：
plt.scatter(x, y)
#Draw the line of linear regression:
#繪製線性回歸線：
plt.plot(x, mymodel) #(x,y)
#Display the diagram:
#顯示圖表：
plt.show()

#R for Relationship R 表示關係
#It is important to know how the relationship between the values of the x-axis and the values of the y-axis is, if there are no relationship the linear regression can not be used to predict anything.
#重要的是要知道x軸的值和y軸的值之間的關係是怎樣的，如果沒有關係，線性回歸不能用來預測任何事情。
#This relationship - the coefficient of correlation - is called r.
#這種關係 - 相關係數 - 稱為 r。
#The r value ranges from -1 to 1, where 0 means no relationship, and 1 (and -1) means 100% related.
#r 值範圍從 -1 到 1，其中 0 表示沒有關係，1（和 -1） 表示 100% 相關。
#Python and the Scipy module will compute this value for you, all you have to do is feed it with the x and y values.
#Python 和 Scipy 模組將為您計算此值，您所要做的就是用 x 和 y 值來饋送它。
#How well does my data fit in a linear regression?
print("-------------print(r)--我的數據在線性回歸中是否適合？")
#我的數據在線性回歸中是否適合？
from scipy import stats
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
slope, intercept, r, p, std_err = stats.linregress(x, y)
print('slope:',slope)
print('intercept:',intercept)
print('r:',r)
print('p:',p)
print('std_err:',std_err)
#Note: The result -0.76 shows that there is a relationship, not perfect, but it indicates that we could use linear regression in future predictions.
#注：結果-0.76表明存在一種關係，並不完美，但它表明我們可以在未來的預測中使用線性回歸。

#Predict Future Values 預測未來值
#Now we can use the information we have gathered to predict future values.
#現在，我們可以使用我們收集到的信息來預測未來的值。
#Example: Let us try to predict the speed of a 10 years old car.
#示例：讓我們嘗試預測 10 年老車的速度。
#To do so, we need the same myfunc() function from the example above:
#為此，我們需要從上面的示例中提供相同的 myfunc （） 功能：
def myfunc(x):
  return slope * x + intercept
#Predict the speed of a 10 years old car:
print("---------------------------預測一輛 10 年老車的速度")
#預測一輛 10 年老車的速度：
from scipy import stats
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept
speed = myfunc(10)
print(speed)
#The example predicted a speed at 85.6, which we also could read from the diagram:
#該示例預測速度為 85.6，我們也可以從圖表中讀取：

#Bad Fit? 不好的適合
#Let us create an example where linear regression would not be the best method to predict future values.
#讓我們舉一個例子，線性回歸不是預測未來值的最佳方法。
#These values for the x- and y-axis should result in a very bad fit for linear regression:
print("-----------X 軸和 y 軸的這些值應導致非常不適合線性回歸")
#X 軸和 y 軸的這些值應導致非常不適合線性回歸：
import matplotlib.pyplot as plt
from scipy import stats
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
#And the r for relationship?
#r跟關係呢?
#You should get a very low r value.
print("-----------------------你應該得到一個非常低的 r 值")
#你應該得到一個非常低的 r 值。
import numpy
from scipy import stats
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
slope, intercept, r, p, std_err = stats.linregress(x, y)
print(r)
#The result: 0.013 indicates a very bad relationship, and tells us that this data set is not suitable for linear regression.
#結果：0.013 表示關係非常糟糕，並告訴我們此數據集不適合線性回歸。