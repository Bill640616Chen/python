#https://www.w3schools.com/python/pandas/pandas_series.asp
#Pandas Series Pandas系列
#What is a Series? 什麼是系列？
#A Pandas Series is like a column in a table.
#Pandas系列就像桌子上的柱子。
#It is a one-dimensional array holding data of any type.
#它是一個一維陣列，保存著任何類型的數據。
#Create a simple Pandas Series from a list:
print("--------------從清單中建立一個簡單的Pandas系列")
#從清單中建立一個簡單的Pandas系列：
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
#Series()以列排列下來,最後顯示資料類型

print("----------------------------------Labels")
#Labels 標籤
#If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
#如果沒有其他指定，則值會標有其索引號。第一值有指數0，第二值有指數1等。
#This label can be used to access a specified value.
#此標籤可用於訪問指定值。
#Return the first value of the Series:
#返回系列的第一個值：
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar[0])
#[]傳回索引位置0的值,只能傳回一維陣列

print("---------------------------Create Labels")
#Create Labels 創建標籤
#With the index argument, you can name your own labels.
#有了索引參數，您可以命名自己的標籤。
#Create you own labels:
#建立您自己的標籤：
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"])
#最後顯示資料類型dtype: int64
#左欄的預設索引碼標籤012,被取代為xyz
#When you have created labels, you can access an 
# item by referring to the label.
#創建標籤后，您可以通過引用標籤訪問專案。
