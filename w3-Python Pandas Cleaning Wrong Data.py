#https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_data.asp
#Pandas Cleaning Wrong Data 清除錯誤數據
#Wrong Data 錯誤數據
#"Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".
#"錯誤數據"不必是"空單元格"或"錯誤格式"，它可能是錯誤的，就像有人註冊了"199"而不是"1.99"。
#Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.
#有時，您可以通過查看數據集來發現錯誤的數據，因為您期望數據集應該是什麼。
#If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.
#如果你看看我們的數據集，你可以看到，在第7列，持續時間是450，但對於所有其他列的持續時間是30至60之間。
#It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that this person did not work out in 450 minutes.
#這不一定是錯的，但考慮到這是某人的鍛煉課程的數據集，我們的結論是這個人在450分鐘內沒有鍛煉。
#How can we fix wrong values, like the one for "Duration" in row 7?
#我們如何修復錯誤的值，例如第7列中的「持續時間」值？
print("------------------------------------替換值")
#Replacing Values 替換值
#One way to fix wrong values is to replace them with something else.
#修復錯誤值的一種方法是用其他方法替換它們。
#In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:
#以我們為例，它很可能是一個拼寫錯誤，值應該是「45」而不是「450」，我們可以在第7列插入「45」：
#Set "Duration" = 45 in row 7:
#設定「持續時間」 = 第 7 列中的 45：
import pandas as pd
df = pd.read_csv('dirtydata.csv')
df.loc[7,'Duration'] = 45
print(df.to_string())
#For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
#對於小型數據集，您也許能夠逐個替換錯誤的數據，但不能替換大數據集。
#To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.
#要為較大的數據集替換錯誤的數據，您可以創建一些規則，例如為法律值設置一些邊界，並替換任何超出邊界的值。
#Loop through all values in the "Duration" column.
#迴圈流覽「持續時間」列中的所有值。
#If the value is higher than 120, set it to 120:
print("--------------歷Duration的值,如>120,則替換值為120")
#如果值高於 120，則將其設置為 120：
import pandas as pd
df = pd.read_csv('dirtydata.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
print(df.to_string())
#遍歷Duration的值,如>120,則替換值為120

#Removing Rows 刪除列
#Another way of handling wrong data is to remove the rows that contains wrong data.
#處理錯誤數據的另一種方法是刪除包含錯誤數據的列。
#This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
#這樣，您就不必找出用什麼來替換它們，而且很有可能您不需要它們來進列分析。
#Delete rows where "Duration" is higher than 120:
print("------------------刪除「持續時間」高於 120 的列")
#刪除「持續時間」高於 120 的列：
import pandas as pd
df = pd.read_csv('dirtydata.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
#remember to include the 'inplace = True' argument to make the changes in the original DataFrame object instead of returning a copy
#請記住，請包含"inplace = True"參數，以便對原始數據框架物件進列更改，而不是返回副本
print(df.to_string())