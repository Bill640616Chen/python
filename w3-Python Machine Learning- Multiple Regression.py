#https://www.w3schools.com/python/python_ml_multiple_regression.asp
#Python Machine Learning - Multiple Regression 機器學習- 多次回歸
#Multiple Regression 多次回歸
#Multiple regression is like linear regression, but with more than one independent value, meaning that we try to predict a value based on two or more variables.
#多次回歸就像線性回歸，但具有多個獨立值，這意味著我們嘗試根據兩個或多個變數預測值。
#Take a look at the data set below, it contains some information about cars.
#看看下面的數據集，它包含一些關於汽車的資訊。
#We can predict the CO2 emission of a car based on the size of the engine, but with multiple regression we can throw in more variables, like the weight of the car, to make the prediction more accurate.
#我們可以根據發動機的大小預測汽車的二氧化碳排放，但多重回歸后，我們可以拋出更多的變數，如汽車的重量，使預測更準確。
#How Does it Work? 它是如何工作的？
#In Python we have modules that will do the work for us. Start by importing the Pandas module.
#在 Python 中，我們有模組可以為我們完成工作。從導入pandas模組開始。
import pandas
#Learn about the Pandas module in our Pandas Tutorial.
#了解我們Pandas教程中的Pandas模組。
#The Pandas module allows us to read csv files and return a DataFrame object.
#Pandas模組允許我們讀取 csv 檔並返回數據幀物件。
#The file is meant for testing purposes only, you can download it here: cars.csv
#該檔僅用於測試目的，您可以在此處下載：cars.csv
df = pandas.read_csv("cars.csv")
#Then make a list of the independent values and call this variable X.
#然後列出獨立值並調用此可變 X。
#Put the dependent values in a variable called y.
#將受撫養值放入稱為 y 的變數中。
X = df[['Weight', 'Volume']]
y = df['CO2']
#Tip: It is common to name the list of independent values with a upper case X, and the list of dependent values with a lower case y.
#提示：通常以上殼 X 命名獨立值清單，以及用小寫 y 命名受撫養值清單。
#We will use some methods from the sklearn module, so we will have to import that module as well:
#我們將使用一些方法從sklearn模組，所以我們將不得不導入該模組以及：
from sklearn import linear_model
#From the sklearn module we will use the LinearRegression() method to create a linear regression object.
#從 sklearn 模組中，我們將使用LinearRegression()方法創建線性回歸物件。
#This object has a method called fit() that takes the independent and dependent values as parameters and fills the regression object with data that describes the relationship:
#此物件具有一種稱為擬合fit()的方法，該方法以獨立和受撫養的值為參數，並用描述關係的數據填充回歸物件：
regr = linear_model.LinearRegression()
regr.fit(X, y)
#Now we have a regression object that are ready to predict CO2 values based on a car's weight and volume:
#現在我們有一個回歸對象，準備根據汽車的重量和體積預測二氧化碳值：
#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
#預測重量為 2300kg 且體積為 1300cm3 的汽車的二氧化碳排放量：
predictedCO2 = regr.predict([[2300, 1300]])
#See the whole example in action:
print("----------------------------請參閱整個範例在操作中")
#請參閱整個範例在操作中：
import pandas
from sklearn import linear_model
df = pandas.read_csv("cars.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(X, y)
#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)
#We have predicted that a car with 1.3 liter engine, and a weight of 2300 kg, will release approximately 107 grams of CO2 for every kilometer it drives.
#我們預測，一輛1.3升發動機、重量為2300公斤的汽車每行駛一公里就會釋放大約107克二氧化碳。

print("----------------------------------Coefficient 係數")
#Coefficient 係數
#The coefficient is a factor that describes the relationship with an unknown variable.
#係數是描述與未知變數關係的一個因素。
#Example: if x is a variable, then 2x is x two times. x is the unknown variable, and the number 2 is the coefficient.
#示例：如果 x 是變數，則 2x 是 x 兩次。x 是未知變數，數位 2 是係數。
#In this case, we can ask for the coefficient value of weight against CO2, and for volume against CO2. The answer(s) we get tells us what would happen if we increase, or decrease, one of the independent values.
#在這種情況下，我們可以要求重量與二氧化碳的係數值，以及與二氧化碳的體積。我們得到的答案告訴我們，如果我們增加或減少一個獨立值，會發生什麼。
#Print the coefficient values of the regression object:
#列印回歸物件的係數值：
import pandas
from sklearn import linear_model
df = pandas.read_csv("cars.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(X, y)
print(regr.coef_)
#coef_(coefficients係數):包含每個目標預測係數

print("------------------------Result Explained 結果解釋")
#Result Explained 結果解釋
#The result array represents the coefficient values of weight and volume.
#結果陣列表示重量和體積的係數值。
Weight: 0.00755095
Volume: 0.00780526
#These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.
#這些值告訴我們，如果重量增加1公斤，二氧化碳排放量增加0.00755095克。
#And if the engine size (Volume) increases by 1 cm3, the CO2 emission increases by 0.00780526 g.
#如果發動機尺寸（體積）增加1立方米，二氧化碳排放量增加0.00780526克。
#I think that is a fair guess, but let test it!
#我認為這是一個公平的猜測， 但讓測試它！
#We have already predicted that if a car with a 1300cm3 engine weighs 2300kg, the CO2 emission will be approximately 107g.
#我們已經預測，如果一輛1300cm3發動機的汽車重達2300公斤，二氧化碳排放量約為107克。
#What if we increase the weight with 1000kg?
#如果我們增加1000公斤的重量呢？
#Copy the example from before, but change the weight from 2300 to 3300:
#複製以前的例子，但將重量從 2300 更改為 3300：
import pandas
from sklearn import linear_model
df = pandas.read_csv("cars.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedCO2 = regr.predict([[3300, 1300]])
print(predictedCO2)
#We have predicted that a car with 1.3 liter engine, and a weight of 3300 kg, will release approximately 115 grams of CO2 for every kilometer it drives.
#我們預測，一輛1.3升發動機、重量為3300公斤的汽車每行駛一公里就會釋放大約115克二氧化碳。
#Which shows that the coefficient of 0.00755095 is correct:
#結果表明0.00755095係數正確：
107.2087328 + (1000 * 0.00755095) = 114.75968