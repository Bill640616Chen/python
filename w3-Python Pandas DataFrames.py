#https://www.w3schools.com/python/pandas/pandas_dataframes.asp
#Pandas DataFrames Pandas數據框架
#What is a DataFrame?什麼是數據框架？
#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
#熊貓數據框架是一個 2 維數據結構，如 2 維陣列，或具有行和列的表。
#Create a simple Pandas DataFrame:
print("-------------------建立簡單的熊貓資料框架")
#建立簡單的熊貓資料框架：
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
#load將數據到數據框架中：
df = pd.DataFrame(data)
print(df) 

print("-----------------Locate Row 定位行loc[0]")
#Locate Row 定位行,能傳回二維以上的陣列索引
#As you can see from the result above, the DataFrame is like a table with rows and columns.
#正如您從上面的結果中看到的，DataFrame 就像一張有行和列的表。
#Pandas use the loc attribute to return one or more specified row(s)
#熊貓使用loc屬性返回一個或多個指定行
#Return row 0:
#返回行 0：
#refer to the row index: 指定行的索引碼
print(df.loc[0])
#Note: This example returns a Pandas Series.
#注意:這範例傳回一個Pandas系列

print("-----------Return row 0 and 1:傳回0行與1行")
#Return row 0 and 1:傳回0行與1行
#use a list of indexes:
#使用索引清單
print(df.loc[[0, 1]])
#Note: When using [], the result is a Pandas DataFrame.
#當使用[],這結果是Pandas數據框架

print("-------------------Named Indexes 為索引命名")
#Named Indexes 為索引命名
#With the index argument, you can name your own indexes.
#有了索引參數，您可以說出自己的索引。
#Add a list of names to give each row a name:
#新增名稱清單，給每行一個名稱：
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 

print("--------Locate Named Indexes 定名被命名的索引")
#Locate Named Indexes 定名被命名的索引
#Use the named index in the loc attribute to return the specified row(s).
#使用位置屬性中的命名索引返回指定行。"
#Return "day2": 傳回 "day2"
#refer to the named index:
#指定索引的名稱
print(df.loc["day2"])

print("-------------------------將檔載入到數據框架中")
#Load Files Into a DataFrame將檔載入到數據框架中
#If your data sets are stored in a file, Pandas can load them into a DataFrame.
#如果您的數據集存儲在檔中，熊貓可以將其載入到數據框架中。
#Load a comma separated file (CSV file) into a DataFrame:
#將逗號分離檔 （CSV 檔案） 載入數據框架中：
import pandas as pd
df = pd.read_csv('data.csv')
print(df) #輸出前5筆後5筆
#You will learn more about importing files in the next chapters.
#您將在下一章中瞭解有關導入檔的更多資料。

