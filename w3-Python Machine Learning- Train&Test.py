#https://www.w3schools.com/python/python_ml_train_test.asp
#Python Machine Learning - Train/Test 機器學習- 訓練/測試
#Evaluate Your Model 評估您的模型
#In Machine Learning we create models to predict the outcome of certain events, like in the previous chapter where we predicted the CO2 emission of a car when we knew the weight and engine size.
#在機器學習中，我們創建模型來預測某些事件的結果，比如在前一章中，當我們知道汽車的重量和發動機尺寸時，我們預測了汽車的二氧化碳排放。
#To measure if the model is good enough, we can use a method called Train/Test.
#為了測量模型是否足夠好，我們可以使用一種稱為「訓練/測試」。的方法。
#What is Train/Test 什麼是訓練/測試
#Train/Test is a method to measure the accuracy of your model.
#訓練/測試是測量模型準確性的方法。
#It is called Train/Test because you split the the data set into two sets: a training set and a testing set.
#它被稱為「培訓/測試」，因為您將數據集拆分為兩組：一組培訓集和一組測試集。
#80% for training, and 20% for testing.
#80% 用於培訓，20% 用於測試。
#You train the model using the training set.
#您使用培訓集訓練模型。
#You test the model using the testing set.
#您使用測試集測試模型。
#Train the model means create the model.
#訓練模型意味著創建模型。
#Test the model means test the accuracy of the model.
#測試模型意味著測試模型的準確性。
#Start With a Data Set 從數據集開始
#Start with a data set you want to test.
#從要測試的數據集開始。
#Our data set illustrates 100 customers in a shop, and their shopping habits.
print("---------我們的數據集展示了一家商店的100名顧客及其購物習慣")
#我們的數據集展示了一家商店的100名顧客及其購物習慣。
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
plt.scatter(x, y)
plt.show()
#esult:結果
#The x axis represents the number of minutes before making a purchase.
#x 軸表示購買前的分鐘數。
#The y axis represents the amount of money spent on the purchase.
#y 軸表示用於購買的金額。
#Split Into Train/Test 拆分為訓練/測試
#The training set should be a random selection of 80% of the original data.
#培訓集應隨機選擇 80% 的原始數據。
#The testing set should be the remaining 20%.
#測試集應該是剩餘的 20%。
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
#Display the Training Set 顯示培訓集
#Display the same scatter plot with the training set:
print("--------------------------顯示與培訓集相同的散射圖")
#顯示與培訓集相同的散射圖：
plt.scatter(train_x, train_y)
plt.show()
#It looks like the original data set, so it seems to be a fair selection:
#它看起來像原始數據集，所以它似乎是一個公平的選擇：

#Display the Testing Set 顯示測試集
#To make sure the testing set is not completely different, we will take a look at the testing set as well.
print("-------為了確保測試集並非完全不同，我們還將查看測試集")
#為了確保測試集並非完全不同，我們還將查看測試集。
plt.scatter(test_x, test_y)
plt.show()
#Result: 結果：
#The testing set also looks like the original data set:
#測試集看起來也像原始資料集：

print("----------------------Fit the Data Set 適合數據集")
#Fit the Data Set 適合數據集
#What does the data set look like? In my opinion I think the best fit would be a polynomial regression, so let us draw a line of polynomial regression.
#數據集是什麼樣子的？在我看來，我認為最合適的是多面體回歸，所以讓我們畫一條多面回歸的線。
#To draw a line through the data points, we use the plot() method of the matplotlib module:
#要通過數據點繪製一條線，我們使用 matplotlib 模組的繪圖（）方法：
#Draw a polynomial regression line through the data points:
#通過資料點繪製多面回歸線：
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline = numpy.linspace(0, 6, 100)
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()
#linspace(start: _ArrayLikeNumber, stop: _ArrayLikeNumber, num: SupportsIndex = ..., endpoint: bool = ..., retstep: Literal[False] = ..., dtype: DTypeLike = ..., axis: SupportsIndex = ...) -> ndarray
#linspace(start: _ArrayLikeNumber, stop: _ArrayLikeNumber, num: SupportsIndex = ..., endpoint: bool = ..., retstep: Literal[True] = ..., dtype: DTypeLike = ..., axis: SupportsIndex = ...) -> Tuple[ndarray, Any]
#numpy.linspace(1, 22, 100) 1,代表x軸的開始點,22代表x軸的停止點
#The result can back my suggestion of the data set fitting a polynomial regression, even though it would give us some weird results if we try to predict values outside of the data set. Example: the line indicates that a customer spending 6 minutes in the shop would make a purchase worth 200. That is probably a sign of overfitting.
#結果可以支援我的建議，即數據集適合多面體回歸，即使如果我們嘗試預測數據集以外的值，它會給我們一些奇怪的結果。示例：該行指示客戶在商店中花費 6 分鐘，將購買價值 200 美元的產品。這可能是過度健身的跡象。
#But what about the R-squared score? The R-squared score is a good indicator of how well my data set is fitting the model.
#但是 R 方形分數呢？R 方分很好地指示了我的數據集與模型的配合程度。

#R2
#Remember R2, also known as R-squared?
#還記得 R2 嗎，也叫 R 方形？
#It measures the relationship between the x axis and the y axis, and the value ranges from 0 to 1, where 0 means no relationship, and 1 means totally related.
#它測量 x 軸和 y 軸之間的關係，值範圍從 0 到 1，其中 0 表示沒有關係，1 表示完全相關。
#The sklearn module has a method called r2_score() that will help us find this relationship.
#sklearn 模組有一種稱為r2_score的方法（）將幫助我們找到這種關係。
#In this case we would like to measure the relationship between the minutes a customer stays in the shop and how much money they spend.
#在這種情況下，我們想衡量客戶在商店停留的時間和花費多少錢之間的關係。
#How well does my training data fit in a polynomial regression?
print("------------------我的訓練數據在多面回歸中有多合適？")
#我的訓練數據在多面回歸中有多合適？
import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
r2 = r2_score(train_y, mymodel(train_x))
print(r2)
#把120,121行的train改成test後,數據更接近1
#polyfit: (x, y, deg, rcond=..., full=..., w=..., cov=...) -> Any
#deg : int...Degree of the fitting polynomial
##適合多面體的度數
#r2_score:(coefficient of determination) regression score 
# function.
#（確定係數）回歸分數函數。
#r2_score: (y_true, y_pred, *, sample_weight=None, 
# multioutput="uniform_average") -> (float | ndarray | Any)
#Note: The result 0.799 shows that there is a OK relationship.
#注：結果0.799表明存在良好關係。

#Bring in the Testing Set 引入測試集
#Now we have made a model that is OK, at least when it comes to training data.
#現在，我們已經製作了一個模型，這是確定，至少當涉及到培訓數據。
#Now we want to test the model with the testing data as well, to see if gives us the same result.
#現在，我們也想用測試數據來測試模型，看看是否給我們相同的結果。
#Let us find the R2 score when using testing data:
print("------------------讓我們在使用測試數據時找到 R2 分數")
#讓我們在使用測試數據時找到 R2 分數：
import numpy
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
r2 = r2_score(test_y, mymodel(test_x))
print(r2)
#Note: The result 0.809 shows that the model fits the testing set as well, and we are confident that we can use the model to predict future values.
#注：結果 0.809 顯示該模型也符合測試集，我們相信，我們可以使用該模型預測未來值。

print("----------如果購買客戶在店裡呆上5分鐘，她會花多少錢？")
#Predict Values預測值
#Now that we have established that our model is OK, we can start predicting new values.
#現在，我們已經確定我們的模型是確定的，我們可以開始預測新的值。
#How much money will a buying customer spend, if she or he stays in the shop for 5 minutes?
#如果購買客戶在店裡呆上5分鐘，她會花多少錢？
print(mymodel(10))
plt.scatter(test_x, test_y)
plt.plot(myline, mymodel(myline))
plt.show()
#test只有20%,故分散的點較train少
#待10分鐘,客人的可能消費10668.566758263845
#待5分鐘,客人的可能消費22.879625918114925
#The example predicted the customer to spend 22.88 dollars, as seems to correspond to the diagram:
#該示例預測客戶將花費 22.88 美元，這似乎與圖表相對應：


