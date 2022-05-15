#https://www.w3schools.com/python/python_ml_scale.asp
#Python Machine Learning - Scale 機器學習- 縮放
#Scale Features 縮放特徵
#When your data has different values, and even different measurement units, it can be difficult to compare them. What is kilograms compared to meters? Or altitude compared to time?
#當您的數據具有不同的值，甚至不同的測量單位時，可能很難比較它們。與儀錶相比，公斤是怎樣的？還是與時間相比海拔？
#The answer to this problem is scaling. We can scale data into new values that are easier to compare.
#這個問題的答案是縮放。我們可以將數據擴展為易於比較的新值。
#Take a look at the table below, it is the same data set that we used in the multiple regression chapter, but this time the volume column contains values in liters instead of cm3 (1.0 instead of 1000).
#看看下面的表，它是相同的數據集，我們在多個回歸章節中使用，但這次卷列包含值在升，而不是釐米3（1.0而不是1000）。
#The file is meant for testing purposes only, you can download it here: cars2.csv
#該檔僅用於測試目的，您可以在此處下載：cars2.csv
#It can be difficult to compare the volume 1.0 with the weight 790, but if we scale them both into comparable values, we can easily see how much one value is compared to the other.
#將體積 1.0 與重量 790 進行比較可能很困難，但如果我們將它們兩者都放大到可比值中，我們很容易看到一個值與另一個值相比的程度。
#There are different methods for scaling data, in this tutorial we will use a method called standardization.
#縮放數據的方法不同，在此教程中，我們將使用一種稱為標準化的方法。
#The standardization method uses this formula:
#標準化方法使用此公式：
#z = (x - u) / s
#Where z is the new value, x is the original value, u is the mean and s is the standard deviation.
#z 是新值，x 是原始值，u 是平均值，s 是標準偏差。
#If you take the weight column from the data set above, the first value is 790, and the scaled value will be:
#如果從上面的數據集中取出權重列，第一個值為 790，縮放值為：
#(790 - 1292.23) / 238.74 = -2.1
#If you take the volume column from the data set above, the first value is 1.0, and the scaled value will be:
#如果從上面的數據集中取體積欄，第一個值為 1.0，縮放值為：
#(1.0 - 1.61) / 0.38 = -1.59
#Now you can compare -2.1 with -1.59 instead of comparing 790 with 1.0.
#現在，您可以將 -2.1 與 -1.59 進行比較，而不是將 790 與 1.0 進行比較。
#You do not have to do this manually, the Python sklearn module has a method called StandardScaler() which returns a Scaler object with methods for transforming data sets.
#您不必手動操作，Python sklearn 模組具有一種稱為StandardScaler()的方法，它使用轉換數據集的方法返回 Scaler 物件。
#Scale all values in the Weight and Volume columns:
print("------------------------縮放重量和體積列中的所有值")
#縮放重量和體積列中的所有值：
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
df = pandas.read_csv("cars2.csv")
X = df[['Weight', 'Volume']]
scaledX = scale.fit_transform(X)
print(scaledX)
#fit_transform():Fit to data, then transform it.
#適合數據，然後轉換數據
#Note that the first two values are -2.1 and -1.59, which corresponds to our calculations:
#請注意，前兩個值是 -2.1 和 -1.59，這符合我們的計算：

print("----------------------------------預測二氧化碳值")
#Predict CO2 Values 預測二氧化碳值
#The task in the Multiple Regression chapter was to predict the CO2 emission from a car when you only knew its weight and volume.
#多重回歸「章節的任務是在你只知道汽車的重量和體積時預測汽車的二氧化碳排放。
#When the data set is scaled, you will have to use the scale when you predict values:
#當資料集縮放時，當您預測值時，您必須使用該刻度：
#Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms:
#預測一輛重達 2300 公斤的 1.3 升汽車的二氧化碳排放量：
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
df = pandas.read_csv("cars2.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']
scaledX = scale.fit_transform(X)
regr = linear_model.LinearRegression()
regr.fit(scaledX, y)
scaled = scale.transform([[2300, 1.3]])
predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)