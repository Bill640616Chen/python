#https://www.w3schools.com/python/pandas/pandas_json.asp
#Pandas Read JSON
#Big data sets are often stored, or extracted as JSON.
#大數據集通常存儲或提取為 JSON。
#JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
#JSON 是純文字，但有一個物件的格式，並在程式設計世界中廣為人知，包括熊貓。
#In our examples we will be using a JSON file called 'data.json'.
#在我們的示例中，我們將使用稱為「數據.json」的 JSON 檔。
#Open data.json.
#打開數據. json.
#Load the JSON file into a DataFrame:
print("--------------------將 JSON 檔載入資料框架中")
#將 JSON 檔載入資料框架中：
import pandas as pd
df = pd.read_json('data.json')
print(df.to_string()) 
#Tip: use to_string() to print the entire DataFrame.
#提示：使用to_string（）列印整個數據框架。

#Dictionary as JSON 字典作為 Json
#JSON = Python Dictionary
#JSON = Python字典
#JSON objects have the same format as Python 
# dictionaries.
#JSON 物件的格式與 Python 字典相同。
#If your JSON code is not in a file, but in a Python 
# Dictionary, you can load it into a DataFrame 
# directly:
#如果您的 JSON 代碼不在檔中，而是在 Python 字典中，
# 您可以直接將其載入到數據框架中：
#Load a Python Dictionary into a DataFrame:
print("---------------載入一個Python字典到數據框架中")
#載入一個Python字典到數據框架中:
import pandas as pd
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
df = pd.DataFrame(data)
print(df) 