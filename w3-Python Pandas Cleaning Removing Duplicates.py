#https://www.w3schools.com/python/pandas/pandas_cleaning_duplicates.asp
#Pandas Removing Duplicates 移除重複
#Discovering Duplicates 發現重複
#Duplicate rows are rows that have been registered more than one time.
#重複行是已註冊多次的行。
#By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.
#通過查看我們的測試數據集，我們可以假設第 11 行和第 12 行是重複的。
#To discover duplicates, we can use the duplicated() method.
#要發現重複，我們可以使用重複（）方法。
#The duplicated() method returns a Boolean values for each row:
#重複（） 方法傳回每行的 Boolean 值：
#Returns True for every row that is a duplicate, othwerwise False:
print("-----------返回真實的每一行是重複的， 否則錯誤")
#返回真實的每一行是重複的， 否則錯誤：
import pandas as pd
df = pd.read_csv('dirtydata.csv')
print(df.duplicated())
#檢查每一列是否重複

print("------------------------------------刪除重複")
#Removing Duplicates 刪除重複
#To remove duplicates, use the drop_duplicates() method.
#要刪除重複，請使用drop_duplicates（）方法。
import pandas as pd
df = pd.read_csv('data.csv')
df.drop_duplicates(inplace = True)
print(df.to_string())
#Notice that row 12 has been removed from the result
#請注意，第 12 行已從結果中刪除
#Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.
#請記住：（inplace = True）將確保該方法不會返回新的數據框架，但它將從原始數據框架中刪除所有副本。


