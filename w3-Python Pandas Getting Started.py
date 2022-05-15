#https://www.w3schools.com/python/pandas/pandas_getting_started.asp
#Pandas Getting Started
#Pandas (panel data analysis面板數據分析的縮寫)
#Installation of Pandas 安裝Pandas
#If you have Python and PIP already installed on a system, then installation of Pandas is very easy.
#如果您的 Python 和 PIP 已經安裝在系統上，那麼安裝Pandas非常容易。
#Install it using this command:
#使用此指令安裝它：
#If this command fails, then use a python distribution that already has Pandas installed like, Anaconda, Spyder etc.
#如果此命令失敗，則使用已經安裝了Pandas的python分佈，如，Anaconda, Spyder 等。
#Import Pandas 導入Pandas
#Once Pandas is installed, import it in your applications by adding the import keyword:
#安裝Pandas后，請通過添加導入關鍵字在應用程式中導入：
import pandas
#Now Pandas is imported and ready to use.
print("----------------------------import pandas")
#現在Pandas已經導入,準備使用
import pandas
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pandas.DataFrame(mydataset)
print(myvar)
#DataFrame()變表格,cars,passings在列的標頭,
# 其他值也以列呈現,每列最前是索引值

#Pandas as pd
#Pandas is usually imported under the pd alias.
#Pandas通常以 pd 別名導入。
#alias: In Python alias are an alternate name for referring to the same thing.
#別名： 在 Python 別名中， 是提及同一件事的替代名稱。
#Create an alias with the as keyword while importing:
#在匯入時建立帶有關鍵字的別名：
import pandas as pd
#Now the Pandas package can be referred to as pd instead of pandas.
#現在Pandas包可以稱為 pd 而不是Pandas。
print("------------------------import pandas as pd")
import pandas as pd
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

print("-----------------------------pd.__version__")
#Checking Pandas Version 檢查Pandas的版本
#The version string is stored under __version__ attribute.
#版本字串存儲在屬性下__version__。
import pandas as pd
print(pd.__version__)
