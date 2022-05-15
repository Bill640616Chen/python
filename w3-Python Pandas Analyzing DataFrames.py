#https://www.w3schools.com/python/pandas/pandas_analyzing.asp
#Pandas Analyzing DataFrames 分析數據框架
#Viewing the Data 查看數據
#One of the most used method for getting a quick overview of the DataFrame, is the head() method.
#獲取數據框架快速概述的最常用的方法之一是head()方法。
#The head() method returns the headers and a specified number of rows, starting from the top.
#head()方法從頂部開始返回標頭和指定行數。
#Get a quick overview by printing the first 10 rows of the DataFrame:
print("----------通過列印數據框架的前 10 行獲得快速概述")
#通過列印數據框架的前 10 行獲得快速概述：
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(10))
#print(df.loc[:9])也是取前10筆資料
#head(N)從頭取N筆資料
#In our examples we will be using a CSV file called 'data.csv'.
#在我們的示例中，我們將使用稱為「數據.csv」的 CSV 檔。
#Download data.csv, or open data.csv in your browser.
#在瀏覽器中下載數據.csv或打開數據.csv。
#Note: if the number of rows is not specified, the head() method will return the top 5 rows.
#注意：如果不指定行數，則head()方法將返回前 5 行。
print("--------------------------沒指定行數,傳回前5行")
print(df.head()) #沒指定行數,傳回前5行
#print(df.loc)
#<pandas.core.indexing._LocIndexer object at 0x000001B3BE9D9630>
#There is also a tail() method for viewing the last rows of the DataFrame.
#還有一個tail()方法來查看數據框架的最後一行。
#The tail() method returns the headers and a specified number of rows, starting from the bottom.
#tail()方法從底部開始返回頭和指定行數。
#Print the last 5 rows of the DataFrame:
print("--------------------------沒指定行數,傳回後5行")
#列印資料框架的最後 5 行：
print(df.tail()) #沒指定行數,傳回後5行

#Info About the Data 有關數據的資訊
#The DataFrames object has a method called info(), that gives you more information about the data set.
#數據框架物件有一種稱為info() 的方法，它為您提供有關數據集的更多資訊。
#Print information about the data:
print("----------------------------列印有關數據的資訊")
#列印有關數據的資訊：
print(df.info()) 

#Result Explained 結果解釋
#The result tells us there are 169 rows and 4 columns:
#結果告訴我們有169列和4欄：
'''
  RangeIndex: 169 entries, 0 to 168
  Data columns (total 4 columns):
'''
#And the name of each column, with the data type:
#以及每個欄的名稱，以及資料類型：
'''
   #   Column    Non-Null Count  Dtype  
  ---  ------    --------------  -----  
   0   Duration  169 non-null    int64  
   1   Pulse     169 non-null    int64  
   2   Maxpulse  169 non-null    int64  
   3   Calories  164 non-null    float64
'''
#Null Values 空值
#The info() method also tells us how many Non-Null 
# values there are present in each column, and in 
# our data set it seems like there are 164 of 169 
# Non-Null values in the "Calories" column.
#info()方法還告訴我們每個列中有多少非空值，在我們的數據
# 集中，似乎"卡路里"列中有 169 個非空值中的 164 個。
#Which means that there are 5 rows with no value 
# at all, in the "Calories" column, for whatever 
# reason.
#這意味著，無論出於什麼原因，"卡路里"列中有 5 列沒有任
# 何價值。
#Empty values, or Null values, can be bad when 
# analyzing data, and you should consider removing 
# rows with empty values. This is a step towards 
# what is called cleaning data, and you will learn 
# more about that in the next chapters.
#在分析資料時，空值（或 Null 值）可能很糟糕，您應該考慮
# 刪除具有空值的行。這是朝著所謂的清潔數據邁出的一步，
# 您將在下一章中瞭解更多有關這一點的詳細情況。
