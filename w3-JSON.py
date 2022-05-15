#https://www.w3schools.com/python/python_json.asp
#Python JSON
#（全名 JavaScript Object Notation）是一種將資料呈現為
# JavaScript 物件的標準格式
#JSON is a syntax for storing and exchanging data.
#JSON 是用於存儲和交換數據的語法。
#JSON is text, written with JavaScript object notation.
#JSON 是用 JavaScript 物件表示法（JavaScript object notation）
# 編寫的文本。
#JSON in Python
#Python has a built-in package called json, which can be used to work with JSON data.
#Python 有一個名為 json 的內置包，可用於處理 JSON 數據。
#Import the json module:
#匯入 json 模組：
import json
print("----------------------------把 JSON 轉換為 Python")
#Parse JSON - Convert from JSON to Python
#解析 JSON - 把 JSON 轉換為 Python
#If you have a JSON string, you can parse it by using the json.loads() method.
#若有 JSON 字串，則可以使用 json.loads（） 方法對其進行解析。
#The result will be a Python dictionary.
#結果將是 Python 字典。
#Convert from JSON to Python:
#將 JSON 轉換為 Python：
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
#解析 x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

print("----------------------------把 Python 轉換為 JSON")
#Convert from Python to JSON
#把 Python 轉換為 JSON
#If you have a Python object, you can convert it into
#  a JSON string by using the json.dumps() method.
#若有 Python 物件，則可以使用 json.dumps（） 方法將其轉換為
# JSON 字串。
#Convert from Python to JSON:
#將 Python 轉換為 JSON：
import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

print("----------------------------把 JSON 轉換為 Python-2")
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
#解析 x:
y = json.loads(x)
# the result is a Python dictionary:
print(y)

#You can convert Python objects of the following types, 
# into JSON strings:
#您可以把以下類型的 Python 物件轉換為 JSON 字串：
#dict
#list
#tuple
#string
#int
#float
#True
#False
#None
print("----------------------------把 Python 轉換為 JSON-2")
#Convert Python objects into JSON strings, and print the values:
#將 Python 物件轉換為 JSON 字串，並列印值：
import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
#When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
#當 Python 轉換為 JSON 時，Python 物件會被轉換為 JSON（JavaScript）等效項：
#Python	    JSON
#dict	    Object
#list	    Array
#tuple	    Array
#str	    String
#int	    Number
#float	    Number
#True	    true
#False	    false
#None	    null

print("----------------------------把 Python 轉換為 JSON-3")
#Convert a Python object containing all the legal data types:
#轉換包含所有合法資料類型的 Python 物件：
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
print("----------------------------使用 indent 參數定義縮進數")
print(json.dumps(x, indent=4))
print("-------------------使用 separators 參數來變更預設分隔符")
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print("-----------使用 sort_keys 參數來指定是否應對結果進行排序")
print(json.dumps(x, indent=4, sort_keys=True))
#按照鍵的第一個字母做排序
#Format the Result
#格式化結果
#The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
#上面的實例列印一個 JSON 字串，但它不是很容易閱讀，沒有縮進和換行。
#The json.dumps() method has parameters to make it easier to read the result:
#json.dumps（） 方法提供了令結果更易讀的參數：
#Use the indent parameter to define the numbers of indents:
#使用 indent 參數定義縮進數：
json.dumps(x, indent=4)
#You can also define the separators, default value is 
# (", ", ": "), which means using a comma and a space 
# to separate each object, and a colon and a space to 
# separate keys from values:
#您還可以定義分隔符，預設值為（"， "， "： "），這意味著使用
# 逗號和空格分隔每個物件，使用冒號和空格將鍵與值分開：
#Use the separators parameter to change the default separator:
#使用 separators 參數來變更預設分隔符：
json.dumps(x, indent=4, separators=(". ", " = "))

#Order the Result
#對結果排序
#The json.dumps() method has parameters to order the 
# keys in the result:
#json.dumps（） 方法提供了對結果中的鍵進行排序的參數：
#Use the sort_keys parameter to specify if the result 
# should be sorted or not:
#使用 sort_keys 參數來指定是否應對結果進行排序：
json.dumps(x, indent=4, sort_keys=True)