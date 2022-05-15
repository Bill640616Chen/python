#https://www.w3schools.com/python/pandas/pandas_csv.asp
#Pandas Read CSV 
#Read CSV Files
#A simple way to store big data sets is to use CSV files (comma separated files).
#存儲大數據集的簡單方法是使用 CSV 檔（comma 分離檔）。
#CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
#CSV 檔包含純文本，是一種眾所周知的格式，包括熊貓在內的每個人都可以閱讀。
#In our examples we will be using a CSV file called 'data.csv'.
#在我們的示例中，我們將使用稱為「數據.csv」的 CSV 檔。
#Download data.csv. or Open data.csv
#下載數據.csv。或打開數據.csv
#Load the CSV into a DataFrame:
print("-----------------------將 CSV 載入資料框架中")
#將 CSV 載入資料框架中：
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string()) 
#print(df)輸出前5筆後5筆
#Tip: use to_string() to print the entire DataFrame.
#提示：使用to_string（）列印整個數據框架。

print("------------------loc[2:6]--列印減少的範例")
#By default, when you print a DataFrame, you will only get the first 5 rows, and the last 5 rows:
#預設情況下，當您列印數據幀時，您將只獲得前 5 行和最後 5 行：
#Print a reduced sample:
#列印減少的範例：
import pandas as pd
df = pd.read_csv('data.csv')
print(df.loc[2:6]) 
#loc[:]索引2-6的值