#https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp
#Pandas Cleaning Empty Cells 清除空單元
#Empty Cells 空單元
#Empty cells can potentially give you a wrong result when you analyze data.
#當您分析數據時，空單元可能會給你一個錯誤的結果。
#Remove Rows 刪除列
#One way to deal with empty cells is to remove rows that contain empty cells.
#處理空單元的一種方法是刪除包含空單元格的行。
#This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
#這通常是可以的，因為數據集可以非常大，刪除幾個行不會對結果產生太大的影響。
#Return a new Data Frame with no empty cells:
print("-------------------傳回沒有空單元的新資料框架")
#傳回沒有空單元的新資料框架：
import pandas as pd
df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())
#dropna()清理空單元,()如無參數必須左邊要有變數
#print(new_df)輸出前五筆後五筆
#In our cleaning examples we will be using a CSV file
#  called 'dirtydata.csv'.
#在我們的清潔示例中，我們將使用稱為「髒數據.csv」的 CSV 檔。
#Note: By default, the dropna() method returns a 
# new DataFrame, and will not change the original.
#注意：默認情況下，Dropna（） 方法返回新的數據框架，
# 並且不會改變原始數據框架。
#If you want to change the original DataFrame, 
# use the inplace = True argument:
#如果您要變更原始資料框架，請使用inplace(就地取值) = 真實參數：
#Remove all rows with NULL values:
print("----------------------移除具有 NULL 值的所有列")
#移除具有 NULL 值的所有列：
import pandas as pd
df = pd.read_csv('data.csv')
df.dropna(inplace = True)
print(df.to_string())
#dropna(inplace = True)裡有參數,所以不用設變數
#Note: Now, the dropna(inplace = True) will NOT 
# return a new DataFrame, but it will remove all 
# rows containg NULL values from the original 
# DataFrame.
#注意：現在，Dropna（(inplace = True）不會返回新的
# 數據框架，但它將從原始數據框架中刪除包含 NULL 值的
# 所有行。

print("---------------Replace Empty Values 替換空值")
#Replace Empty Values 替換空值
#Another way of dealing with empty cells is to insert a new value instead.
#處理空值的另一種方法是插入新的值。
#This way you do not have to delete entire rows just because of some empty cells.
#這樣，您就不必僅僅因為某些空單元格就刪除整個行。
#The fillna() method allows us to replace empty cells with a value:
#fillna()(填補空值fillnan)方法允許我們以價值替換空單元格：
#Replace NULL values with the number 130:
#將 NULL 值取代為數字 130：
import pandas as pd
df = pd.read_csv('dirtydata.csv')
df.fillna(130, inplace = True)
print(df.to_string())

print("-------------------------------僅替換指定欄")
#Replace Only For a Specified Columns
#僅替換指定欄
#The example above replaces all empty cells in the whole Data Frame.
#上例表示取代了整個數據框架中的所有空單元格。
#To only replace empty values for one column, specify the column name for the DataFrame:
#要僅替換一列的空值，只需指定資料框架的欄名：
#Replace NULL values in the "Calories" columns with the number 130:
#將「卡路里」列中的 NULL 值替換為數位 130：
import pandas as pd
df = pd.read_csv('dirtydata.csv')
df["Calories"].fillna(130, inplace = True)
print(df.to_string())

print("----------------------------使用平均數替換")
#Replace Using Mean, Median, or Mode
#使用平均、中位數或模式替換
#A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
#替換空儲存格的常見方法是計算列的平均值、中位數或模式值。
#Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
#熊貓使用平均值（）中位數（）和模式（）方法計算指定列的相應值：
#Calculate the MEAN, and replace any empty values with it:
#計算平均值，並將其替換為任何空值：
import pandas as pd
df = pd.read_csv('dirtydata.csv')
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
print(df.to_string())
#Mean = the average value (the sum of all values 
# divided by number of values).
#平均值 = 平均值（所有值的總和除以值數30=304.68）。

print("----------------------------使用中位數替換")
#Calculate the MEDIAN, and replace any empty values with it:
#計算中位數，並將其替換為任何空值：
import pandas as pd
df = pd.read_csv('dirtydata.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
print(df.to_string())
#Median = the value in the middle, after you have sorted all values ascending.
#中位數 = 中間值，在您對所有值提升進行排序后。

print("----------------------------使用MODE替換")
#Calculate the MODE, and replace any empty values with it:
#計算MODE，並將其替換為任何空值：
import pandas as pd
df = pd.read_csv('dirtydata.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
print(df.to_string())
#mode()[0],0代表空值,若沒有[0],則18,28列的空值還在
#300出現2次,則18,28列的值為300.0
#Mode = the value that appears most frequently.
#模式 = 最常出現的值。