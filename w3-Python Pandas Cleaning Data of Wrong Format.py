#https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_format.asp
#Pandas Cleaning Data of Wrong Format 
#清除錯誤格式的數據
#Data of Wrong Format 錯誤格式的數據
#Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
#具有錯誤格式數據的儲存格可能使分析數據變得困難，甚至無法分析。
#To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
#要修復它，您有兩個選項：刪除列，或將列中的所有儲存格轉換為相同的格式。
#Convert Into a Correct Format 轉換為正確的格式
#In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the 'Date' column should be a string that represents a date:
#在我們的數據框架中，我們有兩個格式錯誤的儲存格。查看第 22 列和第 26 列，"日期"列應是表示日期的字串：
print("---------查看第 22 列和第 26 列，日期列應是表示日期的字串")
import pandas as pd
df = pd.read_csv('dirtydata.csv')
print(df.to_string())
#Let's try to convert all cells in the 'Date' column into dates.
#讓我們嘗試將「日期」列中的所有儲存格轉換為日期。
#Pandas has a to_datetime() method for this:
#熊貓有一個to_datetime（）方法：
#Convert to date:
print("---------------------------------轉換至日期")
#轉換至日期：
import pandas as pd
df = pd.read_csv('dirtydata.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())
#As you can see from the result, the date in row 26 was fixed, but the empty date in row 22 got a NaT (Not a Time) value, in other words an empty value. One way to deal with empty values is simply removing the entire row.
#從結果中可以看出，第 26 列中的日期已固定，但第 22 列中的空日期具有 NAT（不是時間）值，換句話說，是空值。處理空值的一種方法是簡單地刪除整個列。

print("------------------------------------刪除列")
#Removing Rows 刪除列
#The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.
#上表中轉換的結果為我們提供了 NAT 值，該值可以作為 NULL 值處理，並且我們可以使用 dropna（）方法刪除行。
#Remove rows with a NULL value in the "Date" column:
#刪除「日期」列中具有 NULL 值的行：
import pandas as pd
df = pd.read_csv('dirtydata.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.dropna(subset=['Date'], inplace = True)
print(df.to_string())
#刪除日期為NaT列之前,先把26列的日期格式改變

print("---------------------------測試------刪除列")
import pandas as pd
df = pd.read_csv('dirtydata.csv')
df.dropna(inplace = True)
print(df.to_string())
#dropna(inplace = True)刪除有空值的列